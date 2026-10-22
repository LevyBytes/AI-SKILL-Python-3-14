# traceback / StackSummary Objects: `traceback.StackSummary`, `extract()`

### `StackSummary` Objects

Added in version 3.5.

`StackSummary` objects represent a call stack ready for formatting.

 *class *traceback.StackSummary

 *classmethod *extract(*frame_gen*, ***, *limit=None*, *lookup_lines=True*, *capture_locals=False*)

Build a `StackSummary` object out of a frame generator (of the kind `walk_stack()` or `walk_tb()` hands back).

Supplying *limit* caps how many frames are drawn from *frame_gen* at that number. Setting *lookup_lines* to `False` means the returned `FrameSummary` objects hold off on reading their lines, which makes building the `StackSummary` cheaper (worthwhile when there is a chance it never gets formatted). Setting *capture_locals* to `True` causes the local variables in each `FrameSummary` to be recorded as object representations.

Changed in version 3.12: When [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) raises on a local variable (with *capture_locals* set to `True`), that exception is no longer handed back up to the caller.

[Subject index](INDEX.md) · [Previous](traceback-exception-formatting.md) · [Continue](stack-summary-and-frame-formatting.md) · [Owning module, declaration or section: traceback](traceback-print-or-retrieve-a-stack-traceback.md)
