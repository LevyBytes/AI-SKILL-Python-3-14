# argparse — Argument groups

### Argument groups

 ArgumentParser.add_argument_group(*title=None*, *description=None*, ***[, *argument_default*][, *conflict_handler*])

When printing help messages, `ArgumentParser` by default sorts command-line arguments into “positional arguments” and “options”. If a clearer conceptual grouping exists than that default, you can build fitting groups with the `add_argument_group()` method:

```python
>>> parser = argparse.ArgumentParser(prog='PROG', add_help=False)
>>> group = parser.add_argument_group('group')
>>> group.add_argument('--foo', help='foo help')
>>> group.add_argument('bar', help='bar help')
>>> parser.print_help()
usage: PROG [--foo FOO] bar

group:
  bar    bar help
  --foo FOO  foo help

```

What `add_argument_group()` returns is an argument group object that carries an `add_argument()` method exactly like an ordinary `ArgumentParser`. Once an argument joins the group, the parser handles it just as it would any normal argument, only it shows the argument in its own group within help messages. The `add_argument_group()` method takes *title* and *description* arguments you can use to tailor this display:

```python
>>> parser = argparse.ArgumentParser(prog='PROG', add_help=False)
>>> group1 = parser.add_argument_group('group1', 'group1 description')
>>> group1.add_argument('foo', help='foo help')
>>> group2 = parser.add_argument_group('group2', 'group2 description')
>>> group2.add_argument('--bar', help='bar help')
>>> parser.print_help()
usage: PROG [--bar BAR] foo

group1:
  group1 description

  foo    foo help

group2:
  group2 description

  --bar BAR  bar help

```

The optional, keyword-only parameters argument_default and conflict_handler give you finer control over how the argument group behaves. They carry the same meaning they have in the `ArgumentParser` constructor, except they apply only to the argument group instead of the whole parser.

Keep in mind that whatever arguments fall outside your own defined groups will drop back into the standard “positional arguments” and “optional arguments” sections.

Inside each argument group, the help output lists arguments in the same order they were added.

Deprecated since version 3.11, removed in version 3.14: An exception is now raised when `add_argument_group()` runs against an argument group. Such nesting had no support, frequently misbehaved, and only surfaced by accident because of inheritance.

Deprecated since version 3.14: Passing prefix_chars to `add_argument_group()` is now deprecated.

[Subject index](INDEX.md) · [Previous](argparse-filetype-class.md) · [Continue](argumentparser-add-mutually-exclusive-group.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
