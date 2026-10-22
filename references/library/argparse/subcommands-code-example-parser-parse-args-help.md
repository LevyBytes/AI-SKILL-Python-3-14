# argparse — Subcommands — Code example: >>> parser.parse_args(['--help'])

```python
>>> parser.parse_args(['--help'])
usage: PROG [-h] [--foo] {a,b} ...

positional arguments:
  {a,b}   subcommand help
    a     a help
    b     b help

options:
  -h, --help  show this help message and exit
  --foo   foo help

>>> parser.parse_args(['a', '--help'])
usage: PROG a [-h] bar

positional arguments:
  bar     bar help

options:
  -h, --help  show this help message and exit

>>> parser.parse_args(['b', '--help'])
usage: PROG b [-h] [--baz {X,Y,Z}]

options:
  -h, --help     show this help message and exit
  --baz {X,Y,Z}  baz help

```

Beyond that, `add_subparsers()` honors the `title` and `description` keyword arguments. Supply either one and the subparser's commands gather into their own section of the help output. For instance:

```python
>>> parser = argparse.ArgumentParser()
>>> subparsers = parser.add_subparsers(title='subcommands',
...                                    description='valid subcommands',
...                                    help='additional help')
>>> subparsers.add_parser('foo')
>>> subparsers.add_parser('bar')
>>> parser.parse_args(['-h'])
usage:  [-h] {foo,bar} ...

options:
  -h, --help  show this help message and exit

subcommands:
  valid subcommands

  {foo,bar}   additional help

```

On top of that, `add_parser()` accepts an extra *aliases* argument that lets several strings point at the same subparser. The next example, mirroring `svn`, makes `co` a shorthand for `checkout`:

```python
>>> parser = argparse.ArgumentParser()
>>> subparsers = parser.add_subparsers()
>>> checkout = subparsers.add_parser('checkout', aliases=['co'])
>>> checkout.add_argument('foo')
>>> parser.parse_args(['co', 'bar'])
Namespace(foo='bar')

```

`add_parser()` likewise takes an extra *deprecated* argument, which lets you mark the subparser as deprecated.

```python
>>> import argparse
>>> parser = argparse.ArgumentParser(prog='chicken.py')
>>> subparsers = parser.add_subparsers()
>>> run = subparsers.add_parser('run')
>>> fly = subparsers.add_parser('fly', deprecated=True)
>>> parser.parse_args(['fly'])
chicken.py: warning: command 'fly' is deprecated
Namespace()

```

Added in version 3.13.

A notably clean approach to subcommands pairs the `add_subparsers()` method with `set_defaults()` calls, letting each subparser carry the Python function it ought to run. For example:

[Subject index](INDEX.md) · [Previous](argumentparser-add-subparsers.md) · [Continue](subcommands-code-example-subcommand-functions.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md) · [Owning module, declaration or section: Subcommands](argumentparser-add-subparsers.md) · [Owning module, declaration or section: ArgumentParser.add_subparsers](argumentparser-add-subparsers.md)
