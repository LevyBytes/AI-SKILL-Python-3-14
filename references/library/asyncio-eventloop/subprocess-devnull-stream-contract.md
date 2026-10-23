# Running subprocesses - Contract: the `subprocess.DEVNULL` constant, marking that the dedicated `os.devnull` file is used

the [`subprocess.DEVNULL`](https://docs.python.org/3.14/library/subprocess.html#subprocess.DEVNULL) constant, marking that the dedicated [`os.devnull`](https://docs.python.org/3.14/library/os.html#os.devnull) file is used

  - the [`subprocess.STDOUT`](https://docs.python.org/3.14/library/subprocess.html#subprocess.STDOUT) constant, which ties the standard error stream into the process’ standard output stream

- Every remaining keyword argument is forwarded verbatim to [`subprocess.Popen`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen), with the sole exceptions of *bufsize*, *universal_newlines*, *shell*, *text*, *encoding* and *errors* — none of which you should pass at all.

Decoding subprocess streams into text is not something the `asyncio` subprocess API offers. To turn the bytes read from a stream into text, apply [`bytes.decode()`](https://docs.python.org/3.14/library/stdtypes.html#bytes.decode).

Should a file-like object supplied as *stdin*, *stdout* or *stderr* stand for a pipe, register the pipe's opposite end through `connect_write_pipe()` or `connect_read_pipe()` so the event loop can work with it.

See the constructor of the [`subprocess.Popen`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen) class for documentation on other arguments.

Hands back a `(transport, protocol)` pair, where *transport* conforms to the [`asyncio.SubprocessTransport`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.SubprocessTransport) base class and *protocol* is an object that the *protocol_factory* produced.

When the transport gets closed or garbage collected, any child process still running is killed.

[Subject index](INDEX.md) · [Previous](loop-subprocess-exec.md) · [Continue](loop-subprocess-shell.md) · [Owning module, declaration or section: Running subprocesses](running-subprocesses.md) · [Owning module, declaration or section: loop.subprocess_exec](loop-subprocess-exec.md)
