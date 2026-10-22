# queue — SimpleQueue Objects

### SimpleQueue Objects

`SimpleQueue` objects expose the public methods laid out below.

 SimpleQueue.qsize()

Hand back the queue's approximate size. Mind that qsize() > 0 is no promise that a later get() won't block.

 SimpleQueue.empty()

Hand back `True` should the queue be empty, `False` otherwise. Should empty() hand back `False` it's no promise that a later call to get() won't block.

 SimpleQueue.put(*item*, *block=True*, *timeout=None*)

Put *item* into the queue. The method never blocks and invariably succeeds (barring potential low-level errors such as failing to allocate memory). The optional args *block* and *timeout* get disregarded and exist only for compatibility with `Queue.put()`.

**CPython implementation detail:** This method carries a reentrant C implementation. Put another way, one `put()` or `get()` call may be cut off mid-flight by a second `put()` running on that same thread, with no deadlock and no corruption of the queue's internal state. That makes it fit for use within destructors such as `__del__` methods or [`weakref`](https://docs.python.org/3.14/library/weakref.html#module-weakref) callbacks.

 SimpleQueue.put_nowait(*item*)

Equivalent to `put(item, block=False)`, provided for compatibility with `Queue.put_nowait()`.

 SimpleQueue.get(*block=True*, *timeout=None*)

Remove and hand back an item from the queue. Should optional args *block* be true and *timeout* be `None` (the default), block as needed until an item opens up. Should *timeout* be a positive number, it blocks for at most *timeout* seconds and raises the `Empty` exception if no item opened up within that span. Otherwise (*block* is false), hand back an item if one is at once available, else raise the `Empty` exception (*timeout* is then disregarded).

 SimpleQueue.get_nowait()

Equivalent to `get(False)`.

See also

Class [`multiprocessing.Queue`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Queue)

A queue class meant for use within a multi-processing (rather than multi-threading) context.

[`collections.deque`](https://docs.python.org/3.14/library/collections.html#collections.deque) is an alternative implementation of unbounded queues offering fast atomic [`append()`](https://docs.python.org/3.14/library/collections.html#collections.deque.append) and [`popleft()`](https://docs.python.org/3.14/library/collections.html#collections.deque.popleft) operations that need no locking and support indexing as well.

[Subject index](INDEX.md) · [Previous](queue-shutdown.md) · [Owning module, declaration or section: queue](queue-queue-class.md)
