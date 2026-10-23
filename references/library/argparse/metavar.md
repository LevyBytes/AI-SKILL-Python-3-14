# argparse - metavar

### metavar

As `ArgumentParser` builds help messages, it requires a way to name each expected argument. By default an `ArgumentParser` object falls back on the dest value as the "name" for each object. By default, positional argument actions use the dest value just as it is, while optional argument actions present the dest value in upper case. Thus a lone positional argument with `dest='bar'` ends up referred to as `bar`. A solitary optional argument `--foo` meant to be trailed by one command-line argument ends up referred to as `FOO`. Here is an example:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo')
>>> parser.add_argument('bar')
>>> parser.parse_args('X --foo Y'.split())
Namespace(bar='X', foo='Y')
>>> parser.print_help()
usage:  [-h] [--foo FOO] bar

positional arguments:
 bar

options:
 -h, --help  show this help message and exit
 --foo FOO

```

A different name can be set by way of `metavar`:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', metavar='YYY')
>>> parser.add_argument('bar', metavar='XXX')
>>> parser.parse_args('X --foo Y'.split())
Namespace(bar='X', foo='Y')
>>> parser.print_help()
usage:  [-h] [--foo YYY] XXX

positional arguments:
 XXX

options:
 -h, --help  show this help message and exit
 --foo YYY

```

Bear in mind that `metavar` alters only the *displayed* name - the name of the attribute on the `parse_args()` object still comes from the dest value.

Various `nargs` settings can lead to the metavar appearing more than once. By handing a tuple to `metavar`, you set a separate display for each of the arguments:

```python
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-x', nargs=2)
>>> parser.add_argument('--foo', nargs=2, metavar=('bar', 'baz'))
>>> parser.print_help()
usage: PROG [-h] [-x X X] [--foo bar baz]

options:
 -h, --help     show this help message and exit
 -x X X
 --foo bar baz

```

[Subject index](INDEX.md) · [Previous](help.md) · [Continue](dest.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
