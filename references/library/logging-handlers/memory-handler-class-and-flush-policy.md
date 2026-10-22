# logging.handlers / MemoryHandler: `logging.handlers.MemoryHandler`, `close()`, `flush()`, `setTarget()`, `shouldFlush()`

*class *logging.handlers.MemoryHandler(*capacity*, *flushLevel=ERROR*, *target=None*, *flushOnClose=True*)

Hands back a fresh instance of the `MemoryHandler` class. Its setup uses a buffer sized at *capacity* (the count of records buffered). Leave *flushLevel* unspecified and `ERROR` stands in. With no *target* given, you will have to assign one through `setTarget()` before the handler accomplishes anything worthwhile. Give *flushOnClose* as `False` and the buffer is *not* flushed when the handler closes; omit it or give `True` and the earlier behaviour — flushing the buffer at handler close — applies.

Changed in version 3.6: The *flushOnClose* parameter was added.

 close()

Calls `flush()`, points the target at `None`, and empties the buffer.

 flush()

On a `MemoryHandler` instance, a flush simply ships the buffered records off to the target, when one exists. Sending those buffered records to the target empties the buffer as well. Override it if you want behavior of your own.

 setTarget(*target*)

Assigns the target handler that this handler feeds.

 shouldFlush(*record*)

Tests for a full buffer or for a record at the *flushLevel* or above.

[Subject index](INDEX.md) · [Previous](buffering-handler-emission-and-flush.md) · [Continue](logging-handlers-httphandler-class.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md) · [Owning module, declaration or section: MemoryHandler](logging-handlers-bufferinghandler-class.md)
