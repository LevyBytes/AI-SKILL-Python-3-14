# subprocess: `Popen.poll()`, `Popen.wait()`, `Popen.communicate()`, `Popen.send_signal()`, `Popen.terminate()`, `Popen.kill()`, `Popen.args`, `Popen.stdin`

### Popen Objects

Objects of the `Popen` class provide the methods below:

 Popen.poll()

Test whether the child process has finished. Set the `returncode` attribute and hand it back; failing that, return `None`.

 Popen.wait(*timeout=None*)

Block until the child process finishes. Set the `returncode` attribute and hand it back.

Should the process still be running after *timeout* seconds, a `TimeoutExpired` exception is raised. Catching that exception and retrying the wait is safe.

Note

A deadlock arises with `stdout=PIPE` or `stderr=PIPE` once the child process emits so much output to a pipe that it stalls, awaiting room in the OS pipe buffer for further data. Steer clear of that by reaching for `Popen.communicate()` whenever pipes are involved.

Note

Whenever the `timeout` parameter differs from `None`, the function (under POSIX) relies on a busy loop made of non-blocking calls and brief sleeps. For an asynchronous wait, turn to the [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) module: see [`asyncio.create_subprocess_exec`](https://docs.python.org/3.14/library/asyncio-subprocess.html#asyncio.create_subprocess_exec).

Changed in version 3.3: *timeout* was added.

 Popen.communicate(*input=None*, *timeout=None*)

Exchange data with the process: push data into stdin, pull data from stdout and stderr until end-of-file arrives, then await the process's termination and set the `returncode` attribute. The optional *input* argument holds the data destined for the child process, or `None` when nothing should be sent. When the streams were opened in text mode, *input* has to be a string; otherwise it has to be bytes.

`communicate()` hands back a tuple `(stdout_data, stderr_data)`. Those data are strings if the streams were opened in text mode, and bytes otherwise.

Bear in mind that sending data to the process's stdin requires building the Popen object with `stdin=PIPE`. In the same way, obtaining something besides `None` in the result tuple requires also supplying `stdout=PIPE` and/or `stderr=PIPE`.

Should the process still be running after *timeout* seconds, a `TimeoutExpired` exception gets raised. Catching that exception and retrying communication loses none of the output. Feeding *input* into a later post-timeout `communicate()` call counts as undefined behavior and might turn into an error down the road.

Since the expiring timeout does not kill the child process, a well-mannered application should, for proper cleanup, kill the child process and round off communication:

```python
proc = subprocess.Popen(...)
try:
    outs, errs = proc.communicate(timeout=15)
except TimeoutExpired:
    proc.kill()
    outs, errs = proc.communicate()

```

Once `communicate()` has raised `TimeoutExpired`, refrain from calling `wait()`. Issue a further `communicate()` call instead to wrap up pipe handling and fill in the `returncode` attribute.

Note

Whatever is read gets buffered in memory, so steer clear of this method when the data size is large or has no bound.

Changed in version 3.3: *timeout* was added.

 Popen.send_signal(*signal*)

Deliver the signal *signal* to the child.

Take no action when the process has already finished.

Note

Under Windows, SIGTERM serves as an alias for `terminate()`. You can deliver CTRL_C_EVENT and CTRL_BREAK_EVENT to processes launched with a *creationflags* parameter that carries `CREATE_NEW_PROCESS_GROUP`.

 Popen.terminate()

Halt the child. Under POSIX operating systems the method delivers [`SIGTERM`](https://docs.python.org/3.14/library/signal.html#signal.SIGTERM) to the child. Under Windows it halts the child by calling the Win32 API function `TerminateProcess()`.

 Popen.kill()

Terminate the child. Under POSIX operating systems the function delivers SIGKILL to the child. Under Windows `kill()` doubles as an alias for `terminate()`.

The class additionally populates the attributes below for your reading. Putting new values back into them is unsupported:

 Popen.args

The *args* argument exactly as handed to `Popen` — either a sequence of program arguments or a lone string.

Added in version 3.3.

 Popen.stdin

When the *stdin* argument was `PIPE`, this attribute holds a writeable stream object such as [`open()`](https://docs.python.org/3.14/library/functions.html#open) yields. The stream is a text stream when the *encoding* or *errors* arguments were given, or when the *text* or *universal_newlines* argument was `True`; otherwise it is a byte stream. When the *stdin* argument was something other than `PIPE`, this attribute is `None`.

[Subject index](INDEX.md) · [Previous](security-considerations.md) · [Continue](popen-stdout-to-popen-returncode.md) · [Owning module, declaration or section: subprocess](subprocess-subprocess-management.md)
