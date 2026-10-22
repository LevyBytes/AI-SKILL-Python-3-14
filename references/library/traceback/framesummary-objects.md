# traceback: FrameSummary source location and local-variable attributes

filename

This frame's source-code filename. Reading it is the same as reaching for [`f.f_code.co_filename`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_filename) on a [frame object](https://docs.python.org/3.14/reference/datamodel.html#frame-objects) *f*.

 lineno

The line number of the source code for this frame.

 name

Equivalent to accessing [`f.f_code.co_name`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_name) on a [frame object](https://docs.python.org/3.14/reference/datamodel.html#frame-objects) *f*.

 line

A string holding the source code for this frame, with whitespace at the start and end trimmed away. When the source cannot be obtained, it is `None`.

 end_lineno

This frame's final source-code line number. It defaults to whatever `lineno` holds, with indexing that starts at 1.

Changed in version 3.13: The default value changed from `None` to `lineno`.

 colno

This frame's source-code column number. It defaults to `None`, with indexing that starts at 0.

 end_colno

This frame's final source-code column number. It defaults to `None`, with indexing that starts at 0.

[Subject index](INDEX.md) · [Previous](traceback-framesummary-class.md) · [Continue](examples-of-using-the-module-level-functions.md) · [Owning module, declaration or section: traceback](traceback-print-or-retrieve-a-stack-traceback.md) · [Owning module, declaration or section: traceback.FrameSummary](traceback-framesummary-class.md) · [Owning module, declaration or section: `FrameSummary` Objects](traceback-framesummary-class.md)
