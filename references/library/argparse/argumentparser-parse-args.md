# argparse — The parse_args() method

### The parse_args() method

 ArgumentParser.parse_args(*args=None*, *namespace=None*)

Turn the argument strings into objects, attach them as attributes on the namespace, and hand back the filled-in namespace.

Whatever you previously registered through `add_argument()` dictates precisely which objects get built and where they land. Consult the `add_argument()` documentation for the specifics.

- args - The list of strings to parse, defaulting to whatever [`sys.argv`](https://docs.python.org/3.14/library/sys.html#sys.argv) holds.

- namespace - The object that receives the attributes; absent one, a fresh empty `Namespace` object is used.

[Subject index](INDEX.md) · [Previous](argparse-booleanoptionalaction-class.md) · [Continue](option-value-syntax.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
