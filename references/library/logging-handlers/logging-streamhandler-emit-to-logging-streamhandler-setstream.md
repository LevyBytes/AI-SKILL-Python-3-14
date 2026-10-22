# logging.handlers / StreamHandler: `emit()`, `flush()`, `setStream()`

emit(*record*)

When a formatter has been set, it formats the record. The record is then written onto the stream followed by `terminator`. Where exception information exists, it gets formatted through [`traceback.print_exception()`](https://docs.python.org/3.14/library/traceback.html#traceback.print_exception) and appended onto the stream.

 flush()

Flushes the stream by invoking its `flush()` method. Keep in mind that the `close()` method, inherited from [`Handler`](https://docs.python.org/3.14/library/logging.html#logging.Handler), produces no output, so now and then an explicit `flush()` call may be required.

 setStream(*stream*)

Points the instance's stream at the given value, provided it differs. The previous stream gets flushed before the new one takes its place.

Parameters:

**stream** – The stream that the handler should use.

Returns:

the previous stream when a change occurred, or else `None` when no change took place.

Added in version 3.7.

 terminator

String employed as the terminator when a formatted record is written onto a stream. The default value is `'\n'`.

Should you prefer no newline termination, set the handler instance's `terminator` attribute to the empty string.

In releases prior to this, the terminator was hardcoded as `'\n'`.

Added in version 3.2.

[Subject index](INDEX.md) · [Previous](logging-streamhandler-class.md) · [Continue](logging-filehandler-class.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md) · [Owning module, declaration or section: logging.StreamHandler](logging-streamhandler-class.md) · [Owning module, declaration or section: StreamHandler](logging-streamhandler-class.md)
