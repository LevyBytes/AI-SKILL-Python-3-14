# argparse - allow_abbrev

### allow_abbrev

Ordinarily, handing an argument list to the `parse_args()` method of an `ArgumentParser` lets it accept abbreviations of long options.

Switching `allow_abbrev` to `False` turns this feature off:

```python
>>> parser = argparse.ArgumentParser(prog='PROG', allow_abbrev=False)
>>> parser.add_argument('--foobar', action='store_true')
>>> parser.add_argument('--foonley', action='store_false')
>>> parser.parse_args(['--foon'])
usage: PROG [-h] [--foobar] [--foonley]
PROG: error: unrecognized arguments: --foon

```

Added in version 3.5.

[Subject index](INDEX.md) · [Previous](argument-default.md) · [Continue](conflict-handler.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
