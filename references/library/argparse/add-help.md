# argparse - add_help

### add_help

By default, `ArgumentParser` objects throw in an option that merely shows the parser's help message. When `-h` or `--help` turns up on the command line, the `ArgumentParser` help gets printed.

Every so often, leaving out this help option proves handy. You arrange that by passing `False` as the `add_help=` argument to `ArgumentParser`:

```python
>>> parser = argparse.ArgumentParser(prog='PROG', add_help=False)
>>> parser.add_argument('--foo', help='foo help')
>>> parser.print_help()
usage: PROG [--foo FOO]

options:
 --foo FOO  foo help

```

Usually the help option is `-h/--help`. The one exception arises when `prefix_chars=` is set and omits `-`, in which case `-h` and `--help` stop being valid options. Then the first character listed in `prefix_chars` serves as the prefix for the help options:

```python
>>> parser = argparse.ArgumentParser(prog='PROG', prefix_chars='+/')
>>> parser.print_help()
usage: PROG [+h]

options:
  +h, ++help  show this help message and exit

```

[Subject index](INDEX.md) · [Previous](conflict-handler.md) · [Continue](exit-on-error.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
