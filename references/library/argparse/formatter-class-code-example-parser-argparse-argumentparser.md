# argparse - formatter_class - Code example: >>> parser = argparse.ArgumentParser(

```python
>>> parser = argparse.ArgumentParser(
...     prog='PROG',
...     formatter_class=argparse.MetavarTypeHelpFormatter)
>>> parser.add_argument('--foo', type=int)
>>> parser.add_argument('bar', type=float)
>>> parser.print_help()
usage: PROG [-h] [--foo int] float

positional arguments:
  float

options:
  -h, --help  show this help message and exit
  --foo int

```

[Subject index](INDEX.md) · [Previous](help-formatter-classes.md) · [Continue](prefix-chars.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md) · [Owning module, declaration or section: argparse.RawDescriptionHelpFormatter; argparse.RawTextHelpFormatter; argparse.ArgumentDefaultsHelpFormatter; argparse.MetavarTypeHelpFormatter](help-formatter-classes.md) · [Owning module, declaration or section: formatter_class](formatter-class.md)
