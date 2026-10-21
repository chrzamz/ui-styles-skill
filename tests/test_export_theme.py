import copy
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'export_theme.py'
spec = importlib.util.spec_from_file_location('export_theme', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def sample():
    colors = dict(zip(module.COLORS, ['#ffffff', '#f4f4f4', '#181818', '#595959', '#b3b3b3',
        '#b32837', '#ffffff', '#206a3d', '#805300', '#b42318', '#1a55a0']))
    return {'schemaVersion': 1, 'name': 'test-fixture-not-a-default', 'modes': {'light': colors},
            'typography': {'fontFamily': '"Noto Sans SC", sans-serif', 'fontSize': 14, 'lineHeight': 1.5},
            'shape': {'borderRadius': 6}, 'spacing': {'unit': 4}, 'control': {'height': 36},
            'motion': {'duration': 160, 'reducedMotion': True}}


class ExportThemeTests(unittest.TestCase):
    def test_no_implicit_dark_palette(self):
        data = sample()
        for library in module.WARNINGS:
            with self.subTest(library=library):
                text = module.render(data, library)
                self.assertNotIn('"dark": {', text)
        del data['modes']['light']['primary']
        with self.assertRaisesRegex(ValueError, 'primary'):
            module.render(data, 'css')

    def test_color_injection_rejected_for_all_adapters(self):
        for bad in ['red; } body { display: none', 'url(https://example.com)', '#abcdef\n!important', 'var(--x); color:red']:
            for library in module.WARNINGS:
                data = sample()
                data['modes']['light']['primary'] = bad
                with self.subTest(bad=bad, library=library), self.assertRaises(ValueError):
                    module.render(data, library)

    def test_font_injection_rejected(self):
        data = sample()
        data['typography']['fontFamily'] = 'sans-serif; } @import url(x);'
        with self.assertRaisesRegex(ValueError, 'fontFamily'):
            module.render(data, 'css')

    def test_malformed_color_functions_rejected(self):
        for color in ['rgb(1)', 'rgb(1,,2)', 'rgb(1 2 3 / / 1)', 'oklch(50%, 0.1, 20)', 'hsl(90 20 30)']:
            data = sample()
            data['modes']['light']['primary'] = color
            with self.subTest(color=color), self.assertRaises(ValueError):
                module.render(data, 'css')
        for color in ['rgb(10, 20, 30)', 'rgb(10 20 30 / 50%)', 'hsl(30 50% 60%)', 'oklch(60% 0.2 30)']:
            data = sample()
            data['modes']['light']['primary'] = color
            self.assertIn(color, module.render(data, 'css'))

    def test_library_color_algorithms_require_resolved_hex(self):
        for color in ['var(--brand)', 'oklch(60% 0.2 30)', '#11223380']:
            data = sample()
            data['modes']['light']['primary'] = color
            self.assertIn(color, module.render(data, 'css'))
            self.assertIn(color, module.render(data, 'semi'))
            for library in ['antd', 'mui']:
                with self.assertRaisesRegex(ValueError, 'requires opaque'):
                    module.render(data, library)

    def test_invalid_numeric_and_schema_values(self):
        for section, key, value in [('spacing', 'unit', 0), ('shape', 'borderRadius', -1),
                                    ('control', 'height', True), ('motion', 'duration', float('nan')),
                                    ('motion', 'reducedMotion', 'false')]:
            data = sample()
            data[section][key] = value
            with self.subTest(section=section), self.assertRaises(ValueError):
                module.render(data, 'css')
        for version in [True, 2, '1']:
            data = sample()
            data['schemaVersion'] = version
            with self.assertRaises(ValueError):
                module.render(data, 'css')

    def test_antd_semantic_mapping(self):
        data = sample()
        tokens = module.antd_tokens(data, data['modes']['light'])
        self.assertEqual(tokens['colorPrimary'], '#b32837')
        self.assertEqual(tokens['colorTextLightSolid'], '#ffffff')
        self.assertEqual(tokens['controlOutline'], '#1a55a0')
        self.assertEqual(tokens['sizeUnit'], 4)
        self.assertEqual(tokens['motionDurationMid'], '0.16s')

    def test_mui_palette_and_control_mapping(self):
        data = sample()
        options = module.mui_options(data, 'light', data['modes']['light'])
        self.assertEqual(options['palette']['primary']['contrastText'], '#ffffff')
        self.assertEqual(options['palette']['background']['paper'], '#f4f4f4')
        self.assertEqual(options['spacing'], 4)
        self.assertEqual(options['typography']['body1']['fontSize'], '14px')
        self.assertEqual(options['components']['MuiButton']['styleOverrides']['root']['minHeight'], 36)
        self.assertEqual(options['palette']['mode'], 'light')

    def test_dark_mode_values_are_not_copied_from_light(self):
        data = sample()
        data['modes']['dark'] = copy.deepcopy(data['modes']['light'])
        data['modes']['dark']['background'] = '#121212'
        for library in module.WARNINGS:
            output = module.render(data, library)
            self.assertIn('#121212', output)
        self.assertIn('body[theme-mode="dark"]', module.render(data, 'semi'))
        self.assertIn(':root[data-ui-mode="dark"]', module.render(data, 'css'))

    def test_semi_does_not_put_hex_into_rgb_channels(self):
        output = module.render(sample(), 'semi')
        self.assertIn('--semi-color-primary: #b32837;', output)
        self.assertNotIn('--semi-blue-5:', output)
        self.assertNotIn('--semi-color-white:', output)
        self.assertIn('PARTIAL SEMI ADAPTER', output)

    def test_reduced_motion_is_explicit(self):
        data = sample()
        self.assertIn('@media (prefers-reduced-motion: reduce)', module.render(data, 'css'))
        data['motion']['reducedMotion'] = False
        self.assertNotIn('@media', module.render(data, 'css'))
        self.assertIn('false && prefersReducedMotion', module.render(data, 'antd'))

    def test_cli_refuses_overwrite_and_symlink(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source, target = root / 'tokens.json', root / 'theme.css'
            source.write_text(json.dumps(sample()))
            command = [sys.executable, str(SCRIPT), str(source), '--library', 'css', '--output', str(target)]
            first = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertIn('Review required:', first.stderr)
            target.write_text('KEEP')
            second = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(second.returncode, 2)
            self.assertEqual(target.read_text(), 'KEEP')
            target.unlink()
            target.symlink_to(root / 'missing.css')
            third = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(third.returncode, 2)
            self.assertFalse((root / 'missing.css').exists())

    def test_invalid_input_leaves_no_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source, target = root / 'tokens.json', root / 'theme.css'
            source.write_text('{}')
            result = subprocess.run([sys.executable, str(SCRIPT), str(source), '--library', 'css',
                                     '--output', str(target)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertFalse(target.exists())

    @unittest.skipUnless(os.environ.get('UI_STYLES_THEME_CHECK_NODE_MODULES') and shutil.which('node'),
                         'Optional real-library regression: set UI_STYLES_THEME_CHECK_NODE_MODULES')
    def test_real_library_types_providers_and_semantic_values(self):
        dependencies = Path(os.environ['UI_STYLES_THEME_CHECK_NODE_MODULES']).resolve()
        self.assertTrue((dependencies / 'typescript/bin/tsc').is_file())
        data = sample()
        data['modes']['dark'] = {**data['modes']['light'], 'background': '#121820', 'primary': '#8DBEE8'}
        with tempfile.TemporaryDirectory(prefix='ui-styles-theme-regression-') as tmp:
            root = Path(tmp)
            (root / 'node_modules').symlink_to(dependencies, target_is_directory=True)
            (root / 'package.json').write_text('{"type":"commonjs"}')
            (root / 'antd-theme.ts').write_text(module.render(data, 'antd'))
            (root / 'mui-theme.ts').write_text(module.render(data, 'mui'))
            (root / 'tsconfig.json').write_text(json.dumps({'compilerOptions': {
                'target': 'ES2022', 'module': 'Node16', 'moduleResolution': 'Node16',
                'strict': True, 'esModuleInterop': True, 'skipLibCheck': True,
                'noEmitOnError': True, 'outDir': 'dist'}, 'include': ['*.ts']}))
            (root / 'check.ts').write_text('''
import { createElement } from 'react';
import { renderToString } from 'react-dom/server';
import { ConfigProvider, Button as AntButton, theme } from 'antd';
import { ThemeProvider } from '@mui/material/styles';
import MuiButton from '@mui/material/Button';
import { getUiTheme } from './antd-theme';
import { createUiTheme } from './mui-theme';
function eq(actual: unknown, expected: unknown) {
  if (actual !== expected) throw new Error(JSON.stringify({actual, expected}));
}
for (const mode of ['light', 'dark']) {
  const primary = mode === 'light' ? '#b32837' : '#8DBEE8';
  const ant = theme.getDesignToken(getUiTheme(mode));
  eq(ant.colorPrimary, primary);
  eq(ant.colorSuccess, '#206a3d');
  eq(ant.colorWarning, '#805300');
  eq(ant.colorError, '#b42318');
  eq(ant.controlHeight, 36);
  eq(ant.motionDurationMid, '0.16s');
  const reduced = theme.getDesignToken(getUiTheme(mode, true));
  eq(reduced.motion, false);
  for (const duration of [reduced.motionDurationFast, reduced.motionDurationMid, reduced.motionDurationSlow]) eq(duration, '0s');
  const mui = createUiTheme(mode);
  eq(mui.palette.primary.main, primary);
  eq(mui.spacing(2), '8px');
  eq(mui.typography.body1.fontSize, '14px');
  eq(createUiTheme(mode, true).transitions.duration.standard, 0);
  const antHtml = renderToString(createElement(ConfigProvider, {theme:getUiTheme(mode)}, createElement(AntButton, {type:'primary'}, 'Ant test')));
  const muiHtml = renderToString(createElement(ThemeProvider, {theme:mui}, createElement(MuiButton, {variant:'contained'}, 'MUI test')));
  eq(antHtml.includes('Ant test'), true);
  eq(muiHtml.includes('MUI test'), true);
}
console.log('real-library regression passed');
''')
            check = subprocess.run([shutil.which('node'), str(dependencies / 'typescript/bin/tsc'),
                                    '--pretty', 'false'], cwd=root, capture_output=True, text=True)
            self.assertEqual(check.returncode, 0, check.stdout + check.stderr)
            runtime = subprocess.run([shutil.which('node'), 'dist/check.js'], cwd=root,
                                     capture_output=True, text=True)
            self.assertEqual(runtime.returncode, 0, runtime.stdout + runtime.stderr)


if __name__ == '__main__':
    unittest.main()
