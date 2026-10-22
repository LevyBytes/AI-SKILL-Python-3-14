# logging.handlers.BufferingHandler: `emit()`, `flush()`, `shouldFlush()`

emit(*record*)

Tack the record onto the buffer. Should `shouldFlush()` come back true, call `flush()` to deal with the buffer.

 flush()

On a `BufferingHandler` instance, a flush amounts to resetting the buffer to an empty list. You can overwrite this method to put more useful flushing behavior in place.

 shouldFlush(*record*)

Hands back `True` once the buffer has reached capacity. Override this method to put custom flushing strategies in place.

[Subject index](INDEX.md) · [Previous](logging-handlers-bufferinghandler-class.md) · [Continue](memory-handler-class-and-flush-policy.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md) · [Owning module, declaration or section: logging.handlers.BufferingHandler](logging-handlers-bufferinghandler-class.md) · [Owning module, declaration or section: MemoryHandler](logging-handlers-bufferinghandler-class.md)
