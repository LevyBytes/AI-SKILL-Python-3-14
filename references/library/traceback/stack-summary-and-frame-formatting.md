# traceback / StackSummary Objects: `from_list()`, `format()`, `format_frame_summary()`

*classmethod *from_list(*a_list*)

Build a `StackSummary` object out of a supplied list of `FrameSummary` objects or an old-style list of tuples. Each tuple ought to be a 4-tuple holding *filename*, *lineno*, *name*, *line* as its elements.

 format()

Hands back a list of print-ready strings. Every string in the result lines up with one [frame](https://docs.python.org/3.14/reference/datamodel.html#frame-objects) of the stack. Each string finishes with a newline; a string may also carry newlines inside it for those items that have source text lines.

Where the same frame and line recur over a long run, only the opening few repetitions are shown, then a summary line that states precisely how many more repetitions follow.

Changed in version 3.6: Lengthy runs of repeated frames are now condensed.

 format_frame_summary(*frame_summary*)

Hands back a string for printing one of the [frames](https://docs.python.org/3.14/reference/datamodel.html#frame-objects) that make up the stack. `StackSummary.format()` calls this method for each `FrameSummary` object it is about to print. Should it return `None`, that frame is left out of the output.

Added in version 3.11.

[Subject index](INDEX.md) · [Previous](traceback-stacksummary-class.md) · [Continue](traceback-framesummary-class.md) · [Owning module, declaration or section: traceback](traceback-print-or-retrieve-a-stack-traceback.md) · [Owning module, declaration or section: traceback.StackSummary; extract](traceback-stacksummary-class.md) · [Owning module, declaration or section: `StackSummary` Objects](traceback-stacksummary-class.md)
