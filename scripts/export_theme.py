#!/usr/bin/env python3
"""Export explicit project tokens to CSS or a library theme scaffold (stdlib only)."""
import argparse
import json
import math
import re
import sys
from pathlib import Path

COLORS = ('background', 'surface', 'text', 'mutedText', 'border', 'primary',
          'onPrimary', 'success', 'warning', 'danger', 'focus')
HEX = re.compile(r'#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})\Z')
OPAQUE_HEX = re.compile(r'#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})\Z')
CSS_VAR = re.compile(r'var\(--[a-zA-Z_][a-zA-Z0-9_-]*\)\Z')
# A deliberately small, non-executable subset; unsupported CSS syntax is an error.
CSS_FUNCTION = re.compile(r'(?:rgb|rgba|hsl|hsla|oklch|oklab)\([0-9.,% /+\-]+\)\Z')
CSS_NUMBER = re.compile(r'[+-]?(?:\d+(?:\.\d+)?|\.\d+)%?\Z')
WARNINGS = {
    'css': 'CSS variables only: components must consume them. No component states or accessibility result is implied.',
    'antd': 'Base Ant Design theme only. Derived states come from the library algorithm; review component overrides, focus, overlays and contrast. Only medium motion duration is mapped.',
    'mui': 'Base MUI theme only. Control height covers Button/InputBase; focus covers ButtonBase; line height covers body1/body2. Review other slots, states, overlays and contrast.',
    'semi': 'PARTIAL SEMI ADAPTER: only base colors and small radius are mapped. Hover/active/disabled/light palettes, onPrimary, typography, spacing, control height and motion need DSM/SCSS or component-level implementation before acceptance. Unmapped values remain as --ui-* variables.',
}


def require_object(value, label, keys):
    if not isinstance(value, dict):
        raise ValueError(f'{label} must be an object')
    missing, extra = set(keys) - value.keys(), value.keys() - set(keys)
    if missing or extra:
        raise ValueError(f'{label}: missing {sorted(missing)}, unknown {sorted(extra)}')


def positive(value, label, allow_zero=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f'{label} must be a finite number')
    if value < 0 or (value == 0 and not allow_zero):
        raise ValueError(f'{label} must be {"non-negative" if allow_zero else "positive"}')


def safe_color_function(value):
    if not CSS_FUNCTION.fullmatch(value):
        return False
    name, body = value[:-1].split('(', 1)
    if ',' in body:
        if '/' in body or name in ('oklch', 'oklab'):
            return False
        values = [part.strip() for part in body.split(',')]
        if len(values) not in (3, 4):
            return False
    else:
        parts = body.split('/')
        if len(parts) > 2 or len(parts[0].split()) != 3:
            return False
        values = parts[0].split()
        if len(parts) == 2:
            values.append(parts[1].strip())
    if not all(CSS_NUMBER.fullmatch(part) for part in values):
        return False
    if name in ('hsl', 'hsla') and not all(part.endswith('%') for part in values[1:3]):
        return False
    return True


def validate(data, library):
    require_object(data, 'tokens', ('schemaVersion', 'name', 'modes', 'typography', 'shape', 'spacing', 'control', 'motion'))
    if type(data['schemaVersion']) is not int or data['schemaVersion'] != 1:
        raise ValueError('schemaVersion must be 1')
    if not isinstance(data['name'], str) or not data['name'].strip():
        raise ValueError('name must be a non-empty string')
    modes = data['modes']
    if not isinstance(modes, dict) or 'light' not in modes or set(modes) - {'light', 'dark'}:
        raise ValueError('modes must contain light and optionally dark; no implicit dark palette is generated')
    for mode, colors in modes.items():
        require_object(colors, f'modes.{mode}', COLORS)
        for name, color in colors.items():
            if not isinstance(color, str) or not (HEX.fullmatch(color) or CSS_VAR.fullmatch(color)
                    or safe_color_function(color) or color in ('transparent', 'currentColor')):
                raise ValueError(f'modes.{mode}.{name}: use a hex color, simple numeric color function or var(--name); CSS declarations/URLs are not accepted')
            if library in ('antd', 'mui') and not OPAQUE_HEX.fullmatch(color):
                raise ValueError(f'modes.{mode}.{name}: {library} export requires opaque #RGB/#RRGGBB so library color algorithms can resolve it; resolve CSS variables/color functions first')
    require_object(data['typography'], 'typography', ('fontFamily', 'fontSize', 'lineHeight'))
    font = data['typography']['fontFamily']
    if not isinstance(font, str) or not font.strip() or not re.fullmatch(r'[\w ,\-\'".]+', font):
        raise ValueError('typography.fontFamily must be a plain CSS font stack, without declarations, escapes or URLs')
    positive(data['typography']['fontSize'], 'typography.fontSize')
    positive(data['typography']['lineHeight'], 'typography.lineHeight')
    for section, key, zero in [('shape', 'borderRadius', True), ('spacing', 'unit', False), ('control', 'height', False)]:
        require_object(data[section], section, (key,))
        positive(data[section][key], f'{section}.{key}', zero)
    require_object(data['motion'], 'motion', ('duration', 'reducedMotion'))
    positive(data['motion']['duration'], 'motion.duration', True)
    if type(data['motion']['reducedMotion']) is not bool:
        raise ValueError('motion.reducedMotion must be a boolean (whether to honor the system preference)')
    return data


