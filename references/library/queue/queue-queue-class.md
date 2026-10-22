# queue: `queue.Queue`

## queue — A synchronized queue class??

### `queue` — A synchronized queue class

**Source code:** [Lib/queue.py](https://github.com/python/cpython/tree/3.14/Lib/queue.py)

---

The `queue` module brings multi-producer, multi-consumer queues to life. It shines particularly in threaded programming whenever data has to pass safely among several threads. Within this module the `Queue` class carries out every bit of the locking semantics that's needed.

Three kinds of queue are carried out by the module, parting ways solely over the order entries come back in. Within a FIFO queue, the earliest tasks added are the earliest to come back. Within a LIFO queue, the most recently added entry comes back first (behaving like a stack). On a priority queue, the entries stay sorted (by way of the [`heapq`](https://docs.python.org/3.14/library/heapq.html#module-heapq) module) and the lowest valued entry comes back ahead of the rest.

Under the hood, all three queue kinds lean on locks to briefly hold off rival threads; they are not, however, built to cope with reentrancy inside a single thread.

On top of that, the module carries out a "simple" FIFO queue kind, `SimpleQueue`, whose particular implementation trades the trimmed-down functionality for extra guarantees.

The `queue` module lays out the following classes and exceptions:

 *class *queue.Queue(*maxsize=0*)

Constructor for a FIFO queue. *maxsize* is an integer setting the upperbound limit on how many items may sit in the queue. Insertion blocks once that size has been hit, until queue items get consumed. Should *maxsize* be less than or equal to zero, the queue size runs infinite.

[Subject index](INDEX.md) · [Continue](queue-lifoqueue-class.md)
