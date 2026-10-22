# inspect: Stack-frame filename, context and position fields

filename

The name of the file tied to the code being run by the frame this record corresponds to.

 lineno

The line number of the present line tied to the code being run by the frame this record corresponds to.

 function

The name of the function being run by the frame this record corresponds to.

 code_context

A list of context lines drawn from the source code being run by the frame this record corresponds to.

 index

The index, within the `code_context` list, of the line currently being run.

 positions

A [`dis.Positions`](https://docs.python.org/3.14/library/dis.html#dis.Positions) object carrying the starting and ending line numbers along with the starting and ending column offsets for the instruction being run by the frame this record corresponds to.

Changed in version 3.5: Return a [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple) instead of a [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple).

Changed in version 3.11: `FrameInfo` is now a class instance (one that stays backwards compatible with the earlier [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple)).

[Subject index](INDEX.md) · [Previous](inspect-frameinfo-class.md) · [Continue](inspect-traceback-class.md) · [Owning module, declaration or section: inspect](inspect-inspect-live-objects.md) · [Owning module, declaration or section: inspect.FrameInfo; frame](inspect-frameinfo-class.md) · [Owning module, declaration or section: The interpreter stack](inspect-frameinfo-class.md)
