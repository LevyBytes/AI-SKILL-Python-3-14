# asyncio.subprocess: `wait()`, `communicate()`, `send_signal()`, `terminate()`, `kill()`

*async *wait()

Wait for the child process to terminate.

Set and return the `returncode` attribute.

Note

A deadlock can arise from this method whenever you use `stdout=PIPE` or `stderr=PIPE` and the child process emits enough output that it stalls, waiting on the OS pipe buffer to take more data. Steer clear of this situation by reaching for the `communicate()` method whenever pipes are involved.

 *async *communicate(*input=None*)

Interact with process:

1.

send data to *stdin* (if *input* is not `None`);

2.

closes *stdin*;

3.

read data from *stdout* and *stderr*, until EOF is reached;

4.

wait for process to terminate.

The optional *input* argument holds the data (a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object) to be delivered to the child process.

Return a tuple `(stdout_data, stderr_data)`.

Where either a [`BrokenPipeError`](https://docs.python.org/3.14/library/exceptions.html#BrokenPipeError) or [`ConnectionResetError`](https://docs.python.org/3.14/library/exceptions.html#ConnectionResetError) exception arises while *input* is being written into *stdin*, that exception gets ignored. The situation crops up when the process finishes ahead of all data being written into *stdin*.

To deliver data to the process' *stdin*, you must have created the process with `stdin=PIPE`. In the same way, getting back anything besides `None` in the result tuple requires that the process was created with `stdout=PIPE` and/or `stderr=PIPE` arguments.

Bear in mind that the data read sits buffered in memory, so steer clear of this method whenever the data size is large or has no fixed bound.

Changed in version 3.12: *stdin* gets closed when `input=None` too.

 send_signal(*signal*)

Sends the signal *signal* to the child process.

Note

On Windows, [`SIGTERM`](https://docs.python.org/3.14/library/signal.html#signal.SIGTERM) serves as an alias for `terminate()`. You can dispatch `CTRL_C_EVENT` and `CTRL_BREAK_EVENT` to processes launched with a *creationflags* parameter that bundles in `CREATE_NEW_PROCESS_GROUP`.

 terminate()

Stop the child process.

On POSIX systems this method dispatches [`SIGTERM`](https://docs.python.org/3.14/library/signal.html#signal.SIGTERM) to the child process.

On Windows the Win32 API function `TerminateProcess()` gets invoked to halt the child process.

 kill()

Kill the child process.

On POSIX systems this method dispatches [`SIGKILL`](https://docs.python.org/3.14/library/signal.html#signal.SIGKILL) to the child process.

On Windows this method acts as an alias for `terminate()`.

 stdin

Standard input stream ([`StreamWriter`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.StreamWriter)) or `None` if the process was created with `stdin=None`.

 stdout

Standard output stream ([`StreamReader`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.StreamReader)) or `None` if the process was created with `stdout=None`.

 stderr

Standard error stream ([`StreamReader`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.StreamReader)) or `None` if the process was created with `stderr=None`.

Warning

Prefer the `communicate()` method over `process.stdin.write()`, `await process.stdout.read()` or `await process.stderr.read()`. Doing so sidesteps deadlocks brought on by streams that pause their reading or writing and so stall the child process.

[Subject index](INDEX.md) · [Previous](asyncio-subprocess-process-class.md) · [Continue](interacting-with-subprocesses.md) · [Owning module, declaration or section: asyncio.subprocess.Process](asyncio-subprocess-process-class.md) · [Owning module, declaration or section: Interacting with Subprocesses](asyncio-subprocess-process-class.md)
