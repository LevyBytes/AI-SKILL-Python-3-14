# argparse - Invalid arguments

### Invalid arguments

As it works through the command line, `parse_args()` watches for many kinds of mistakes: ambiguous options, invalid types, invalid options, an incorrect count of positional arguments, and more. On hitting any such mistake, it terminates and reports the error together with a usage message:

```python
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('--foo', type=int)
>>> parser.add_argument('bar', nargs='?')

>>> # invalid type
>>> parser.parse_args(['--foo', 'spam'])
usage: PROG [-h] [--foo FOO] [bar]
PROG: error: argument --foo: invalid int value: 'spam'

>>> # invalid option
>>> parser.parse_args(['--bar'])
usage: PROG [-h] [--foo FOO] [bar]
PROG: error: unrecognized arguments: --bar

>>> # wrong number of arguments
>>> parser.parse_args(['spam', 'badger'])
usage: PROG [-h] [--foo FOO] [bar]
PROG: error: unrecognized arguments: badger
```

[Subject index](INDEX.md) · [Previous](option-value-syntax.md) · [Continue](arguments-containing.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
