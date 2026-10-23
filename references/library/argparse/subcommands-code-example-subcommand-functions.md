# argparse - Subcommands - Code example: >>> # subcommand functions

```python
>>> # subcommand functions
>>> def foo(args):
...     print(args.x * args.y)
...
>>> def bar(args):
...     print('((%s))' % args.z)
...
>>> # create the top-level parser
>>> parser = argparse.ArgumentParser()
>>> subparsers = parser.add_subparsers(required=True)
>>>
>>> # create the parser for the "foo" command
>>> parser_foo = subparsers.add_parser('foo')
>>> parser_foo.add_argument('-x', type=int, default=1)
>>> parser_foo.add_argument('y', type=float)
>>> parser_foo.set_defaults(func=foo)
>>>
>>> # create the parser for the "bar" command
>>> parser_bar = subparsers.add_parser('bar')
>>> parser_bar.add_argument('z')
>>> parser_bar.set_defaults(func=bar)
>>>
>>> # parse the args and call whatever function was selected
>>> args = parser.parse_args('foo 1 -x 2'.split())
>>> args.func(args)
2.0
>>>
>>> # parse the args and call whatever function was selected
>>> args = parser.parse_args('bar XYZYX'.split())
>>> args.func(args)
((XYZYX))

```

Doing it this way leaves `parse_args()` to invoke the right function once parsing finishes. Tying functions to actions in this fashion is generally the simplest path to managing the distinct actions of each of your subparsers. That said, when you do need to discover which subparser ran, the `dest` keyword argument passed to `add_subparsers()` does the trick:

```python
>>> parser = argparse.ArgumentParser()
>>> subparsers = parser.add_subparsers(dest='subparser_name')
>>> subparser1 = subparsers.add_parser('1')
>>> subparser1.add_argument('-x')
>>> subparser2 = subparsers.add_parser('2')
>>> subparser2.add_argument('y')
>>> parser.parse_args(['2', 'frobble'])
Namespace(subparser_name='2', y='frobble')

```

Changed in version 3.7: New *required* keyword-only parameter.

Changed in version 3.14: A custom usage message set on the main parser no longer changes a subparser's *prog*.

[Subject index](INDEX.md) · [Previous](subcommands-code-example-parser-parse-args-help.md) · [Continue](argparse-filetype-class.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md) · [Owning module, declaration or section: Subcommands](argumentparser-add-subparsers.md) · [Owning module, declaration or section: ArgumentParser.add_subparsers](argumentparser-add-subparsers.md)
