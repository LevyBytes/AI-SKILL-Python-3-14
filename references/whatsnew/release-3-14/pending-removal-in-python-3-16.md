# What's new in Python 3.14 / Pending removal in Python 3.16 — array, asyncio, asyncio-eventloop, asyncio-policy, asyncio-runner, builtins, functools, importlib, inspect

### Pending removal in Python 3.16

- The import system:

  - A deprecation applies when [`__loader__`](https://docs.python.org/3.14/reference/datamodel.html#module.__loader__) gets set on a module yet [`__spec__.loader`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec.loader) does not. As of Python 3.16, the import system and the standard library will no longer set or consult `__loader__`.

- [`array`](https://docs.python.org/3.14/library/array.html#module-array):

  - The `'u'` format code (`wchar_t`) has carried a documentation deprecation since Python 3.3 and a runtime one since Python 3.13. For Unicode characters, switch to the `'w'` format code ([`Py_UCS4`](https://docs.python.org/3.14/c-api/unicode.html#c.Py_UCS4)).

- [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio):

  - A deprecation covers `asyncio.iscoroutinefunction()`, with removal slated for Python 3.16; switch to [`inspect.iscoroutinefunction()`](https://docs.python.org/3.14/library/inspect.html#inspect.iscoroutinefunction). (Contributed by Jiahao Li and Kumar Aditya in [gh-122875](https://github.com/python/cpython/issues/122875).)

  - A deprecation covers the [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) policy system, headed for removal in Python 3.16. Specifically, these classes plus functions are deprecated:

    - [`asyncio.AbstractEventLoopPolicy`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.AbstractEventLoopPolicy)

    - [`asyncio.DefaultEventLoopPolicy`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.DefaultEventLoopPolicy)

    - [`asyncio.WindowsSelectorEventLoopPolicy`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.WindowsSelectorEventLoopPolicy)

    - [`asyncio.WindowsProactorEventLoopPolicy`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.WindowsProactorEventLoopPolicy)

    - [`asyncio.get_event_loop_policy()`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.get_event_loop_policy)

    - [`asyncio.set_event_loop_policy()`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.set_event_loop_policy)

To select the event loop implementation you want, reach for [`asyncio.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run) or [`asyncio.Runner`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.Runner) together with *loop_factory*.

As an illustration, here is how you pick [`asyncio.SelectorEventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.SelectorEventLoop) under Windows:

```python
import asyncio

async def main():
    ...

asyncio.run(main(), loop_factory=asyncio.SelectorEventLoop)

```

(Contributed by Kumar Aditya in [gh-127949](https://github.com/python/cpython/issues/127949).)

- [`builtins`](https://docs.python.org/3.14/library/builtins.html#module-builtins):

  - Bitwise inversion against boolean values, `~True` or `~False`, has carried a deprecation since Python 3.12, since the outcomes (`-2` and `-1`) feel startling and counterintuitive. For logical negation of a Boolean, write `not x`. On the rare occasion you genuinely want the bitwise inversion of the backing integer, cast to `int` first (`~int(x)`).

- [`functools`](https://docs.python.org/3.14/library/functools.html#module-functools):

  -

Invoking the Python build of [`functools.reduce()`](https://docs.python.org/3.14/library/functools.html#functools.reduce) while supplying *function* or *sequence* as keyword arguments has carried a deprecation since Python 3.14.

- [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging):

A deprecation covers custom logging handlers that rely on the *strm* argument, with removal targeted for Python 3.16. Build your handlers around the *stream* argument instead. (Contributed by Mariusz Felisiak in [gh-115032](https://github.com/python/cpython/issues/115032).)

- [`mimetypes`](https://docs.python.org/3.14/library/mimetypes.html#module-mimetypes):

  -

For [`mimetypes.MimeTypes.add_type()`](https://docs.python.org/3.14/library/mimetypes.html#mimetypes.MimeTypes.add_type), an extension is only valid when it begins with a ?.? or is left empty. Extensions lacking the leading dot are now deprecated and, come Python 3.16, will trigger a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError). (Contributed by Hugo van Kemenade in [gh-75223](https://github.com/python/cpython/issues/75223).)

- [`shutil`](https://docs.python.org/3.14/library/shutil.html#module-shutil):

  - Since Python 3.14 the `ExecError` exception carries a deprecation. No `shutil` function has relied on it since Python 3.4, and it now stands as an alias of [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

- [`symtable`](https://docs.python.org/3.14/library/symtable.html#module-symtable):

  - Starting with Python 3.14, the [`Class.get_methods`](https://docs.python.org/3.14/library/symtable.html#symtable.Class.get_methods) method carries a deprecation.

- [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys):

  - Carrying a deprecation since Python 3.13, the [`_enablelegacywindowsfsencoding()`](https://docs.python.org/3.14/library/sys.html#sys._enablelegacywindowsfsencoding) function should give way to the [`PYTHONLEGACYWINDOWSFSENCODING`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSFSENCODING) environment variable.

- [`sysconfig`](https://docs.python.org/3.14/library/sysconfig.html#module-sysconfig):

  - Deprecated as of Python 3.14, the `sysconfig.expand_makefile_vars()` function should be replaced by passing the `vars` argument to [`sysconfig.get_paths()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.get_paths).

- [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile):

  - Since Python 3.13 the `TarFile.tarfile` attribute, which was undocumented and unused, carries a deprecation.

[Subject index](INDEX.md) · [Previous source section](pending-removal-in-python-3-15.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](pending-removal-in-python-3-17.md)
