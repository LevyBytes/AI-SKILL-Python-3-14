# queue: `queue.Empty`, `queue.Full`, `queue.ShutDown`

*exception *queue.Empty

Exception raised whenever a non-blocking `get()` (or `get_nowait()`) runs against a `Queue` object that's empty.

 *exception *queue.Full

Exception raised whenever a non-blocking `put()` (or `put_nowait()`) runs against a `Queue` object that's full.

 *exception *queue.ShutDown

Exception raised whenever `put()` or `get()` runs against a `Queue` object that's been shut down.

Added in version 3.13.

[Subject index](INDEX.md) · [Previous](queue-simplequeue-class.md) · [Continue](queue-qsize-to-queue-join.md) · [Owning module, declaration or section: queue](queue-queue-class.md)
