# Python 3.10.0 alpha 1 / library / exceptions

[bpo-41467](https://bugs.python.org/issue?@action=redirect&bpo=41467): Under Windows, corrected the value returned by asyncio `recv_into()` once the socket/pipe is closed ([`BrokenPipeError`](https://docs.python.org/3.14/library/exceptions.html#BrokenPipeError)): it now returns `0` instead of an empty byte string (`b''`).

[bpo-36290](https://bugs.python.org/issue?@action=redirect&bpo=36290): When keyword arguments conflict, AST nodes now raise [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). Rémi Lapeyre submitted the contributing patch.

[bpo-41193](https://bugs.python.org/issue?@action=redirect&bpo=41193): The readline completer's `write_history()` atexit function now swallows any [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError), so an error is ignored on a read-only filesystem, rather than only ignoring [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError) and [`PermissionError`](https://docs.python.org/3.14/library/exceptions.html#PermissionError).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
