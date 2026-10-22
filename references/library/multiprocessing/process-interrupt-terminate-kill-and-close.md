# multiprocessing.Process: `interrupt()`, `terminate()`, `kill()`, `close()`

During the initialization of `multiprocessing`, the main process receives a random string produced via [`os.urandom()`](https://docs.python.org/3.14/library/os.html#os.urandom).

A freshly created `Process` object takes on the authentication key belonging to its parent process, though you may override this by assigning `authkey` a different byte string.

See Authentication keys.

 sentinel

An integer handle referring to a system object that turns “ready” at the moment the process finishes.

This value comes in handy when you want to wait on multiple events simultaneously through `multiprocessing.connection.wait()`. Otherwise it is simpler to just call `join()`.

Under Windows, the value is an OS handle suited to the `WaitForSingleObject` and `WaitForMultipleObjects` family of API calls. Under POSIX, it is a file descriptor that works with primitives from the [`select`](https://docs.python.org/3.14/library/select.html#module-select) module.

Added in version 3.3.

 interrupt()

End the process. This functions on POSIX via the [`SIGINT`](https://docs.python.org/3.14/library/signal.html#signal.SIGINT) signal. On Windows the behavior is not defined.

By default the child process is stopped by raising [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt). You can change this by installing the matching signal handler within the child process [`signal.signal()`](https://docs.python.org/3.14/library/signal.html#signal.signal) for [`SIGINT`](https://docs.python.org/3.14/library/signal.html#signal.SIGINT).

Note: should the child process trap and swallow [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt), the process stays alive.

Note: this default behavior additionally sets `exitcode` to `1`, just as though an uncaught exception had surfaced in the child process. For a different `exitcode`, simply trap [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt) and invoke `exit(your_code)`.

Added in version 3.14.

 terminate()

End the process. POSIX uses the [`SIGTERM`](https://docs.python.org/3.14/library/signal.html#signal.SIGTERM) signal for this; Windows relies on `TerminateProcess()`. Be aware that exit handlers, finally clauses, and similar code will be skipped.

Be aware too that descendant processes of this process are *not* ended — they merely become orphaned.

Warning

Calling this method while the associated process is busy with a pipe or queue risks corrupting that pipe or queue, possibly leaving it unusable for other processes. In the same way, if the process holds a lock or semaphore and so on, ending it risks deadlocking other processes.

 kill()

The same as `terminate()`, except it sends the `SIGKILL` signal under POSIX.

Added in version 3.7.

 close()

Shut the `Process` object down, freeing every resource tied to it. A [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised when the underlying process has not stopped running yet. After `close()` succeeds, the bulk of the other methods and attributes on the `Process` object will raise `ValueError`.

Added in version 3.7.

Be aware that only the process that created the process object ought to call the `start()`, `join()`, `is_alive()`, `terminate()` and `exitcode` methods.

Example usage of some of the methods of `Process`:

```pycon
>>> import multiprocessing, time, signal
>>> mp_context = multiprocessing.get_context('spawn')
>>> p = mp_context.Process(target=time.sleep, args=(1000,))
>>> print(p, p.is_alive())
<...Process ... initial> False
>>> p.start()
>>> print(p, p.is_alive())
<...Process ... started> True
>>> p.terminate()
>>> time.sleep(0.1)
>>> print(p, p.is_alive())
<...Process ... stopped exitcode=-SIGTERM> False
>>> p.exitcode == -signal.SIGTERM
True

```

[Subject index](INDEX.md) · [Continue](multiprocessing-processerror-to-multiprocessing-timeouterror.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md) · [Owning module, declaration or section: multiprocessing.Process](multiprocessing-process-class.md) · [Owning module, declaration or section: `Process` and exceptions](multiprocessing-process-class.md) · [Owning module, declaration or section: authkey](process-run-start-join-and-liveness.md) · [Preceding source contract and version conditions](process-run-start-join-and-liveness.md)
