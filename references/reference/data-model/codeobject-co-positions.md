# codeobject.co_positions()

##### 3.2.13.1.2. Methods on code objects

 codeobject.co_positions()

Yields an iterable across the source code positions belonging to every [bytecode](https://docs.python.org/3.14/glossary.html#term-bytecode) instruction within the code object.

The iterator hands back [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple)s holding the `(start_line, end_line, start_column, end_column)`. The *i-th* tuple maps to the location of the source code that was compiled into the *i-th* code unit. Column data uses 0-indexed utf-8 byte offsets measured on the relevant source line.

There are situations in which this positional information is absent. The following is a non-exhaustive list of cases where that can occur:

- Running the interpreter with [`-X`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) `no_debug_ranges`.

- Loading a pyc file compiled while using [`-X`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) `no_debug_ranges`.

- Position tuples corresponding to artificial instructions.

- Line and column numbers that, owing to implementation specific limitations, cannot be represented.

Should that happen, part or all of the tuple’s elements may be [`None`](https://docs.python.org/3.14/library/constants.html#None).

Added in version 3.11.

Note

Because this capability relies on keeping column positions inside code objects, it can produce a slight growth in the disk footprint of compiled Python files or in interpreter memory consumption. If you want to skip retaining that additional data and/or suppress the printing of the extra traceback information, you can apply the [`-X`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) `no_debug_ranges` command line flag or set the [`PYTHONNODEBUGRANGES`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONNODEBUGRANGES) environment variable.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](internal-types.md) · [Owning language section](code-objects.md) · [Previous source section](special-read-only-attributes.md) · [Following source section](codeobject-co-lines.md)
