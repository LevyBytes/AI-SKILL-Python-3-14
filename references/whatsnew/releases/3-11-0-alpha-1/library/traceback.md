# Python 3.11.0 alpha 1 / library / traceback

[bpo-44569](https://bugs.python.org/issue?@action=redirect&bpo=44569): The `StackSummary.format_frame()` function arrived in [`traceback`](https://docs.python.org/3.14/library/traceback.html#module-traceback). With it, callers can tailor how single lines render inside tracebacks while skipping any rewrite of the recursive-traceback logic.

[bpo-44446](https://bugs.python.org/issue?@action=redirect&bpo=44446): The possibility that `lineno` is `None` is now accounted for in [`traceback.FrameSummary`](https://docs.python.org/3.14/library/traceback.html#traceback.FrameSummary).

[bpo-45075](https://bugs.python.org/issue?@action=redirect&bpo=45075): Renamed `traceback.StackSummary.format_frame()` into [`traceback.StackSummary.format_frame_summary()`](https://docs.python.org/3.14/library/traceback.html#traceback.StackSummary.format_frame_summary). Since this method only arrived for 3.11, no release had shipped it yet.

Both the code and the documentation were updated to draw a sharper line between frame and FrameSummary.

[bpo-31299](https://bugs.python.org/issue?@action=redirect&bpo=31299): Adds the ability to discard frames from a traceback entirely by having a `format_frame()` override return `None`.

[bpo-43024](https://bugs.python.org/issue?@action=redirect&bpo=43024): The help signatures of [`traceback.print_exception()`](https://docs.python.org/3.14/library/traceback.html#traceback.print_exception), [`traceback.format_exception()`](https://docs.python.org/3.14/library/traceback.html#traceback.format_exception) and [`traceback.format_exception_only()`](https://docs.python.org/3.14/library/traceback.html#traceback.format_exception_only) have been refined.

[bpo-33809](https://bugs.python.org/issue?@action=redirect&bpo=33809): A new [`traceback.TracebackException.print()`](https://docs.python.org/3.14/library/traceback.html#traceback.TracebackException.print) method is available; it emits the formatted exception details.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