def dump(value):
    return json.dumps(value, ensure_ascii=False, indent=2)


def css_vars(data, colors):
    result = {'--ui-' + re.sub(r'([A-Z])', r'-\1', name).lower(): value for name, value in colors.items()}
    result.update({
        '--ui-font-family': data['typography']['fontFamily'],
        '--ui-font-size': f"{data['typography']['fontSize']:g}px",
        '--ui-line-height': f"{data['typography']['lineHeight']:g}",
        '--ui-radius': f"{data['shape']['borderRadius']:g}px",
        '--ui-space-unit': f"{data['spacing']['unit']:g}px",
        '--ui-control-height': f"{data['control']['height']:g}px",
        '--ui-motion-duration': f"{data['motion']['duration']:g}ms",
    })
    return result


def css_block(selector, values):
    return selector + ' {\n' + ''.join(f'  {key}: {value};\n' for key, value in values.items()) + '}\n'


def render_css(data, semi=False):
    blocks = ['/* Generated base tokens. ' + WARNINGS['semi' if semi else 'css'] + ' */\n']
    mapping = {'background': 'bg-0', 'surface': 'bg-1', 'text': 'text-0', 'mutedText': 'text-2',
               'border': 'border', 'primary': 'primary', 'success': 'success', 'warning': 'warning',
               'danger': 'danger', 'focus': 'focus-border'}
    for mode, colors in data['modes'].items():
        values = css_vars(data, colors)
        if semi:
            values.update({'--semi-color-' + target: colors[source] for source, target in mapping.items()})
            values['--semi-border-radius-small'] = f"{data['shape']['borderRadius']:g}px"
            selector = 'body' if mode == 'light' else 'body[theme-mode="dark"]'
        else:
            selector = ':root' if mode == 'light' else ':root[data-ui-mode="dark"]'
        blocks.append(css_block(selector, values))
    if data['motion']['reducedMotion']:
        selector = 'body, body[theme-mode="dark"]' if semi else ':root, :root[data-ui-mode="dark"]'
        blocks.append('@media (prefers-reduced-motion: reduce) {\n' + css_block(selector, {'--ui-motion-duration': '0ms'}) + '}\n')
    return '\n'.join(blocks)


def antd_tokens(data, colors):
    mapping = {'background': 'colorBgLayout', 'surface': 'colorBgContainer', 'text': 'colorText',
               'mutedText': 'colorTextSecondary', 'border': 'colorBorder', 'primary': 'colorPrimary',
               'onPrimary': 'colorTextLightSolid', 'success': 'colorSuccess', 'warning': 'colorWarning',
               'danger': 'colorError', 'focus': 'controlOutline'}
    result = {target: colors[source] for source, target in mapping.items()}
    result.update({
        'fontFamily': data['typography']['fontFamily'], 'fontSize': data['typography']['fontSize'],
        'lineHeight': data['typography']['lineHeight'], 'borderRadius': data['shape']['borderRadius'],
        'sizeUnit': data['spacing']['unit'], 'controlHeight': data['control']['height'],
        'motionDurationMid': f"{data['motion']['duration'] / 1000:g}s",
    })
    return result


