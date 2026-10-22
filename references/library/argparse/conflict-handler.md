# argparse — conflict_handler

### conflict_handler

Two actions sharing one option string are not permitted on `ArgumentParser` objects. By default, an `ArgumentParser` object raises an exception the moment you try to create an argument whose option string is already taken:

```python
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-f', '--foo', help='old foo help')
>>> parser.add_argument('--foo', help='new foo help')
Traceback (most recent call last):
 ..
ArgumentError: argument --foo: conflicting option string(s): --foo

```

There are cases (for example, when working with parents) where it is simply handy to overwrite any earlier arguments carrying the same option string. To get that behavior, hand the value `'resolve'` to the `conflict_handler=` argument of `ArgumentParser`:

```python
>>> parser = argparse.ArgumentParser(prog='PROG', conflict_handler='resolve')
>>> parser.add_argument('-f', '--foo', help='old foo help')
>>> parser.add_argument('--foo', help='new foo help')
>>> parser.print_help()
usage: PROG [-h] [-f FOO] [--foo FOO]

options:
 -h, --help  show this help message and exit
 -f FOO      old foo help
 --foo FOO   new foo help

```

Be aware that an `ArgumentParser` object drops an action only once every one of its option strings has been overridden. So, in the example above, the old `-f/--foo` action survives as the `-f` action, because the `--foo` option string was the only one overridden.

[Subject index](INDEX.md) · [Previous](allow-abbrev.md) · [Continue](add-help.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
