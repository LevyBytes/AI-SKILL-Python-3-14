# logging.handlers: `logging.handlers.BufferingHandler`

### MemoryHandler

Living in the `logging.handlers` module, the `MemoryHandler` class lets you buffer logging records in memory and flush them now and then to a *target* handler. A flush is triggered once the buffer fills, or once an event of some chosen severity or higher comes along.

`MemoryHandler` derives from the broader, abstract `BufferingHandler`. That parent buffers logging records in memory; as each record joins the buffer, it calls `shouldFlush()` to judge whether the buffer ought to be flushed, and if so, `flush()` is meant to carry the flush out.

 *class *logging.handlers.BufferingHandler(*capacity*)

Sets the handler up with a buffer of the given capacity. Here *capacity* denotes how many logging records get buffered.

[Subject index](INDEX.md) · [Previous](smtp-handler-emission-and-subject.md) · [Continue](buffering-handler-emission-and-flush.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md)
