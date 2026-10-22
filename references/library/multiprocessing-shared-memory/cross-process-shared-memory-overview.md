# multiprocessing.shared_memory / Shared memory for direct access across processes: `multiprocessing.managers.SharedMemoryManager`, `SharedMemory()`, `ShareableList()`

*class *multiprocessing.managers.SharedMemoryManager([*address*[, *authkey*]])

This subclasses [`multiprocessing.managers.BaseManager`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.managers.BaseManager) and serves to oversee shared memory blocks spanning multiple processes.

Invoking [`start()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.managers.BaseManager.start) on a `SharedMemoryManager` instance brings up a new process. The single job of this new process is to oversee the life cycle of every shared memory block made through it. So as to release all of the shared memory blocks that process oversees, invoke [`shutdown()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.managers.BaseManager.shutdown) on the instance. That fires a `unlink()` call against each `SharedMemory` object the process oversees and afterward halts the process itself. Because we make `SharedMemory` instances through a `SharedMemoryManager`, we no longer have to manually keep track of and fire the release of shared memory resources.

Methods on this class let you build and hand back `SharedMemory` instances as well as build a list-like object (`ShareableList`) that sits on top of shared memory.

Consult [`BaseManager`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.managers.BaseManager) for an account of the inherited optional arguments *address* and *authkey*, plus the way other processes can employ them to hook up with a `SharedMemoryManager` service that already exists.

 SharedMemory(*size*)

Create and return a new `SharedMemory` object with the specified *size* in bytes.

 ShareableList(*sequence*)

Build a fresh `ShareableList` object and hand it back, seeded with the values taken from the supplied *sequence*.

The following example demonstrates the basic mechanisms of a `SharedMemoryManager`:

```pycon
>>> from multiprocessing.managers import SharedMemoryManager
>>> smm = SharedMemoryManager()
>>> smm.start()  # Start the process that manages the shared memory blocks
>>> sl = smm.ShareableList(range(4))
>>> sl
ShareableList([0, 1, 2, 3], name='psm_6572_7512')
>>> raw_shm = smm.SharedMemory(size=128)
>>> another_sl = smm.ShareableList('alpha')
>>> another_sl
ShareableList(['a', 'l', 'p', 'h', 'a'], name='psm_6572_12221')
>>> smm.shutdown()  # Calls unlink() on sl, raw_shm, and another_sl

```

The example below illustrates a possibly handier approach to working with `SharedMemoryManager` objects by way of the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement, which makes sure every shared memory block is released after it is no longer wanted:

```pycon
>>> with SharedMemoryManager() as smm:
...     sl = smm.ShareableList(range(2000))
...     # Divide the work among two processes, storing partial results in sl
...     p1 = Process(target=do_work, args=(sl, 0, 1000))
...     p2 = Process(target=do_work, args=(sl, 1000, 2000))
...     p1.start()
...     p2.start()  # A multiprocessing.Pool might be more efficient
...     p1.join()
...     p2.join()   # Wait for all work to complete in both processes
...     total_result = sum(sl)  # Consolidate the partial results now in sl

```

Whenever a `SharedMemoryManager` is used inside a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement, every shared memory block produced by that manager gets released once the body of the `with` statement’s code block has finished running.

[Subject index](INDEX.md) · [Previous](sharedmemory-buffer-contract.md) · [Continue](shareable-list-contract.md) · [Owning module, declaration or section: multiprocessing.shared_memory](multiprocessing-shared-memory-sharedmemory-class.md)
