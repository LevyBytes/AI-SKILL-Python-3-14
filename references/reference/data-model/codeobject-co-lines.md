# codeobject.co_lines()

codeobject.co_lines()

Hands back an iterator that reports details about consecutive ranges of [bytecode](https://docs.python.org/3.14/glossary.html#term-bytecode)s. Every produced item is a `(start, end, lineno)` [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple):

- `start` (an [`int`](https://docs.python.org/3.14/library/functions.html#int)) stands for the inclusive offset marking where the [bytecode](https://docs.python.org/3.14/glossary.html#term-bytecode) range begins

- `end` (an [`int`](https://docs.python.org/3.14/library/functions.html#int)) stands for the exclusive offset marking where the [bytecode](https://docs.python.org/3.14/glossary.html#term-bytecode) range finishes

- `lineno` is an [`int`](https://docs.python.org/3.14/library/functions.html#int) giving the line number for the [bytecode](https://docs.python.org/3.14/glossary.html#term-bytecode) range, or `None` whenever the range’s bytecodes carry no line number

The produced items hold to these guarantees:

- The first range yielded will have a `start` of 0.

- The `(start, end)` ranges stay non-decreasing and run consecutively. Put another way, across any two such [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple)s, the `start` of the latter equals the `end` of the former.

- No range runs backwards: every triple satisfies `end >= start`.

- For the final [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple) produced, `end` matches the size of the [bytecode](https://docs.python.org/3.14/glossary.html#term-bytecode).

Ranges of zero width, in which `start == end`, are permitted. Such zero-width ranges stand for lines existing in the source code that the [bytecode](https://docs.python.org/3.14/glossary.html#term-bytecode) compiler has since removed.

Added in version 3.10.

See also

[**PEP 626**](https://peps.python.org/pep-0626/) - Precise line numbers for debugging and other tools.

The PEP that introduced the `co_lines()` method.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](internal-types.md) · [Owning language section](code-objects.md) · [Owning language section](codeobject-co-positions.md) · [Previous source section](codeobject-co-positions.md) · [Following source section](codeobject-replace.md)
