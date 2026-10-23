# argparse - ArgumentParser objects

### ArgumentParser objects

```text
class argparse.ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=argparse.HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True, allow_abbrev=True, exit_on_error=True, *, suggest_on_error=False, color=True)
```

Build a fresh `ArgumentParser` object. Every parameter must be supplied as a keyword argument. A fuller account of each one follows further down, but here is the quick version:

- prog - The program's name (default: built out of the `__main__` module attributes together with `sys.argv[0]`)

- usage - The string that spells out program usage (default: built from whichever arguments were added to the parser)

- description - Text to display before the argument help (by default, no text)

- epilog - Text to display after the argument help (by default, no text)

- parents - A list of `ArgumentParser` objects whose arguments should also be included

- formatter_class - A class for customizing the help output

- prefix_chars - The set of characters that prefix optional arguments (default: "-")

- fromfile_prefix_chars - The character set marking files whose contents supply further arguments to be read in (default: `None`)

- argument_default - The global default value for arguments (default: `None`)

- conflict_handler - The strategy for resolving conflicting optionals (usually unnecessary)

- add_help - Add a `-h/--help` option to the parser (default: `True`)

- allow_abbrev - Allows long options to be abbreviated if the abbreviation is unambiguous (default: `True`)

- exit_on_error - Determines whether or not `ArgumentParser` exits with error info when an error occurs. (default: `True`)

- suggest_on_error - Enables suggestions for mistyped argument choices and subparser names (default: `False`)

- color - Allow color output (default: `True`)

Changed in version 3.5: *allow_abbrev* parameter was added.

Changed in version 3.8: Earlier, turning off *allow_abbrev* would additionally stop short flags from being bundled, so `-vv` no longer expanded to `-v -v`.

Changed in version 3.9: *exit_on_error* parameter was added.

Changed in version 3.14: *suggest_on_error* and *color* parameters were added.

How every one of these is applied is covered in the sections that follow.

[Subject index](INDEX.md) · [Previous](argument-parser-overview.md) · [Continue](prog.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
