# Creating Subprocesses

### Creating Subprocesses

 *async *asyncio.create_subprocess_exec(*program*, **args*, *stdin=None*, *stdout=None*, *stderr=None*, *limit=None*, ***kwds*)

Create a subprocess.

The *limit* argument fixes the buffer cap for [`StreamReader`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.StreamReader) wrappers around `stdout` and `stderr` (when [`subprocess.PIPE`](https://docs.python.org/3.14/library/subprocess.html#subprocess.PIPE) gets supplied to the *stdout* and *stderr* arguments).

Return a `Process` instance.

Refer to the documentation for [`loop.subprocess_exec()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.subprocess_exec) regarding the remaining parameters.

Should the process object be garbage collected while its process keeps running, the child process gets killed.

Changed in version 3.10: Removed the *loop* parameter.

 *async *asyncio.create_subprocess_shell(*cmd*, *stdin=None*, *stdout=None*, *stderr=None*, *limit=None*, ***kwds*)

Run the *cmd* shell command.

The *limit* argument fixes the buffer cap for [`StreamReader`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.StreamReader) wrappers around `stdout` and `stderr` (when [`subprocess.PIPE`](https://docs.python.org/3.14/library/subprocess.html#subprocess.PIPE) gets supplied to the *stdout* and *stderr* arguments).

Return a `Process` instance.

Refer to the documentation for [`loop.subprocess_shell()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.subprocess_shell) regarding the remaining parameters.

Should the process object be garbage collected while its process keeps running, the child process gets killed.

Important

Ensuring that all whitespace and special characters get quoted correctly, so as to head off [shell injection](https://en.wikipedia.org/wiki/Shell_injection#Shell_injection) vulnerabilities, falls to the application. The [`shlex.quote()`](https://docs.python.org/3.14/library/shlex.html#shlex.quote) function is available to correctly escape whitespace and special shell characters in any strings destined to build shell commands.

Changed in version 3.10: Removed the *loop* parameter.

Note

Subprocesses work on Windows provided a [`ProactorEventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.ProactorEventLoop) is in use. Consult [Subprocess Support on Windows](https://docs.python.org/3.14/library/asyncio-platforms.html#asyncio-windows-subprocess) for the particulars.

See also

asyncio additionally provides these *low-level* APIs for working with subprocesses: [`loop.subprocess_exec()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.subprocess_exec), [`loop.subprocess_shell()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.subprocess_shell), [`loop.connect_read_pipe()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.connect_read_pipe), [`loop.connect_write_pipe()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.connect_write_pipe), plus the [Subprocess Transports](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio-subprocess-transports) and [Subprocess Protocols](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio-subprocess-protocols).

[Subject index](INDEX.md) · [Previous](subprocesses.md) · [Continue](asyncio-subprocess-pipe-to-asyncio-subprocess-devnull.md)
