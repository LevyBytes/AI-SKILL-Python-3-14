# multiprocessing / Managers: `multiprocessing.managers.SyncManager`, `Barrier()`, `BoundedSemaphore()`, `Condition()`, `Event()`, `Lock()`, `Namespace()`, `Queue()`, `RLock()`, `Semaphore()`, `Array()`, `Value()`, `dict()`, `list()`, `set()`

*class *multiprocessing.managers.SyncManager

A subclass of `BaseManager` usable for keeping processes in sync. `multiprocessing.Manager()` hands back objects of this type.

Its methods build and hand back Proxy Objects for a range of commonly used data types so they can be synchronized across processes. That range notably covers shared lists and dictionaries.

 Barrier(*parties*[, *action*[, *timeout*]])

Build a shared [`threading.Barrier`](https://docs.python.org/3.14/library/threading.html#threading.Barrier) object and hand back a proxy to it.

Added in version 3.3.

 BoundedSemaphore([*value*])

Build a shared [`threading.BoundedSemaphore`](https://docs.python.org/3.14/library/threading.html#threading.BoundedSemaphore) object and hand back a proxy to it.

 Condition([*lock*])

Build a shared [`threading.Condition`](https://docs.python.org/3.14/library/threading.html#threading.Condition) object and hand back a proxy to it.

Should *lock* be given, it ought to be a proxy for a [`threading.Lock`](https://docs.python.org/3.14/library/threading.html#threading.Lock) or [`threading.RLock`](https://docs.python.org/3.14/library/threading.html#threading.RLock) object.

Changed in version 3.3: The [`wait_for()`](https://docs.python.org/3.14/library/threading.html#threading.Condition.wait_for) method was added.

 Event()

Build a shared [`threading.Event`](https://docs.python.org/3.14/library/threading.html#threading.Event) object and hand back a proxy to it.

 Lock()

Build a shared [`threading.Lock`](https://docs.python.org/3.14/library/threading.html#threading.Lock) object and hand back a proxy to it.

 Namespace()

Build a shared `Namespace` object and hand back a proxy to it.

 Queue([*maxsize*])

Build a shared [`queue.Queue`](https://docs.python.org/3.14/library/queue.html#queue.Queue) object and hand back a proxy to it.

 RLock()

Build a shared [`threading.RLock`](https://docs.python.org/3.14/library/threading.html#threading.RLock) object and hand back a proxy to it.

 Semaphore([*value*])

Build a shared [`threading.Semaphore`](https://docs.python.org/3.14/library/threading.html#threading.Semaphore) object and hand back a proxy to it.

 Array(*typecode*, *sequence*)

Build an array and hand back a proxy to it.

 Value(*typecode*, *value*)

Build an object carrying a writable `value` attribute and hand back a proxy to it.

 dict()

 dict(*mapping*)

 dict(*sequence*)

Build a shared [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) object and hand back a proxy to it.

 list()

 list(*sequence*)

Build a shared [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) object and hand back a proxy to it.

 set()

 set(*sequence*)

 set(*mapping*)

Build a shared [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) object and hand back a proxy to it.

Added in version 3.14: [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) support was added.

Changed in version 3.6: Nesting of shared objects became possible. As an example, a shared container like a shared list may hold further shared objects, each of which the `SyncManager` manages and keeps in sync.

[Subject index](INDEX.md) · [Previous](manager-start-and-type-registration.md) · [Continue](multiprocessing-managers-namespace-class.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md) · [Owning module, declaration or section: Managers](multiprocessing-manager.md)
