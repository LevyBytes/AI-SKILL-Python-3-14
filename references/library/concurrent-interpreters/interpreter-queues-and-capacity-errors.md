# concurrent.interpreters — Communicating Between Interpreters

### Communicating Between Interpreters

`class concurrent.interpreters.Queue(*id*)`

A thin layer over a low-level cross-interpreter queue that fulfills the [`queue.Queue`](https://docs.python.org/3.14/library/queue.html#queue.Queue) interface. The queue beneath it comes into being solely through `create_queue()`.

A few objects are shared outright and a few are copied cheaply, while most pass through [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle). Refer to “Sharing” Objects.

`id`

(read-only)

The ID belonging to the queue.

`exception concurrent.interpreters.QueueEmptyError`

A subclass of [`queue.Empty`](https://docs.python.org/3.14/library/queue.html#queue.Empty), thrown out of `Queue.get()` and `Queue.get_nowait()` while the queue holds nothing.

`exception concurrent.interpreters.QueueFullError`

A subclass of [`queue.Full`](https://docs.python.org/3.14/library/queue.html#queue.Full), thrown out of `Queue.put()` and `Queue.put_nowait()` once the queue has filled up.

[Subject index](INDEX.md) · [Previous](interpreter-sharing-exceptions.md) · [Continue](basic-usage.md) · [Owning module, declaration or section: concurrent.interpreters](multiple-interpreters-overview.md)
