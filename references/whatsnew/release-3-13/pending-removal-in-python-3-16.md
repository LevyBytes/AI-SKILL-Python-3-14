# What's New In Python 3.13 / Pending removal in Python 3.16 — array, asyncio, asyncio-eventloop, asyncio-policy, asyncio-runner, builtins, importlib, inspect

### Pending removal in Python 3.16

- The import system:

  - Assigning [`__loader__`](https://docs.python.org/3.14/reference/datamodel.html#module.__loader__) on a module without also assigning [`__spec__.loader`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec.loader) is now deprecated. Come Python 3.16, neither the import system nor the standard library will set or consult `__loader__` any longer.

- [`array`](https://docs.python.org/3.14/library/array.html#module-array):

  - Documentation has flagged the `'u'` format code (`wchar_t`) as deprecated since Python 3.3, and the runtime has done so since Python 3.13. Use the `'w'` format code ([`Py_UCS4`](https://docs.python.org/3.14/c-api/unicode.html#c.Py_UCS4)) for Unicode characters in its place.

- [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio):

  - `asyncio.iscoroutinefunction()` is now deprecated and leaves in Python 3.16; turn to [`inspect.iscoroutinefunction()`](https://docs.python.org/3.14/library/inspect.html#inspect.iscoroutinefunction) instead. (Contributed by Jiahao Li and Kumar Aditya in [gh-122875](https://github.com/python/cpython/issues/122875).)

  - The [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) policy system is now deprecated and leaves in Python 3.16. Specifically, these classes and functions are deprecated:

    - [`asyncio.AbstractEventLoopPolicy`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.AbstractEventLoopPolicy)

    - [`asyncio.DefaultEventLoopPolicy`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.DefaultEventLoopPolicy)

    - [`asyncio.WindowsSelectorEventLoopPolicy`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.WindowsSelectorEventLoopPolicy)

    - [`asyncio.WindowsProactorEventLoopPolicy`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.WindowsProactorEventLoopPolicy)

    - [`asyncio.get_event_loop_policy()`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.get_event_loop_policy)

    - [`asyncio.set_event_loop_policy()`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.set_event_loop_policy)

To select the event loop implementation you want, lean on [`asyncio.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run) or [`asyncio.Runner`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.Runner) together with *loop_factory*.

As an illustration, to run [`asyncio.SelectorEventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.SelectorEventLoop) on Windows:

```python
import asyncio

async def main():
    ...

asyncio.run(main(), loop_factory=asyncio.SelectorEventLoop)

```

(Contributed by Kumar Aditya in [gh-127949](https://github.com/python/cpython/issues/127949).)

- [`builtins`](https://docs.python.org/3.14/library/builtins.html#module-builtins):

  -

> Whatsnew reference. Reworded prose; identifiers retained exactly.

Applying bitwise inversion to a boolean, `~True` or `~False`, has carried a deprecation since Python 3.12, because the outcome (`-2` and `-1`) tends to confuse and mislead. For ordinary logical negation of a Boolean, reach for `not x`. On the uncommon occasion that the bitwise complement of the backing integer is genuinely wanted, cast to `int` first (`~int(x)`).

- [`functools`](https://docs.python.org/3.14/library/functools.html#module-functools):

  - Invoking the pure-Python form of [`functools.reduce()`](https://docs.python.org/3.14/library/functools.html#functools.reduce) while supplying *function* or *sequence* through keyword arguments carries a deprecation as of Python 3.14.

- [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging):

Handlers that take the *strm* argument are deprecated and slated to disappear in Python 3.16. Build your handlers around the *stream* argument in their place. (Contributed by Mariusz Felisiak in [gh-115032](https://github.com/python/cpython/issues/115032).)

- [`mimetypes`](https://docs.python.org/3.14/library/mimetypes.html#module-mimetypes):

  - For [`mimetypes.MimeTypes.add_type()`](https://docs.python.org/3.14/library/mimetypes.html#mimetypes.MimeTypes.add_type), a valid extension either begins with a "." or is the empty string. Extensions lacking the leading dot carry a deprecation and will trigger a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) once Python 3.16 arrives. (Contributed by Hugo van Kemenade in [gh-75223](https://github.com/python/cpython/issues/75223).)

- [`shutil`](https://docs.python.org/3.14/library/shutil.html#module-shutil):

  - As of Python 3.14, the `ExecError` exception carries a deprecation. No function within `shutil` has relied on it since Python 3.4, and it now stands as an alias for [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

- [`symtable`](https://docs.python.org/3.14/library/symtable.html#module-symtable):

  - Starting with Python 3.14, the [`Class.get_methods`](https://docs.python.org/3.14/library/symtable.html#symtable.Class.get_methods) method carries a deprecation.

- [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys):

  - Since Python 3.13 the [`_enablelegacywindowsfsencoding()`](https://docs.python.org/3.14/library/sys.html#sys._enablelegacywindowsfsencoding) function has been deprecated. Reach for the [`PYTHONLEGACYWINDOWSFSENCODING`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSFSENCODING) environment variable in its place.

- [`sysconfig`](https://docs.python.org/3.14/library/sysconfig.html#module-sysconfig):

  - The `sysconfig.expand_makefile_vars()` function carries a deprecation as of Python 3.14. Lean on the `vars` argument of [`sysconfig.get_paths()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.get_paths) instead.

- [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile):

  - Since Python 3.13, the unused and undocumented `TarFile.tarfile` attribute has carried a deprecation.

[Subject index](INDEX.md) · [Previous source section](pending-removal-in-python-3-15.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](pending-removal-in-python-3-17.md)
