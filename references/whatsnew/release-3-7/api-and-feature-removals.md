# What's New In Python 3.7 / API and Feature Removals — asyncio, collections, os.path, plistlib, re, selectors, socket, ssl, tarfile

### API and Feature Removals

These features and APIs are gone from Python 3.7:

- The `os.stat_float_times()` function is no more. Added back in Python 2.3 so it could stay compatible with Python 2.2, it had been deprecated ever since Python 3.1.

- Inside replacement templates passed to [`re.sub()`](https://docs.python.org/3.14/library/re.html#re.sub), unknown escapes made from `'\'` plus an ASCII letter were deprecated in Python 3.5 and will from now on raise an error.

- The *exclude* argument support was dropped from [`tarfile.TarFile.add()`](https://docs.python.org/3.14/library/tarfile.html#tarfile.TarFile.add). Deprecated across Python 2.7 and 3.2, it should be replaced by the *filter* argument.

- The `ntpath.splitunc()` function, deprecated since Python 3.1, has now been taken out. Reach for [`splitdrive()`](https://docs.python.org/3.14/library/os.path.html#os.path.splitdrive) instead.

- [`collections.namedtuple()`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple) has dropped both the *verbose* parameter and the `_source` attribute that used to expose the generated source code for the named tuple class. Removing them formed part of an optimization meant to accelerate class creation. (Contributed by Jelle Zijlstra, refined later on by INADA Naoki, plus Serhiy Storchaka and Raymond Hettinger, in [bpo-28638](https://bugs.python.org/issue?@action=redirect&bpo=28638).)

- The [`bool()`](https://docs.python.org/3.14/library/functions.html#bool), [`float()`](https://docs.python.org/3.14/library/functions.html#float), [`list()`](https://docs.python.org/3.14/library/stdtypes.html#list) and [`tuple()`](https://docs.python.org/3.14/library/stdtypes.html#tuple) functions no longer accept keyword arguments. As for [`int()`](https://docs.python.org/3.14/library/functions.html#int), its first argument may now be supplied solely as a positional argument.

- The `Plist`, `Dict` and `_InternalDict` classes inside the [`plistlib`](https://docs.python.org/3.14/library/plistlib.html#module-plistlib) module, deprecated way back in Python 2.4, have been removed. Dict values returned by the `readPlist()` and `readPlistFromBytes()` functions are now ordinary dicts. Attribute access to reach items of these dictionaries is no longer permitted.

- The `asyncio.windows_utils.socketpair()` function is gone. Rely on the [`socket.socketpair()`](https://docs.python.org/3.14/library/socket.html#socket.socketpair) function in its place, since it has been present across every platform from Python 3.5 onward. On Python 3.5 and later, `asyncio.windows_utils.socketpair` had merely been an alias for `socket.socketpair`.

- [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) stopped exporting the [`selectors`](https://docs.python.org/3.14/library/selectors.html#module-selectors) and `_overlapped` modules under the names `asyncio.selectors` and `asyncio._overlapped`. Swap `from asyncio import selectors` for `import selectors`.

- Constructing [`ssl.SSLSocket`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket) and [`ssl.SSLObject`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLObject) objects directly is now forbidden. Their constructors had never been documented, tested, or meant to serve as public constructors. The expectation was that users would rely on `ssl.wrap_socket()` or [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext). (Contributed by Christian Heimes in [bpo-32951](https://bugs.python.org/issue?@action=redirect&bpo=32951).)

- The unused `distutils` `install_misc` command is gone. (Contributed by Eric N. Vander Weele in [bpo-29218](https://bugs.python.org/issue?@action=redirect&bpo=29218).)

[Subject index](INDEX.md) · [Previous source section](platform-support-removals.md) · [Next source section](module-removals.md) · [Release/subject declaration](summary-release-highlights.md)
