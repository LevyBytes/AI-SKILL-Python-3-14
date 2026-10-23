# What’s New In Python 3.12 / Pending removal in future versions - threading, typing, unittest, urllib.parse

- `ssl.TLSVersion.TLSv1`

  - `ssl.TLSVersion.TLSv1_1`

- [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) methods:

  - `threading.Condition.notifyAll()`: switch to [`notify_all()`](https://docs.python.org/3.14/library/threading.html#threading.Condition.notify_all).

  - `threading.Event.isSet()`: switch to [`is_set()`](https://docs.python.org/3.14/library/threading.html#threading.Event.is_set).

  - `threading.Thread.isDaemon()`, [`threading.Thread.setDaemon()`](https://docs.python.org/3.14/library/threading.html#threading.Thread.setDaemon): adopt the [`threading.Thread.daemon`](https://docs.python.org/3.14/library/threading.html#threading.Thread.daemon) attribute.

  - `threading.Thread.getName()`, [`threading.Thread.setName()`](https://docs.python.org/3.14/library/threading.html#threading.Thread.setName): adopt the [`threading.Thread.name`](https://docs.python.org/3.14/library/threading.html#threading.Thread.name) attribute.

  - `threading.currentThread()`: switch to [`threading.current_thread()`](https://docs.python.org/3.14/library/threading.html#threading.current_thread).

  - `threading.activeCount()`: switch to [`threading.active_count()`](https://docs.python.org/3.14/library/threading.html#threading.active_count).

- [`typing.Text`](https://docs.python.org/3.14/library/typing.html#typing.Text) ([gh-92332](https://github.com/python/cpython/issues/92332)).

- The internal class `typing._UnionGenericAlias` no longer backs the implementation of [`typing.Union`](https://docs.python.org/3.14/library/typing.html#typing.Union). For anyone still importing this private class, a compatibility shim stays in place through at least Python 3.17. (Contributed by Jelle Zijlstra in [gh-105499](https://github.com/python/cpython/issues/105499).)

- [`unittest.IsolatedAsyncioTestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.IsolatedAsyncioTestCase): returning a value other than `None` from a test case is deprecated.

- [`urllib.parse`](https://docs.python.org/3.14/library/urllib.parse.html#module-urllib.parse) deprecated functions: use [`urlparse()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.urlparse) in their place

  - `splitattr()`

  - `splithost()`

  - `splitnport()`

  - `splitpasswd()`

  - `splitport()`

  - `splitquery()`

  - `splittag()`

  - `splittype()`

[Subject index](INDEX.md) · [Previous source section](pending-removal-in-future-versions-importlib-metadata.md) · [Next source section](pending-removal-in-future-versions-splituser.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](undated-api-removals.md)
