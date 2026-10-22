# multiprocessing / Pipes and Queues: `multiprocessing.JoinableQueue`, `task_done()`, `join()`

*class *multiprocessing.JoinableQueue([*maxsize*])

`JoinableQueue`, a subclass of `Queue`, is a queue that adds `task_done()` and `join()` methods on top.

Building an object of this kind can fix the global start method in place. Consult Global start method for the fuller picture.

 task_done()

Signal that a task pulled from the queue earlier is now finished. Queue consumers use this. After every `get()` that fetches a task, a following call to `task_done()` informs the queue that processing of that task is done.

Whenever a [`join()`](https://docs.python.org/3.14/library/queue.html#queue.Queue.join) is blocking at the moment, it resumes once every item has been processed (that is, a `task_done()` call arrived for each item that had been `put()` onto the queue).

Raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) should the number of calls exceed how many items were enqueued.

 join()

Block until every item on the queue has been retrieved and processed.

Each time an item joins the queue, the tally of unfinished tasks rises. Each time a consumer calls `task_done()` to report that the item was fetched and fully handled, the tally falls. As soon as the unfinished-task tally reaches zero, [`join()`](https://docs.python.org/3.14/library/queue.html#queue.Queue.join) stops blocking.

[Subject index](INDEX.md) · [Previous](simple-process-queue.md) · [Continue](active-children-and-start-method-discovery.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md) · [Owning module, declaration or section: Pipes and Queues](multiprocessing-pipe.md)
