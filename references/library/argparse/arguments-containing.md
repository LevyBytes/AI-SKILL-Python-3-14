# argparse - Arguments containing `-`

### Arguments containing `-`

Wherever the user has plainly slipped up, `parse_args()` tries to raise errors, yet certain cases stay ambiguous by their nature. Take the command-line argument `-1`: it might be meant as an option or as a positional argument. Here `parse_args()` plays it safe: a positional argument is allowed to start with `-` only when it resembles a negative number and the parser holds no options that themselves resemble negative numbers:

```python
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-x')
>>> parser.add_argument('foo', nargs='?')

>>> # no negative number options, so -1 is a positional argument
>>> parser.parse_args(['-x', '-1'])
Namespace(foo=None, x='-1')

>>> # no negative number options, so -1 and -5 are positional arguments
>>> parser.parse_args(['-x', '-1', '-5'])
Namespace(foo='-5', x='-1')

>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-1', dest='one')
>>> parser.add_argument('foo', nargs='?')

>>> # negative number options present, so -1 is an option
>>> parser.parse_args(['-1', 'X'])
Namespace(foo=None, one='X')

>>> # negative number options present, so -2 is an option
>>> parser.parse_args(['-2'])
usage: PROG [-h] [-1 ONE] [foo]
PROG: error: unrecognized arguments: -2

>>> # negative number options present, so both -1s are options
>>> parser.parse_args(['-1', '-1'])
usage: PROG [-h] [-1 ONE] [foo]
PROG: error: argument -1: expected one argument
```

When your positional arguments have to start with `-` yet don't resemble negative numbers, place the pseudo-argument `'--'` ahead of them; that signals to `parse_args()` that whatever follows is positional:

```python
>>> parser.parse_args(['--', '-f'])
Namespace(foo='-f', one=None)

```

See also [the argparse howto on ambiguous arguments](https://docs.python.org/3.14/howto/argparse.html#specifying-ambiguous-arguments) for more details.

[Subject index](INDEX.md) · [Previous](invalid-arguments.md) · [Continue](argument-abbreviations-prefix-matching.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
