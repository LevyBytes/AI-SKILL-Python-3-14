# argparse — const

### const

The `const` argument to `add_argument()` holds constant values that the command line does not supply but that the assorted `ArgumentParser` actions still need. Its two most frequent applications are:

- Whenever `add_argument()` runs with `action='store_const'` or `action='append_const'`. Those actions push the `const` value into one of the attributes on the object that `parse_args()` returns. The action description has examples. When you do not pass `const` to `add_argument()`, it takes on a default of `None`.

- Whenever `add_argument()` runs with option strings (for example `-f` or `--foo`) together with `nargs='?'`. This sets up an optional argument that may be trailed by zero or one command-line arguments. While the command line is being parsed, if the option string turns up with nothing following it, the `const` value steps in. The nargs description has examples.

Changed in version 3.11: `const=None` by default, including when `action='append_const'` or `action='store_const'`.

[Subject index](INDEX.md) · [Previous](nargs.md) · [Continue](default.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
