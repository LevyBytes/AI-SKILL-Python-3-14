# traceback: `traceback.FrameSummary`

### `FrameSummary` Objects

Added in version 3.5.

A `FrameSummary` object represents a single [frame](https://docs.python.org/3.14/reference/datamodel.html#frame-objects) in a [traceback](https://docs.python.org/3.14/reference/datamodel.html#traceback-objects).

 *class *traceback.FrameSummary(*filename*, *lineno*, *name*, ***, *lookup_line=True*, *locals=None*, *line=None*, *end_lineno=None*, *colno=None*, *end_colno=None*)

Stands for a single [frame](https://docs.python.org/3.14/reference/datamodel.html#frame-objects) within the [traceback](https://docs.python.org/3.14/reference/datamodel.html#traceback-objects) or stack currently being formatted or printed. It can optionally carry a stringified rendering of the frame's locals. With *lookup_line* set to `False`, the source code stays unread until something accesses the `FrameSummary`'s `line` attribute (which is also what happens when it is cast to a [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple)). You may give `line` outright, and doing so suppresses any line lookups entirely. *locals* is an optional mapping of local variables; when supplied, the variable representations are kept in the summary so they can be shown later.

`FrameSummary` instances have the following attributes:

[Subject index](INDEX.md) · [Previous](stack-summary-and-frame-formatting.md) · [Continue](framesummary-objects.md) · [Owning module, declaration or section: traceback](traceback-print-or-retrieve-a-stack-traceback.md)
