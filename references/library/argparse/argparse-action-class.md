# argparse: `argparse.Action`

### Action classes

The Action API is realized by `Action` classes: a callable that returns a callable to handle command-line arguments. You can hand any object conforming to this API as the `action` parameter of `add_argument()`.

 *class *argparse.Action(*option_strings*, *dest*, *nargs=None*, *const=None*, *default=None*, *type=None*, *choices=None*, *required=False*, *help=None*, *metavar=None*)

An `ArgumentParser` relies on `Action` objects to capture everything required for parsing a single argument out of one or more command-line strings. The `Action` class has to accept those two positional arguments together with whatever keyword arguments `ArgumentParser.add_argument()` forwards, the lone exception being the `action` itself.

An `Action` instance (or whatever a callable supplied to the `action` parameter returns) ought to expose attributes such as `dest`, `option_strings`, `default`, `type`, `required`, `help`, and so on. Invoking `Action.__init__()` is the simplest route to guaranteeing those attributes exist.

[Subject index](INDEX.md) · [Previous](deprecated.md) · [Continue](argparse-action-call-to-argparse-action-format-usage.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
