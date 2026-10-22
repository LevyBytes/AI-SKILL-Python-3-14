# inspect: `inspect.Traceback`

*class *inspect.Traceback

 filename

The name of the file tied to the code being run by the frame this traceback corresponds to.

 lineno

The line number of the present line tied to the code being run by the frame this traceback corresponds to.

 function

The name of the function being run by the frame this traceback corresponds to.

 code_context

A list of context lines drawn from the source code being run by the frame this traceback corresponds to.

 index

The index, within the `code_context` list, of the line currently being run.

 positions

A [`dis.Positions`](https://docs.python.org/3.14/library/dis.html#dis.Positions) object carrying the starting and ending line numbers along with the starting and ending column offsets for the instruction being run by the frame this traceback corresponds to.

Changed in version 3.11: `Traceback` is now a class instance (one that stays backwards compatible with the earlier [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple)).

Note

Holding on to references to frame objects — such as the one sitting at the first position of the frame records returned by these functions — can lead your program to build reference cycles. After a reference cycle exists, the lifespan of every object reachable from the objects that make up the cycle can stretch much longer, even when Python's optional cycle detector is turned on. Whenever such cycles have to be created, it matters that you explicitly break them so as to head off the delayed destruction of objects and the rise in memory consumption that follows.

Even though the cycle detector will pick these up, you can make destruction of the frames (and local variables) deterministic by clearing the cycle inside a [`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) clause. This matters too when the cycle detector was switched off at the time Python was compiled or via [`gc.disable()`](https://docs.python.org/3.14/library/gc.html#gc.disable). For example:

```python
def handle_stackframe_without_leak():
    frame = inspect.currentframe()
    try:
        # do something with the frame
    finally:
        del frame

```

Should you wish to retain the frame (say, to print a traceback later on), you can additionally break reference cycles through the [`frame.clear()`](https://docs.python.org/3.14/reference/datamodel.html#frame.clear) method.

Most of these functions accept an optional *context* argument that sets how many lines of context to return, centered on the current line.

[Subject index](INDEX.md) · [Previous](the-interpreter-stack.md) · [Continue](inspect-getframeinfo-to-inspect-getouterframes.md) · [Owning module, declaration or section: inspect](inspect-inspect-live-objects.md) · [Owning module, declaration or section: The interpreter stack](inspect-frameinfo-class.md)
