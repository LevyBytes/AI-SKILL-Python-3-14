# Python 3.9.0 alpha 1 / library / threads and concurrency

[bpo-37266](https://bugs.python.org/issue?@action=redirect&bpo=37266): Trying to spawn a daemon thread inside a subinterpreter now raises an exception, since subinterpreters never supported daemon threads. Earlier, if such a thread was still alive, subinterpreter finalization would bring down the runtime with a Python fatal error.

[bpo-36402](https://bugs.python.org/issue?@action=redirect&bpo=36402): Closed a race condition during Python shutdown while threads were being awaited. The code now holds off until the Python thread state of every non-daemon thread has been deleted (joining all non-daemon threads), in place of merely waiting for the non-daemon Python threads to finish.

[bpo-31783](https://bugs.python.org/issue?@action=redirect&bpo=31783): Closed a race condition inside ThreadPoolExecutor that occurred when worker threads got created while the interpreter was shutting down.

[bpo-34679](https://bugs.python.org/issue?@action=redirect&bpo=34679): The signal.set_wakeup_fd() call inside asynci.ProactorEventLoop.close() is now restricted to the main thread.

[bpo-36250](https://bugs.python.org/issue?@action=redirect&bpo=36250): Suppress `ValueError` raised by `signal` together with `interaction` when running outside the main thread.

[bpo-10978](https://bugs.python.org/issue?@action=redirect&bpo=10978): Semaphores and BoundedSemaphores are now able to release several waiting threads simultaneously.

[bpo-34679](https://bugs.python.org/issue?@action=redirect&bpo=34679): Reinstated the creation of Windows IOCP event loops from a non-main thread.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
