# asyncio.eventloop: `loop.subprocess_shell()`

*async *loop.subprocess_shell(*protocol_factory*, *cmd*, ***, *stdin=subprocess.PIPE*, *stdout=subprocess.PIPE*, *stderr=subprocess.PIPE*, ***kwargs*)

Launch a subprocess from *cmd* — given as a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), or a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) string encoded to the [filesystem encoding](https://docs.python.org/3.14/library/os.html#filesystem-encoding) — interpreted through the platform’s “shell” syntax.

This parallels the standard library [`subprocess.Popen`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen) class invoked with `shell=True`.

The *protocol_factory* must be a callable returning a subclass of the [`SubprocessProtocol`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.SubprocessProtocol) class.

Refer to `subprocess_exec()` for fuller coverage of the arguments that remain.

Hands back a `(transport, protocol)` pair, where *transport* conforms to the [`SubprocessTransport`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.SubprocessTransport) base class and *protocol* is an object that the *protocol_factory* produced.

When the transport gets closed or garbage collected, any child process still running is killed.

Note

Ensuring every whitespace and special character is correctly quoted, so as to head off [shell injection](https://en.wikipedia.org/wiki/Shell_injection#Shell_injection) vulnerabilities, falls to the application. Use the [`shlex.quote()`](https://docs.python.org/3.14/library/shlex.html#shlex.quote) function to escape whitespace and special characters properly within any strings destined to build shell commands.

[Subject index](INDEX.md) · [Previous](subprocess-devnull-stream-contract.md) · [Continue](asyncio-handle-class.md) · [Owning module, declaration or section: Running subprocesses](running-subprocesses.md)
