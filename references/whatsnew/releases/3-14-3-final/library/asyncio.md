# Python 3.14.3 final / library / asyncio

[gh-143046](https://github.com/python/cpython/issues/143046): In quiet mode ([`-q`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-q)), the [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) REPL no longer emits the copyright and version messages. Bartosz Sławecki supplied the patch.

[gh-140648](https://github.com/python/cpython/issues/140648): The [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) REPL now honors the [`-I`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-I) flag (isolated mode). Earlier it would load and run [`PYTHONSTARTUP`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONSTARTUP) even with that flag set. Bartosz Sławecki contributed this.

[gh-142784](https://github.com/python/cpython/issues/142784): The [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) REPL now closes the loop correctly once an interactive session ends. It could previously raise surprising warnings. Bartosz Sławecki contributed this.

[gh-142556](https://github.com/python/cpython/issues/142556): Within [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio), a crash is fixed that triggered when a task was re-registered partway through finalization. Kumar Aditya supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
