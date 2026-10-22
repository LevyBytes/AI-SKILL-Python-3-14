# argparse: Required mutually exclusive groups and nesting limits

```python
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> group = parser.add_mutually_exclusive_group()
>>> group.add_argument('--foo', action='store_true')
>>> group.add_argument('--bar', action='store_false')
>>> parser.parse_args(['--foo'])
Namespace(bar=True, foo=True)
>>> parser.parse_args(['--bar'])
Namespace(bar=False, foo=False)
>>> parser.parse_args(['--foo', '--bar'])
usage: PROG [-h] [--foo | --bar]
PROG: error: argument --bar: not allowed with argument --foo

```

A *required* argument may additionally be passed to `add_mutually_exclusive_group()`, signalling that one or more of the mutually exclusive arguments has to be supplied:

```python
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> group = parser.add_mutually_exclusive_group(required=True)
>>> group.add_argument('--foo', action='store_true')
>>> group.add_argument('--bar', action='store_false')
>>> parser.parse_args([])
usage: PROG [-h] (--foo | --bar)
PROG: error: one of the arguments --foo --bar is required

```

Be aware that, as things stand, mutually exclusive argument groups offer no *title* or *description* arguments the way `add_argument_group()` does. You can nonetheless place a mutually exclusive group inside an argument group that already carries a title and a description. Here is an illustration:

```python
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> group = parser.add_argument_group('Group title', 'Group description')
>>> exclusive_group = group.add_mutually_exclusive_group(required=True)
>>> exclusive_group.add_argument('--foo', help='foo help')
>>> exclusive_group.add_argument('--bar', help='bar help')
>>> parser.print_help()
usage: PROG [-h] (--foo FOO | --bar BAR)

options:
  -h, --help  show this help message and exit

Group title:
  Group description

  --foo FOO   foo help
  --bar BAR   bar help

```

Deprecated since version 3.11, removed in version 3.14: Invoking `add_argument_group()` or `add_mutually_exclusive_group()` on a mutually exclusive group raises an exception from now on. That kind of nesting had never been a supported configuration, frequently misbehaved, and only showed up by accident because of inheritance.

[Subject index](INDEX.md) · [Continue](argumentparser-set-defaults-to-argumentparser-get-default.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md) · [Owning module, declaration or section: Mutual exclusion](argumentparser-add-mutually-exclusive-group.md) · [Owning module, declaration or section: ArgumentParser.add_mutually_exclusive_group](argumentparser-add-mutually-exclusive-group.md) · [Preceding source contract and version conditions](argumentparser-add-mutually-exclusive-group.md)
