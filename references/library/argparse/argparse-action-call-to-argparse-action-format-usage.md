# argparse.Action: `__call__()`, `format_usage()`

__call__(*parser*, *namespace*, *values*, *option_string=None*)

Because `Action` instances need to be callable, every subclass has to override `__call__()`, and that method takes four parameters:

- *parser* - The `ArgumentParser` object which contains this action.

- *namespace* - The `Namespace` object handed back from `parse_args()`. By way of [`setattr()`](https://docs.python.org/3.14/library/functions.html#setattr), most actions tack an attribute onto it.

- *values* - The matching command-line arguments after any type conversion has run. You declare such conversions via the type keyword argument of `add_argument()`.

- *option_string* - Whichever option string triggered this action. Being optional, the `option_string` argument goes missing when a positional argument is what the action attaches to.

Although `__call__()` is free to do whatever it likes, it usually assigns attributes on the `namespace` derived from `dest` and `values`.

 format_usage()

A `format_usage()` method may be defined on `Action` subclasses; it accepts no argument and yields the string emitted when the program's usage is printed. When no such method exists, a reasonable default takes over.

[Subject index](INDEX.md) · [Previous](argparse-action-class.md) · [Continue](argparse-booleanoptionalaction-class.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md) · [Owning module, declaration or section: argparse.Action](argparse-action-class.md) · [Owning module, declaration or section: Action classes](argparse-action-class.md)
