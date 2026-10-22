# Specifying ambiguous arguments

### Specifying ambiguous arguments

When it's unclear whether an argument is positional or belongs to an option, `--` can serve to inform [`parse_args()`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser.parse_args) that everything past it counts as a positional argument:

```python
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-n', nargs='+')
>>> parser.add_argument('args', nargs='*')

>>> # ambiguous, so parse_args assumes it's an option
>>> parser.parse_args(['-f'])
usage: PROG [-h] [-n N [N ...]] [args ...]
PROG: error: unrecognized arguments: -f

>>> parser.parse_args(['--', '-f'])
Namespace(args=['-f'], n=None)

>>> # ambiguous, so the -n option greedily accepts arguments
>>> parser.parse_args(['-n', '1', '2', '3'])
Namespace(args=[], n=['1', '2', '3'])

>>> parser.parse_args(['-n', '1', '--', '2', '3'])
Namespace(args=['2', '3'], n=['1'])

```

[Subject index](INDEX.md) · [Previous source context](getting-a-little-more-advanced.md) · [Following source context](conflicting-options.md)
