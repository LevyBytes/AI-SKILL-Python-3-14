# What’s New In Python 3.12 / Pending removal in Python 3.16 - array, asyncio, asyncio-eventloop, asyncio-policy, asyncio-runner, builtins, functools, importlib, inspect

### Pending removal in Python 3.16

- The import system:

  - Assigning [`__loader__`](https://docs.python.org/3.14/reference/datamodel.html#module.__loader__) on a module without also assigning [`__spec__.loader`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec.loader) now carries a deprecation. Come Python 3.16, the import machinery and the standard library will neither assign `__loader__` nor consult it.

- [`array`](https://docs.python.org/3.14/library/array.html#module-array):

  - The `'u'` format code (`wchar_t`) has been deprecated in the docs since Python 3.3 and at runtime since Python 3.13. Switch to the `'w'` format code ([`Py_UCS4`](https://docs.python.org/3.14/c-api/unicode.html#c.Py_UCS4)) for Unicode characters in its place.

- [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio):

  - A deprecation covers `asyncio.iscoroutinefunction()`, which gets dropped in Python 3.16; reach for [`inspect.iscoroutinefunction()`](https://docs.python.org/3.14/library/inspect.html#inspect.iscoroutinefunction) in its place. (Contributed by Jiahao Li and Kumar Aditya in [gh-122875](https://github.com/python/cpython/issues/122875).)

  - The [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) policy system now carries a deprecation and gets dropped in Python 3.16. Specifically, the classes and functions below are deprecated:

    - [`asyncio.AbstractEventLoopPolicy`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.AbstractEventLoopPolicy)

    - [`asyncio.DefaultEventLoopPolicy`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.DefaultEventLoopPolicy)

    - [`asyncio.WindowsSelectorEventLoopPolicy`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.WindowsSelectorEventLoopPolicy)

    - [`asyncio.WindowsProactorEventLoopPolicy`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.WindowsProactorEventLoopPolicy)

    - [`asyncio.get_event_loop_policy()`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.get_event_loop_policy)

    - [`asyncio.set_event_loop_policy()`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.set_event_loop_policy)

Callers should turn to [`asyncio.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run) or [`asyncio.Runner`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.Runner) paired with *loop_factory* to select whichever event loop implementation they want.

As an illustration, employing [`asyncio.SelectorEventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.SelectorEventLoop) under Windows:

```python
import asyncio

async def main():
    ...

asyncio.run(main(), loop_factory=asyncio.SelectorEventLoop)

```

(Contributed by Kumar Aditya in [gh-127949](https://github.com/python/cpython/issues/127949).)

- [`builtins`](https://docs.python.org/3.14/library/builtins.html#module-builtins):

  - Bitwise inversion applied to boolean types, `~True` or `~False`, has carried a deprecation since Python 3.12, because the outcomes it yields are surprising and unintuitive (`-2` and `-1`). Reach for `not x` instead when negating a Boolean logically. Should you find yourself needing the bitwise inversion of the backing integer, perform an explicit conversion to `int` (`~int(x)`).

- [`functools`](https://docs.python.org/3.14/library/functools.html#module-functools):

  -

Invoking the Python build of [`functools.reduce()`](https://docs.python.org/3.14/library/functools.html#functools.reduce) with *function* or *sequence* passed as keyword arguments has carried a deprecation since Python 3.14.

- [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging):

Custom logging handlers that rely on the *strm* argument now carry a deprecation, with removal set for Python 3.16. Build your handlers around the *stream* argument in its place. (Contributed by Mariusz Felisiak in [gh-115032](https://github.com/python/cpython/issues/115032).)

- [`mimetypes`](https://docs.python.org/3.14/library/mimetypes.html#module-mimetypes):

  - For [`mimetypes.MimeTypes.add_type()`](https://docs.python.org/3.14/library/mimetypes.html#mimetypes.MimeTypes.add_type), a valid extension either opens with a ?.? or is empty. Extensions lacking a dot now carry a deprecation and will throw a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) in Python 3.16. (Contributed by Hugo van Kemenade in [gh-75223](https://github.com/python/cpython/issues/75223).)

- [`shutil`](https://docs.python.org/3.14/library/shutil.html#module-shutil):

  - The `ExecError` exception has carried a deprecation since Python 3.14. No function within `shutil` has touched it since Python 3.4, and it now serves as an alias for [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

- [`symtable`](https://docs.python.org/3.14/library/symtable.html#module-symtable):

  - A deprecation has covered the [`Class.get_methods`](https://docs.python.org/3.14/library/symtable.html#symtable.Class.get_methods) method ever since Python 3.14.

- [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys):

  - A deprecation has covered the [`_enablelegacywindowsfsencoding()`](https://docs.python.org/3.14/library/sys.html#sys._enablelegacywindowsfsencoding) function ever since Python 3.13. Switch to the [`PYTHONLEGACYWINDOWSFSENCODING`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSFSENCODING) environment variable in its place.

- [`sysconfig`](https://docs.python.org/3.14/library/sysconfig.html#module-sysconfig):

  - A deprecation has covered the `sysconfig.expand_makefile_vars()` function ever since Python 3.14. Lean on the `vars` argument of [`sysconfig.get_paths()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.get_paths) in its place.

- [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile):

  - A deprecation has covered the undocumented and unused `TarFile.tarfile` attribute ever since Python 3.13.

[Subject index](INDEX.md) · [Previous source section](pending-removal-in-python-3-15.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](pending-removal-in-python-3-17.md)
