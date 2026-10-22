# Python 3.14.4 final / library / asyncio subprocess

[gh-145551](https://github.com/python/cpython/issues/145551): Corrects an InvalidStateError when cancelling a process spawned by [`asyncio.create_subprocess_exec()`](https://docs.python.org/3.14/library/asyncio-subprocess.html#asyncio.create_subprocess_exec) or [`asyncio.create_subprocess_shell()`](https://docs.python.org/3.14/library/asyncio-subprocess.html#asyncio.create_subprocess_shell). Daan De Meyer supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
