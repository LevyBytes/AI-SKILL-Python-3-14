# traceback: `traceback.format_exception()`, `traceback.format_exc()`, `traceback.format_tb()`, `traceback.format_stack()`, `traceback.clear_frames()`, `traceback.walk_stack()`, `traceback.walk_tb()`

traceback.format_exception(*exc*, */*, [*value*, *tb*, ]*limit=None*, *chain=True*)

Format both a stack trace and the exception information. Its arguments mean the same as the matching arguments of `print_exception()`. The return value is a list of strings, each closing with a newline and some carrying newlines inside them. Join those lines and print them, and you get precisely the same text that `print_exception()` produces.

Changed in version 3.5: The *etype* argument is disregarded; its value is instead deduced from the type of *value*.

Changed in version 3.10: Both the signature and the behaviour of this function were reworked to line up with `print_exception()`.

 traceback.format_exc(*limit=None*, *chain=True*)

This works like `print_exc(limit)` except that it hands back a string rather than writing to a file.

 traceback.format_tb(*tb*, *limit=None*)

A shorthand for `format_list(extract_tb(tb, limit))`.

 traceback.format_stack(*f=None*, *limit=None*)

A shorthand for `format_list(extract_stack(f, limit))`.

 traceback.clear_frames(*tb*)

Wipe the local variables held by each stack frame in a [traceback](https://docs.python.org/3.14/reference/datamodel.html#traceback-objects) *tb*, invoking the [`clear()`](https://docs.python.org/3.14/reference/datamodel.html#frame.clear) method on every [frame object](https://docs.python.org/3.14/reference/datamodel.html#frame-objects).

Added in version 3.4.

 traceback.walk_stack(*f*)

Traverse a stack by following [`f.f_back`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_back) out from the supplied frame, producing the frame along with its line number at each step. When *f* is `None`, the traversal starts from the current stack. `StackSummary.extract()` makes use of this helper.

Added in version 3.5.

Changed in version 3.14: Formerly this function gave back a generator that only traversed the stack once you began iterating it. The generator handed back today captures the stack exactly as it stood at the moment `walk_stack` was invoked.

 traceback.walk_tb(*tb*)

Traverse a traceback by following [`tb_next`](https://docs.python.org/3.14/reference/datamodel.html#traceback.tb_next), producing the frame along with its line number at each step. `StackSummary.extract()` makes use of this helper.

Added in version 3.5.

[Subject index](INDEX.md) · [Previous](traceback-print-tb-to-traceback-format-exception-only.md) · [Continue](traceback-tracebackexception-class.md) · [Owning module, declaration or section: traceback](traceback-print-or-retrieve-a-stack-traceback.md) · [Owning module, declaration or section: Module-Level Functions](traceback-print-tb-to-traceback-format-exception-only.md)
