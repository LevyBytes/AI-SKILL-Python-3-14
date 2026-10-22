# Migrating `optparse` code to `argparse`

## Migrating optparse code to argparse

### Migrating `optparse` code to `argparse`

A number of higher-level capabilities come built into the [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) module that the [`optparse`](https://docs.python.org/3.14/library/optparse.html#module-optparse) module never offered out of the box, such as:

- Handling positional arguments.

- Supporting subcommands.

- Allowing alternative option prefixes like `+` and `/`.

- Handling zero-or-more and one-or-more style arguments.

- Producing more informative usage messages.

- Giving you a far cleaner way to define custom `type` and `action`.

At the outset, the [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) module set out to stay compatible with [`optparse`](https://docs.python.org/3.14/library/optparse.html#module-optparse). Yet a deep design gap — between handling option processing declaratively while leaving positional arguments to the application on one side, and handling both named options and positional arguments declaratively on the other — has pulled the API steadily away from that of `optparse` as the years passed.

As [Choosing an argument parsing library](https://docs.python.org/3.14/library/optparse.html#choosing-an-argument-parser) explains, any application already running on [`optparse`](https://docs.python.org/3.14/library/optparse.html#module-optparse) and content with how it behaves is free to stick with `optparse`.

Developers weighing a move ought as well to go over the inherent behavioural differences laid out in that same section before they settle on whether migrating makes sense.

For the applications that do opt to switch from [`optparse`](https://docs.python.org/3.14/library/optparse.html#module-optparse) over to [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse), the pointers below ought to come in handy:

- Swap every [`optparse.OptionParser.add_option()`](https://docs.python.org/3.14/library/optparse.html#optparse.OptionParser.add_option) call for a [`ArgumentParser.add_argument()`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser.add_argument) call.

- Change `(options, args) = parser.parse_args()` to `args = parser.parse_args()`, then bring in extra [`ArgumentParser.add_argument()`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser.add_argument) calls to cover the positional arguments. Remember that whatever used to go by `options` is, in the [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) world, now named `args`.

- Stand in for [`optparse.OptionParser.disable_interspersed_args()`](https://docs.python.org/3.14/library/optparse.html#optparse.OptionParser.disable_interspersed_args) by calling [`parse_intermixed_args()`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser.parse_intermixed_args) in place of [`parse_args()`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser.parse_args).

- Trade out callback actions together with the `callback_*` keyword arguments in favour of `type` or `action` arguments.

- Hand the matching type objects to `type` keyword arguments rather than their string names (int, float, complex, and so on).

- Substitute [`Namespace`](https://docs.python.org/3.14/library/argparse.html#argparse.Namespace) for [`optparse.Values`](https://docs.python.org/3.14/library/optparse.html#optparse.Values), and let [`ArgumentError`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentError) stand in for both [`optparse.OptionError`](https://docs.python.org/3.14/library/optparse.html#optparse.OptionError) and [`optparse.OptionValueError`](https://docs.python.org/3.14/library/optparse.html#optparse.OptionValueError).

- Where strings carried implicit arguments like `%default` or `%prog`, move to Python's ordinary dictionary-based string formatting instead — namely `%(default)s` and `%(prog)s`.

- In place of the OptionParser constructor's `version` argument, issue a `parser.add_argument('--version', action='version', version='<the version>')` call.

[Subject index](INDEX.md) · [Previous source context](../annotations-best-practices/annotations-quirks.md)
