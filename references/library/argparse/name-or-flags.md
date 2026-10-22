# argparse — name or flags

What follows explains the role each of these plays.

### name or flags

When you call `add_argument()`, it needs to be told whether you intend an optional argument (something like `-f` or `--foo`) or a positional one (such as a list of filenames). For that reason, the leading arguments you hand to `add_argument()` should be either one or more flags, or just a plain argument name.

As an illustration, here is how you might define an optional argument:

```python
>>> parser.add_argument('-f', '--foo')

```

and a positional argument can be defined this way:

```python
>>> parser.add_argument('bar')

```

Once `parse_args()` runs, anything carrying the `-` prefix is treated as optional, while whatever is left over is taken to be positional:

```python
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-f', '--foo')
>>> parser.add_argument('bar')
>>> parser.parse_args(['BAR'])
Namespace(bar='BAR', foo=None)
>>> parser.parse_args(['BAR', '--foo', 'FOO'])
Namespace(bar='BAR', foo='FOO')
>>> parser.parse_args(['--foo', 'FOO'])
usage: PROG [-h] [-f FOO] bar
PROG: error: the following arguments are required: bar

```

Out of the box, `argparse` takes care of an argument's internal name and its displayed name on its own, so the workflow stays simple and no extra setup is needed. Consequently, supplying the dest and metavar parameters is unnecessary. With optional arguments, dest falls back to the argument's own name, where any hyphens `-` become underscores `_`. The metavar value, meanwhile, defaults to that name in upper case. Here is an example:

```python
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('--foo-bar')
>>> parser.parse_args(['--foo-bar', 'FOO-BAR'])
Namespace(foo_bar='FOO-BAR')
>>> parser.print_help()
usage:  [-h] [--foo-bar FOO-BAR]

optional arguments:
 -h, --help  show this help message and exit
 --foo-bar FOO-BAR

```

[Subject index](INDEX.md) · [Continue](action-section-introduction-and-initial-examples.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md) · [Owning module, declaration or section: The add_argument() method](the-add-argument-method.md) · [Preceding source contract and version conditions](the-add-argument-method.md)
