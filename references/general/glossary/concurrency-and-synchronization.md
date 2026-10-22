# Concurrency and synchronization

Open when checking Python definitions for concurrency and synchronization.

## concurrency

A computer program's capacity to carry out several tasks during the same span of time. Python ships libraries for authoring programs that draw on various styles of concurrency. [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) is a library aimed at handling asynchronous tasks and coroutines. [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) exposes operating system threads, while [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) exposes operating system processes. Processors with multiple cores can run threads and processes simultaneously on separate CPU cores (see parallelism).

## parallelism

Carrying out several operations simultaneously (for instance across multiple CPU cores). Within Python builds that include the global interpreter lock (GIL), just one thread executes Python bytecode at a time, so exploiting multiple CPU cores generally calls for multiple processes (such as [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing)) or native extensions that release the GIL. Under free-threaded Python, several Python threads can execute Python code at once across different cores.

## non-deterministic

Behavior in which a program's result can differ from run to run despite identical inputs. Within multi-threaded programs, non-deterministic behavior frequently stems from race conditions in which the relative timing or interleaving of threads shapes the result. Sound synchronization built on locks and other synchronization primitives helps secure deterministic behavior.

## concurrent modification

The case in which several threads alter shared data during the same span of time. When concurrent modification lacks proper synchronization, it can produce race conditions and may further set off a data race, data corruption, or both.

## atomic operation

An operation that seems to run as one indivisible step: no second thread can catch it partway through, and the whole of its effect lands at once. High-level statements are not guaranteed atomic by Python (`x += 1`, for instance, carries out several bytecode operations and is not atomic). Atomicity holds only in the cases where it is documented explicitly. Refer as well to race condition and data race.

## synchronization primitive

A fundamental building block used to coordinate (synchronize) how multiple threads run so as to keep access to shared resources thread-safe. Python's [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module furnishes a number of synchronization primitives, among them [`Lock`](https://docs.python.org/3.14/library/threading.html#threading.Lock), [`RLock`](https://docs.python.org/3.14/library/threading.html#threading.RLock), [`Semaphore`](https://docs.python.org/3.14/library/threading.html#threading.Semaphore), [`Condition`](https://docs.python.org/3.14/library/threading.html#threading.Condition), [`Event`](https://docs.python.org/3.14/library/threading.html#threading.Event), and [`Barrier`](https://docs.python.org/3.14/library/threading.html#threading.Barrier). On top of that, the [`queue`](https://docs.python.org/3.14/library/queue.html#module-queue) module supplies multi-producer, multi-consumer queues that prove particularly handy in multithreaded programs. These primitives aid in heading off race conditions and in coordinating how threads run. See also lock.

## lock

A synchronization primitive permitting just one thread at any given moment to reach a shared resource. Before touching the protected resource a thread has to acquire a lock, then release it once finished. Should a thread try to acquire a lock another thread already holds, it blocks until that lock frees up. The [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module in Python ships [`Lock`](https://docs.python.org/3.14/library/threading.html#threading.Lock) (a basic lock) along with [`RLock`](https://docs.python.org/3.14/library/threading.html#threading.RLock) (a reentrant lock). Locks serve to head off race conditions and to guarantee thread-safe access to shared data. Beyond locks, other design patterns can be used as well: among them are thread-local state, producer/consumer patterns, and queues. See also deadlock, and reentrant.

## per-object lock

A lock tied to one individual object instance rather than a single global lock shared by all objects. Within free-threaded Python, built-in types such as [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) and [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) rely on per-object locks so that operations on distinct objects can run concurrently while operations on the same object are serialized. Operations holding the per-object lock keep other locking operations on that same object from advancing, yet they leave lock-free operations unblocked.

## lock-free

An operation that takes no lock and instead leans on atomic CPU instructions for correctness. Such lock-free operations may run concurrently without ever blocking one another, and no lock-holding operation can block them. Within free-threaded Python, built-in types such as [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) and [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) offer lock-free read operations, so other threads might witness intermediate states while a multi-step modification is underway, even though that modification holds the per-object lock.

## thread-safe

A module, function, or class that stays correct even while several threads make use of it at once. Code that is thread-safe either guards shared mutable state with suitable synchronization primitives such as locks, or is laid out to sidestep shared mutable state altogether. Within the free-threaded build, built-in types such as [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict), [`list`](https://docs.python.org/3.14/library/stdtypes.html#list), and [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) lean on internal locking to render many operations thread-safe, though that does not amount to a guarantee of thread safety. Code lacking thread safety can run into race conditions and data races once it is put to use across multi-threaded programs.

## race condition

A program condition whose behavior hinges on the relative timing or ordering of events, especially within multi-threaded programs. Race conditions can produce non-deterministic behavior plus bugs that prove hard to reproduce. A data race is one particular kind of race condition that involves unsynchronized access to shared memory. In multi-threaded code the LBYL coding style is especially prone to race conditions. Employing locks and other synchronization primitives helps stave off race conditions.

## data race

A scenario in which several threads reach the same memory location during the same span of time, with at least one of those accesses being a write, and the threads applying no synchronization to govern their access. Data races yield non-deterministic behavior and can bring about data corruption. Sound use of locks and other synchronization primitives keeps data races from happening. Bear in mind that data races can occur only within native code, although that native code may be surfaced through a Python API. Refer as well to race condition and thread-safe.

## deadlock

A scenario in which two or more tasks (threads, processes, or coroutines) hold out endlessly for one another to free resources or finish actions, so that none can advance. As an example, when thread A holds lock 1 and waits on lock 2 while thread B holds lock 2 and waits on lock 1, neither thread will ever stop waiting. Within Python this frequently stems from taking several locks in clashing orders or from circular join/await dependencies. You can steer clear of deadlocks by consistently taking several locks in one fixed order. Refer as well to lock and reentrant.

## reentrant

A trait of a function or lock that lets the same thread call or acquire it more than once without provoking errors or a deadlock.

In the case of functions, reentrancy means a function can be called again safely before an earlier invocation has finished, which matters when functions may be invoked recursively or out of signal handlers. Thread-unsafe functions may behave non-deterministically when called reentrantly inside a multithreaded program.
Where locks are concerned, Python's [`threading.RLock`](https://docs.python.org/3.14/library/threading.html#threading.RLock) (reentrant lock) is reentrant: a thread that already owns the lock may take it once more and not block. [`threading.Lock`](https://docs.python.org/3.14/library/threading.html#threading.Lock), by contrast, is not reentrant - trying to acquire it a second time from one thread leads to a deadlock.

See also lock and deadlock.

[Glossary context index](INDEX.md).
