# Python 3.13.0 alpha 3 / library / exceptions

[gh-112182](https://github.com/python/cpython/issues/112182): `asyncio.futures.Future.set_exception()` will now convert [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) into [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) rather than hanging or otherwise misbehaving. Jamie Phan contributed this patch.

[gh-114077](https://github.com/python/cpython/issues/114077): Resolved a possible [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) within [`socket.socket.sendfile()`](https://docs.python.org/3.14/library/socket.html#socket.socket.sendfile) whenever *count* is passed larger than 2 GiB on a 32-bit platform.

[gh-96037](https://github.com/python/cpython/issues/96037): Place [`TimeoutError`](https://docs.python.org/3.14/library/exceptions.html#TimeoutError) into the context of whatever exception was raised while leaving an expired [`asyncio.timeout()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.timeout) block.

[gh-113594](https://github.com/python/cpython/issues/113594): Resolved a [`UnicodeEncodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeEncodeError) inside [`email`](https://docs.python.org/3.14/library/email.html#module-email) while re-folding lines holding an unknown-8bit encoded part trailed by a non-unknown-8bit encoded part.

[gh-112578](https://github.com/python/cpython/issues/112578): Eliminate a bogus [`RuntimeWarning`](https://docs.python.org/3.14/library/exceptions.html#RuntimeWarning) raised while running the [`zipfile`](https://docs.python.org/3.14/library/zipfile.html#module-zipfile) module.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
