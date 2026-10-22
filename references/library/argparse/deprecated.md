# argparse — deprecated

### deprecated

Over the course of a project, certain arguments will eventually need to disappear from the command line. Ahead of dropping them, warn your users that those arguments are deprecated and slated for removal. The `add_argument()` call accepts a `deprecated` keyword argument, defaulting to `False`, that marks whether the argument is deprecated and destined to go away later. When `deprecated` is `True` for an argument, supplying it on the command line triggers a warning sent to [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr):

```python
>>> import argparse
>>> parser = argparse.ArgumentParser(prog='snake.py')
>>> parser.add_argument('--legs', default=0, type=int, deprecated=True)
>>> parser.parse_args([])
Namespace(legs=0)
>>> parser.parse_args(['--legs', '4'])
snake.py: warning: option '--legs' is deprecated
Namespace(legs=4)

```

Added in version 3.13.

[Subject index](INDEX.md) · [Previous](dest.md) · [Continue](argparse-action-class.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
