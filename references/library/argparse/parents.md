# argparse — parents

### parents

On occasion, a group of parsers will hold a shared collection of arguments in common. Instead of writing out the definitions of those arguments over and over, you can build one parser carrying all the shared arguments and feed it to the `parents=` argument of `ArgumentParser`. The `parents=` argument accepts a list of `ArgumentParser` objects, gathers every positional and optional action they hold, and adds those actions to the `ArgumentParser` object under construction:

```python
>>> parent_parser = argparse.ArgumentParser(add_help=False)
>>> parent_parser.add_argument('--parent', type=int)

>>> foo_parser = argparse.ArgumentParser(parents=[parent_parser])
>>> foo_parser.add_argument('foo')
>>> foo_parser.parse_args(['--parent', '2', 'XXX'])
Namespace(foo='XXX', parent=2)

>>> bar_parser = argparse.ArgumentParser(parents=[parent_parser])
>>> bar_parser.add_argument('--bar')
>>> bar_parser.parse_args(['--bar', 'YYY'])
Namespace(bar='YYY', parent=None)

```

Bear in mind that the bulk of parent parsers will set `add_help=False`. If they don't, the `ArgumentParser` ends up seeing two `-h/--help` options — one from the parent and one from the child — and throws an error.

Note

The parsers have to be completely set up before you hand them off via `parents=`. Editing the parent parsers once the child parser exists leaves those edits absent from the child.

[Subject index](INDEX.md) · [Previous](epilog.md) · [Continue](formatter-class.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
