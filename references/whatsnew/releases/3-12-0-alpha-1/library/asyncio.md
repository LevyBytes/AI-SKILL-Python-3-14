# Python 3.12.0 alpha 1 / library / asyncio

[gh-89237](https://github.com/python/cpython/issues/89237): Corrects a Windows hang in `subprocess.wait_closed()` under [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) with [`ProactorEventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.ProactorEventLoop). Kumar Aditya wrote the patch.

[gh-85760](https://github.com/python/cpython/issues/85760): A race condition in [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) is resolved; previously [`process_exited()`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.SubprocessProtocol.process_exited) could run ahead of [`pipe_data_received()`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.SubprocessProtocol.pipe_data_received), which produced inconsistent output. Kumar Aditya supplied the patch.

[gh-96704](https://github.com/python/cpython/issues/96704): The right `contextvars.Context` is now handed over whenever an `asyncio` exception handler runs for a task or callback handle. A fresh `Task` method named `get_context` arrives here, along with an identically named `Handle` method. Should a task object lack this method — say it comes from a third-party library that has not added it yet — then the context active at the moment the exception handler fires gets used instead.

[gh-93297](https://github.com/python/cpython/issues/93297): Have asyncio task groups keep their child tasks from getting garbage collected

[gh-88050](https://github.com/python/cpython/issues/88050): The [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) subprocess transport is fixed so it kills a process cleanly when that process is blocked, and to sidestep a `RuntimeError` once the loop has closed. Kumar Aditya wrote the patch.

[gh-96827](https://github.com/python/cpython/issues/96827): Stops spurious tracebacks from [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) whenever default executor cleanup is postponed until after the event loop has closed (for example, following a keyboard interrupt).

[bpo-46364](https://bugs.python.org/issue?@action=redirect&bpo=46364): Confine the substitution of sockets for pipes on subprocess stdin created by [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) so it happens only on the AIX platform.

[bpo-45924](https://bugs.python.org/issue?@action=redirect&bpo=45924): Fixed a wrong [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) traceback produced when a future's exception gets raised more than once. Kumar Aditya wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
