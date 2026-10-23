# argparse - Subcommands - Signature and initial contract

### Other utilities

### Subcommands

 ArgumentParser.add_subparsers(***[, *title*][, *description*][, *prog*][, *parser_class*][, *action*][, *dest*][, *required*][, *help*][, *metavar*])

A great many programs divide their work among several subcommands; the `svn` program, for instance, fires off subcommands such as `svn checkout`, `svn update`, and `svn commit`. Carving up the work like this works especially well when a single program covers several distinct functions, each wanting its own style of command-line arguments. `ArgumentParser` lets you build these subcommands through the `add_subparsers()` method. You usually call `add_subparsers()` without any arguments, and it hands back a special action object. That object offers one method, `add_parser()`, which accepts a command name plus any `ArgumentParser` constructor arguments and yields an `ArgumentParser` object you can then adjust as you normally would.

Description of parameters:

- *title* - the heading the sub-parser group carries in help output; it falls back to “subcommands” when description is supplied, and otherwise borrows the title used for positional arguments

- *description* - the blurb shown for the sub-parser group in help output, `None` by default

- *prog* - the usage text printed alongside subcommand help; it defaults to the program's name plus whatever positional arguments precede the subparser argument

- *parser_class* - the class from which sub-parser instances get built, defaulting to the class of the parser at hand (for instance `ArgumentParser`)

- action - the fundamental kind of action triggered once this argument turns up on the command line

- dest - the attribute name where the chosen subcommand name lands; it defaults to `None`, in which case nothing is recorded

- required - whether a subcommand is mandatory, defaulting to `False` (introduced in 3.7)

- help - the help text for the sub-parser group in help output, `None` by default

- metavar - the string that lists the available subcommands in help; left at `None` by default, it shows the subcommands as {cmd1, cmd2, ..}

Some example usage:

```python
>>> # create the top-level parser
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('--foo', action='store_true', help='foo help')
>>> subparsers = parser.add_subparsers(help='subcommand help')
>>>
>>> # create the parser for the "a" command
>>> parser_a = subparsers.add_parser('a', help='a help')
>>> parser_a.add_argument('bar', type=int, help='bar help')
>>>
>>> # create the parser for the "b" command
>>> parser_b = subparsers.add_parser('b', help='b help')
>>> parser_b.add_argument('--baz', choices=('X', 'Y', 'Z'), help='baz help')
>>>
>>> # parse some argument lists
>>> parser.parse_args(['a', '12'])
Namespace(bar=12, foo=False)
>>> parser.parse_args(['--foo', 'b', '--baz', 'Z'])
Namespace(baz='Z', foo=True)

```

Be aware that whatever `parse_args()` returns carries attributes only for the main parser plus the one subparser the command line picked (none of the other subparsers). Hence in the example above, naming the `a` command yields just the `foo` and `bar` attributes, while naming the `b` command yields just the `foo` and `baz` attributes.

Should a subparser register an argument whose `dest` matches the parent parser's, both end up sharing one namespace attribute, and the parent's value is lost. To keep both values, hand them separate `dest` values.

In the same vein, asking a subparser for its help message prints help for that one parser alone. No parent-parser or sibling-parser text is woven in. (You can still surface help for each subparser command by passing the `help=` argument to `add_parser()`, as shown above.)

[Subject index](INDEX.md) · [Continue](subcommands-code-example-parser-parse-args-help.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
