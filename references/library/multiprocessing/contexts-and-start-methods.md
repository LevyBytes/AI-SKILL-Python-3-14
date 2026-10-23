# multiprocessing - Contexts and start methods

### Contexts and start methods

`multiprocessing` offers three platform-dependent ways of launching a process. These *start methods* are

>

*spawn*

A brand-new Python interpreter process is launched by the parent. Only the resources strictly required to run the process object's `run()` method get inherited by the child. Notably, extraneous file descriptors and handles belonging to the parent are not passed along. Launching a process this way is fairly slow next to *fork* or *forkserver*.

Available on POSIX and Windows platforms. The default on Windows and macOS.

*fork*

The parent process uses [`os.fork()`](https://docs.python.org/3.14/library/os.html#os.fork) to fork the Python interpreter. At the point it starts, the child process is essentially a copy of the parent. The child inherits every one of the parent's resources. Be aware that forking a multithreaded process safely is tricky.

Available on POSIX systems.

Changed in version 3.14: On every platform, this has stopped being the default start method. Any code depending on *fork* now has to request it deliberately through `get_context()` or `set_start_method()`.

Changed in version 3.12: When Python can tell that your process holds more than one thread, the [`os.fork()`](https://docs.python.org/3.14/library/os.html#os.fork) function invoked internally by this start method will raise a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). Pick a different start method instead. The `os.fork()` documentation explains this more fully.

*forkserver*

If a program picks the *forkserver* start method as it begins, a server process gets launched. After that, every time a new process is wanted, the parent reaches out to the server and asks it to fork a fresh process. Barring threads spawned as a side-effect by system libraries or preloaded imports, the fork server process keeps to one thread, which makes calling [`os.fork()`](https://docs.python.org/3.14/library/os.html#os.fork) from it generally safe. No unnecessary resources are inherited.

Available on POSIX systems, like Linux, that allow file descriptors to be passed across Unix pipes. It is the default there.

Changed in version 3.14: Across POSIX platforms, this turned into the default start method.

Changed in version 3.4: Every POSIX platform gained *spawn*, while *forkserver* arrived on a subset of POSIX platforms. On Windows, child processes stopped inheriting the full set of the parent's inheritable handles.

Changed in version 3.8: The *spawn* start method now serves as the default on macOS. Treat the *fork* start method as unsafe there, since it can crash the subprocess when macOS system libraries start threads. See [bpo-33725](https://bugs.python.org/issue?@action=redirect&bpo=33725).

Changed in version 3.14: To keep the performance while sidestepping the usual multithreaded-process problems, the POSIX default start method moved from *fork* over to *forkserver*. See [gh-84559](https://github.com/python/cpython/issues/84559).

On POSIX, choosing either the *spawn* or *forkserver* start method additionally launches a *resource tracker* process, which keeps tabs on the unlinked named system resources (such as named semaphores or [`SharedMemory`](https://docs.python.org/3.14/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory) objects) that the program's processes create. Once every process has exited, the resource tracker unlinks whatever tracked object is left over. Ordinarily nothing remains, but should a process be killed by a signal, some "leaked" resources may persist. (Until the machine reboots, no leaked semaphore or shared memory segment gets unlinked on its own. Both kinds of object pose a problem here, because the system caps how many named semaphores may exist, and shared memory segments consume a portion of main memory.)

To pick a start method, call `set_start_method()` from within the `if __name__ == '__main__'` clause of the main module. For example:

```python
import multiprocessing as mp

def foo(q):
    q.put('hello')

if __name__ == '__main__':
    mp.set_start_method('spawn')
    q = mp.Queue()
    p = mp.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()

```

Do not call `set_start_method()` more than once within the program.

As an alternative, calling `get_context()` hands you back a context object. Such context objects share the same API as the multiprocessing module, and let you employ several start methods within a single program.

```python
import multiprocessing as mp

def foo(q):
    q.put('hello')

if __name__ == '__main__':
    ctx = mp.get_context('spawn')
    q = ctx.Queue()
    p = ctx.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()

```

Bear in mind that objects tied to one context may not work with processes belonging to another context. Specifically, locks built with the *fork* context cannot be handed to processes launched via the *spawn* or *forkserver* start methods.

Code in libraries that use `multiprocessing` or [`ProcessPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor) ought to be written so callers can supply their own multiprocessing context. Pinning a library to one particular context of your own may clash with the rest of the application written by the library's user. Always document if your library requires a specific start method.

Warning

On POSIX systems the `'spawn'` and `'forkserver'` start methods generally will not work with "frozen" executables (that is, binaries built by packages such as **PyInstaller** and **cx_Freeze**). The `'fork'` start method may work if code does not use threads.

[Subject index](INDEX.md) · [Previous](the-process-class.md) · [Continue](exchanging-objects-between-processes.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md)
