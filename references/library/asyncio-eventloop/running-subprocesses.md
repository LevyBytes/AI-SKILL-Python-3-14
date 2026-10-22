# asyncio.eventloop: Low-level subprocess transport prerequisites

### Running subprocesses

The methods covered in these subsections operate at a low level. For ordinary async/await code, reach instead for the high-level [`asyncio.create_subprocess_shell()`](https://docs.python.org/3.14/library/asyncio-subprocess.html#asyncio.create_subprocess_shell) and [`asyncio.create_subprocess_exec()`](https://docs.python.org/3.14/library/asyncio-subprocess.html#asyncio.create_subprocess_exec) convenience functions.

Note

Under Windows the default event loop is `ProactorEventLoop`, which handles subprocesses; `SelectorEventLoop` does not. Refer to [Subprocess Support on Windows](https://docs.python.org/3.14/library/asyncio-platforms.html#asyncio-windows-subprocess) for the specifics.

[Subject index](INDEX.md) · [Previous](loop-get-debug-to-loop-slow-callback-duration.md) · [Continue](loop-subprocess-exec.md)