def render_antd(data):
    palettes = {mode: antd_tokens(data, colors) for mode, colors in data['modes'].items()}
    return '''// Generated base theme; review states and component overrides before acceptance.
import { theme as antdTheme } from 'antd';
import type { ThemeConfig } from 'antd';

const tokensByMode: Record<string, NonNullable<ThemeConfig['token']>> = ''' + dump(palettes) + ''';

export function getUiTheme(mode = 'light', prefersReducedMotion = false): ThemeConfig {
  const token = tokensByMode[mode];
  if (!token) throw new Error('No project tokens for mode: ' + mode);
  const reduce = ''' + str(data['motion']['reducedMotion']).lower() + ''' && prefersReducedMotion;
  const algorithm = mode === 'dark' ? antdTheme.darkAlgorithm : antdTheme.defaultAlgorithm;
  return {
    algorithm: (seed) => ({
      ...algorithm(seed),
      // Project semantic colors are final decisions, not seeds to darken again.
      colorPrimary: token.colorPrimary ?? seed.colorPrimary,
      colorSuccess: token.colorSuccess ?? seed.colorSuccess,
      colorWarning: token.colorWarning ?? seed.colorWarning,
      colorError: token.colorError ?? seed.colorError,
    }),
    token: {
      ...token,
      motion: !reduce,
      ...(reduce ? { motionDurationFast: '0s', motionDurationMid: '0s', motionDurationSlow: '0s' } : {}),
    },
  };
}
// Pass getUiTheme(mode, preference) to ConfigProvider's theme prop.
// Use the application's SSR-safe media-query handling for preference; do not read window at module scope.
'''


def mui_options(data, mode, colors):
    height = data['control']['height']
    duration = data['motion']['duration']
    return {
        'palette': {'mode': mode, 'background': {'default': colors['background'], 'paper': colors['surface']},
                    'text': {'primary': colors['text'], 'secondary': colors['mutedText']}, 'divider': colors['border'],
                    'primary': {'main': colors['primary'], 'contrastText': colors['onPrimary']},
                    'success': {'main': colors['success']}, 'warning': {'main': colors['warning']},
                    'error': {'main': colors['danger']}},
        'typography': {'fontFamily': data['typography']['fontFamily'], 'fontSize': data['typography']['fontSize'],
                       'body1': {'fontSize': f"{data['typography']['fontSize']:g}px", 'lineHeight': data['typography']['lineHeight']},
                       'body2': {'lineHeight': data['typography']['lineHeight']}},
        'shape': {'borderRadius': data['shape']['borderRadius']}, 'spacing': data['spacing']['unit'],
        'transitions': {'duration': {'standard': duration}},
        'components': {
            'MuiButton': {'styleOverrides': {'root': {'minHeight': height}}},
            'MuiInputBase': {'styleOverrides': {'root': {'minHeight': height}}},
            'MuiButtonBase': {'styleOverrides': {'root': {'&.Mui-focusVisible': {
                'outline': f"2px solid {colors['focus']}", 'outlineOffset': 2}}}},
        },
    }


def render_mui(data):
    palettes = {mode: mui_options(data, mode, colors) for mode, colors in data['modes'].items()}
    return '''// Generated base theme; review states and component overrides before acceptance.
import { createTheme } from '@mui/material/styles';
import type { ThemeOptions } from '@mui/material/styles';

const optionsByMode: Record<string, ThemeOptions> = ''' + dump(palettes) + ''';

export function createUiTheme(mode = 'light', prefersReducedMotion = false) {
  const options = optionsByMode[mode];
  if (!options) throw new Error('No project tokens for mode: ' + mode);
  const reduce = ''' + str(data['motion']['reducedMotion']).lower() + ''' && prefersReducedMotion;
  return createTheme({
    ...options,
    transitions: reduce ? { duration: {
      shortest: 0, shorter: 0, short: 0, standard: 0, complex: 0, enteringScreen: 0, leavingScreen: 0,
    } } : options.transitions,
  });
}
// Pass createUiTheme(mode, preference) to ThemeProvider; add CssBaseline if the app uses it.
// Pass the system preference from SSR-safe application code. CSS animations and ripples need separate review.
'''


def render(data, library):
    validate(data, library)
    if library == 'antd':
        return render_antd(data)
    if library == 'mui':
        return render_mui(data)
    if library in ('css', 'semi'):
        return render_css(data, semi=library == 'semi')
    raise ValueError(f'Unsupported library: {library}')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('tokens', type=Path)
    parser.add_argument('--library', required=True, choices=tuple(WARNINGS))
    parser.add_argument('--output', type=Path, help='Create a new file; refuses to replace files or symlinks. Default: stdout.')
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.tokens.read_text(encoding='utf-8'))
        output = render(data, args.library)
        if args.output:
            with args.output.open('x', encoding='utf-8') as stream:
                stream.write(output)
        else:
            sys.stdout.write(output)
        print('Review required: ' + WARNINGS[args.library], file=sys.stderr)
        return 0
    except (OSError, ValueError, TypeError, KeyError) as error:
        print(f'export_theme: {error}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
