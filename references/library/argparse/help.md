# argparse — help

### help

The `help` value is a string giving a short account of the argument. Whenever a user asks for help (typically with `-h` or `--help` on the command line), these `help` descriptions get shown next to each argument.

Inside the `help` strings you can place a range of format specifiers, sparing you from repeating items such as the program name or an argument's default. Among the available specifiers are the program name, `%(prog)s`, and most keyword arguments to `add_argument()`, for example `%(default)s`, `%(type)s`, and so on:

```python
>>> parser = argparse.ArgumentParser(prog='frobble')
>>> parser.add_argument('bar', nargs='?', type=int, default=42,
...                     help='the bar to %(prog)s (default: %(default)s)')
>>> parser.print_help()
usage: frobble [-h] [bar]

positional arguments:
 bar     the bar to frobble (default: 42)

options:
 -h, --help  show this help message and exit

```

Because the help string honors %-formatting, getting a literal `%` to show up in it requires escaping it as `%%`.

`argparse` lets you suppress the help entry for particular options by giving the `help` value as `argparse.SUPPRESS`:

```python
>>> parser = argparse.ArgumentParser(prog='frobble')
>>> parser.add_argument('--foo', help=argparse.SUPPRESS)
>>> parser.print_help()
usage: frobble [-h]

options:
  -h, --help  show this help message and exit

```

[Subject index](INDEX.md) · [Previous](required.md) · [Continue](metavar.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
