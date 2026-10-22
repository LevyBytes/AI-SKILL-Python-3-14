# argparse: `argparse.BooleanOptionalAction`

*class *argparse.BooleanOptionalAction

This `Action` subclass deals with boolean flags that carry both a positive and a negative form. Registering one argument like `--foo` produces the pair `--foo` and `--no-foo`, which store `True` and `False` in turn:

```python
>>> import argparse
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', action=argparse.BooleanOptionalAction)
>>> parser.parse_args(['--no-foo'])
Namespace(foo=False)

```

Added in version 3.9.

[Subject index](INDEX.md) · [Previous](argparse-action-call-to-argparse-action-format-usage.md) · [Continue](argumentparser-parse-args.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md) · [Owning module, declaration or section: Action classes](argparse-action-class.md)
