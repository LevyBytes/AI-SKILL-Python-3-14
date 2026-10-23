# Concurrent Execution - Section introduction and initial examples

# Concurrency

### Concurrent Execution

The modules covered in this chapter help you run code concurrently. Which tool fits best hinges on the nature of the work (CPU bound versus IO bound) and on the development style you favour (event driven cooperative multitasking versus preemptive multitasking). The list below gives an overview:

- [`threading` - Thread-based parallelism](https://docs.python.org/3.14/library/threading.html)
  - [Introduction](https://docs.python.org/3.14/library/threading.html#introduction)
  - [GIL and performance considerations](https://docs.python.org/3.14/library/threading.html#gil-and-performance-considerations)
  - [Reference](https://docs.python.org/3.14/library/threading.html#reference)
    - [Thread-local data](https://docs.python.org/3.14/library/threading.html#thread-local-data)
    - [Thread objects](https://docs.python.org/3.14/library/threading.html#thread-objects)
    - [Lock objects](https://docs.python.org/3.14/library/threading.html#lock-objects)
    - [RLock objects](https://docs.python.org/3.14/library/threading.html#rlock-objects)
    - [Condition objects](https://docs.python.org/3.14/library/threading.html#condition-objects)
    - [Semaphore objects](https://docs.python.org/3.14/library/threading.html#semaphore-objects)
    - [`Semaphore` example](https://docs.python.org/3.14/library/threading.html#semaphore-example)
    - [Event objects](https://docs.python.org/3.14/library/threading.html#event-objects)
    - [Timer objects](https://docs.python.org/3.14/library/threading.html#timer-objects)
    - [Barrier objects](https://docs.python.org/3.14/library/threading.html#barrier-objects)

  - [Using locks, conditions, and semaphores in the `with` statement](https://docs.python.org/3.14/library/threading.html#using-locks-conditions-and-semaphores-in-the-with-statement)

- [`multiprocessing` - Process-based parallelism](https://docs.python.org/3.14/library/multiprocessing.html)
  - [Introduction](https://docs.python.org/3.14/library/multiprocessing.html#introduction)
    - [The `Process` class](https://docs.python.org/3.14/library/multiprocessing.html#the-process-class)
    - [Contexts and start methods](https://docs.python.org/3.14/library/multiprocessing.html#contexts-and-start-methods)
    - [Exchanging objects between processes](https://docs.python.org/3.14/library/multiprocessing.html#exchanging-objects-between-processes)
    - [Synchronization between processes](https://docs.python.org/3.14/library/multiprocessing.html#synchronization-between-processes)
    - [Sharing state between processes](https://docs.python.org/3.14/library/multiprocessing.html#sharing-state-between-processes)
    - [Using a pool of workers](https://docs.python.org/3.14/library/multiprocessing.html#using-a-pool-of-workers)

  - [Reference](https://docs.python.org/3.14/library/multiprocessing.html#reference)
    - [Global start method](https://docs.python.org/3.14/library/multiprocessing.html#global-start-method)
    - [`Process` and exceptions](https://docs.python.org/3.14/library/multiprocessing.html#process-and-exceptions)
    - [Pipes and Queues](https://docs.python.org/3.14/library/multiprocessing.html#pipes-and-queues)
    - [Miscellaneous](https://docs.python.org/3.14/library/multiprocessing.html#miscellaneous)
    - [Connection Objects](https://docs.python.org/3.14/library/multiprocessing.html#connection-objects)
    - [Synchronization primitives](https://docs.python.org/3.14/library/multiprocessing.html#synchronization-primitives)
    - [Shared `ctypes` Objects](https://docs.python.org/3.14/library/multiprocessing.html#shared-ctypes-objects)
      - [The `multiprocessing.sharedctypes` module](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing.sharedctypes)

    - [Managers](https://docs.python.org/3.14/library/multiprocessing.html#managers)
      - [Customized managers](https://docs.python.org/3.14/library/multiprocessing.html#customized-managers)
      - [Using a remote manager](https://docs.python.org/3.14/library/multiprocessing.html#using-a-remote-manager)

    - [Proxy Objects](https://docs.python.org/3.14/library/multiprocessing.html#proxy-objects)
      - [Cleanup](https://docs.python.org/3.14/library/multiprocessing.html#cleanup)

    - [Process Pools](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing.pool)
    - [Listeners and Clients](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing.connection)
      - [Address Formats](https://docs.python.org/3.14/library/multiprocessing.html#address-formats)

    - [Authentication keys](https://docs.python.org/3.14/library/multiprocessing.html#authentication-keys)
    - [Logging](https://docs.python.org/3.14/library/multiprocessing.html#logging)
    - [The `multiprocessing.dummy` module](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing.dummy)

  - [Programming guidelines](https://docs.python.org/3.14/library/multiprocessing.html#programming-guidelines)
    - [All start methods](https://docs.python.org/3.14/library/multiprocessing.html#all-start-methods)
    - [The *spawn* and *forkserver* start methods](https://docs.python.org/3.14/library/multiprocessing.html#the-spawn-and-forkserver-start-methods)

  - [Examples](https://docs.python.org/3.14/library/multiprocessing.html#examples)

- [`multiprocessing.shared_memory` - Shared memory for direct access across processes](https://docs.python.org/3.14/library/multiprocessing.shared_memory.html)
- [The `concurrent` package](https://docs.python.org/3.14/library/concurrent.html)
- [`concurrent.futures` - Launching parallel tasks](https://docs.python.org/3.14/library/concurrent.futures.html)
  - [Executor Objects](https://docs.python.org/3.14/library/concurrent.futures.html#executor-objects)
  - [ThreadPoolExecutor](https://docs.python.org/3.14/library/concurrent.futures.html#threadpoolexecutor)
    - [ThreadPoolExecutor Example](https://docs.python.org/3.14/library/concurrent.futures.html#threadpoolexecutor-example)

  - [InterpreterPoolExecutor](https://docs.python.org/3.14/library/concurrent.futures.html#interpreterpoolexecutor)
  - [ProcessPoolExecutor](https://docs.python.org/3.14/library/concurrent.futures.html#processpoolexecutor)
    - [ProcessPoolExecutor Example](https://docs.python.org/3.14/library/concurrent.futures.html#processpoolexecutor-example)

  - [Future Objects](https://docs.python.org/3.14/library/concurrent.futures.html#future-objects)
  - [Module Functions](https://docs.python.org/3.14/library/concurrent.futures.html#module-functions)
  - [Exception classes](https://docs.python.org/3.14/library/concurrent.futures.html#exception-classes)

[Subject index](INDEX.md) · [Continue](concurrent-execution.md)
