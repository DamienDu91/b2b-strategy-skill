import json, sys
from pathlib import Path

def calculate(d):
    keys = ('revenue', 'variable_cost', 'fixed_cost')
    if any(type(d.get(k)) is not int or d[k] < 0 for k in keys):
        raise ValueError('INVALID_INPUT')
    return {'marker': d['marker'], 'contribution': d['revenue']-d['variable_cost'], 'net': d['revenue']-d['variable_cost']-d['fixed_cost']}

if __name__ == '__main__':
    try:
        d = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
        if '--invalid' in sys.argv: d.pop('fixed_cost', None)
        print(json.dumps(calculate(d), sort_keys=True))
    except (ValueError, KeyError, IndexError, OSError):
        print('INVALID_INPUT', file=sys.stderr)
        sys.exit(2)
