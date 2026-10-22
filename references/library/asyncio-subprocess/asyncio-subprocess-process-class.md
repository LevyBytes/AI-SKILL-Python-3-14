# asyncio.subprocess: `asyncio.subprocess.Process`

### Interacting with Subprocesses

Each of the `create_subprocess_exec()` and `create_subprocess_shell()` functions hands back instances of the *Process* class. *Process* is a high-level wrapper that supports communicating with subprocesses and watching for their completion.

 *class *asyncio.subprocess.Process

An object wrapping the OS processes spawned by the `create_subprocess_exec()` and `create_subprocess_shell()` functions.

The intent is for this class to mirror the API of the [`subprocess.Popen`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen) class, though a few noteworthy distinctions exist:

- in contrast to Popen, Process instances offer nothing matching the [`poll()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen.poll) method;

- the `communicate()` and `wait()` methods omit a *timeout* parameter: rely on the [`wait_for()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.wait_for) function;

- the `Process.wait()` method runs asynchronously, while the [`subprocess.Popen.wait()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen.wait) method is built as a blocking busy loop;

- the *universal_newlines* parameter has no support.

This class is [not thread safe](https://docs.python.org/3.14/library/asyncio-dev.html#asyncio-multithreading).

See also the Subprocess and Threads section.

[Subject index](INDEX.md) · [Previous](asyncio-subprocess-pipe-to-asyncio-subprocess-devnull.md) · [Continue](subprocess-wait-communicate-and-signals.md)
