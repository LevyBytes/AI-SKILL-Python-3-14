# multiprocessing: `multiprocessing.Pipe()`

### Pipes and Queues

With multiple processes in play, communication between them normally happens through message passing, which sidesteps the need for synchronization primitives such as locks.

To pass messages, you can reach for `Pipe()` (linking two processes together) or for a queue (which accommodates many producers and consumers).

The `Queue`, `SimpleQueue` and `JoinableQueue` types are multi-producer, multi-consumer FIFO queues patterned after the [`queue.Queue`](https://docs.python.org/3.14/library/queue.html#queue.Queue) class from the standard library. Where they part ways is that `Queue` omits the [`task_done()`](https://docs.python.org/3.14/library/queue.html#queue.Queue.task_done) and [`join()`](https://docs.python.org/3.14/library/queue.html#queue.Queue.join) methods that arrived in Python 2.5's `queue.Queue` class.

Choosing `JoinableQueue` means you **must** call `JoinableQueue.task_done()` for every task pulled off the queue; otherwise the semaphore tracking the count of unfinished tasks can eventually overflow and raise an exception.

A point where `multiprocessing` queues differ from other Python queue implementations: they serialize each object placed into them with [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle). What the get method hands back is a freshly reconstructed object that shares no memory with the original.

Be aware that you can also build a shared queue from a manager object — see Managers.

Note

To flag a timeout, `multiprocessing` reuses the ordinary [`queue.Empty`](https://docs.python.org/3.14/library/queue.html#queue.Empty) and [`queue.Full`](https://docs.python.org/3.14/library/queue.html#queue.Full) exceptions. Because they are absent from the `multiprocessing` namespace, you have to import them from [`queue`](https://docs.python.org/3.14/library/queue.html#module-queue).

Note

Once an object is placed on a queue, it gets pickled, and a background thread flushes the pickled bytes into an underlying pipe later on. A few somewhat surprising consequences follow from this, though none should pose any real trouble for everyday use — if they genuinely concern you, fall back on a queue made with a manager.

1.

Right after putting an object onto an empty queue, a vanishingly small delay can pass before the queue's `empty()` method returns [`False`](https://docs.python.org/3.14/library/constants.html#False) and `get_nowait()` can return without raising [`queue.Empty`](https://docs.python.org/3.14/library/queue.html#queue.Empty).

2.

When several processes enqueue objects, those objects may arrive at the far end in a different order. That said, objects enqueued by one and the same process keep their expected order relative to each other.

Warning

Should a process get killed by `Process.terminate()` or [`os.kill()`](https://docs.python.org/3.14/library/os.html#os.kill) midway through using a `Queue`, the queue's data is apt to end up corrupted. Any other process may then hit an exception the next time it tries to use the queue.

Warning

Per the earlier remark, if a child process has placed items on a queue (and has not invoked `JoinableQueue.cancel_join_thread`), that process will not finish until every buffered item has been flushed into the pipe.

Consequently, trying to join such a process can deadlock unless you are certain every item put on the queue has been consumed. By the same token, when the child process is non-daemonic the parent process can stall on exit while trying to join all of its non-daemonic children.

Be aware that a manager-backed queue avoids this problem. See Programming guidelines.

For a worked example of using queues for interprocess communication, consult Examples.

 multiprocessing.Pipe(*duplex=True*)

Gives back a pair `(conn1, conn2)` of `Connection` objects standing for the two ends of a pipe.

When *duplex* is `True` (the default), the pipe runs in both directions. When *duplex* is `False`, the pipe runs one way only: `conn1` is solely for receiving messages while `conn2` is solely for sending them.

The `send()` method serializes the object via [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle), and `recv()` reconstructs it.

[Subject index](INDEX.md) · [Previous](multiprocessing-processerror-to-multiprocessing-timeouterror.md) · [Continue](process-queue-contract-and-feeder-lifecycle.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md)
