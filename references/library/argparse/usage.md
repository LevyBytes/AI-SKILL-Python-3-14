# argparse — usage

### usage

By default, `ArgumentParser` builds the usage message out of the arguments it holds. You can replace that default message by way of the `usage=` keyword argument:

```python
>>> parser = argparse.ArgumentParser(prog='PROG', usage='%(prog)s [options]')
>>> parser.add_argument('--foo', nargs='?', help='foo help')
>>> parser.add_argument('bar', nargs='+', help='bar help')
>>> parser.print_help()
usage: PROG [options]

positional arguments:
 bar          bar help

options:
 -h, --help   show this help message and exit
 --foo [FOO]  foo help

```

Within your usage messages, the `%(prog)s` format specifier stands ready to substitute the program name.

Whenever you give the main parser a custom usage message, it is also worth thinking about passing the `prog` argument to `add_subparsers()`, or both the `prog` and `usage` arguments to `add_parser()`, so that command prefixes and usage details stay consistent across the subparsers.

[Subject index](INDEX.md) · [Previous](prog.md) · [Continue](description.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
