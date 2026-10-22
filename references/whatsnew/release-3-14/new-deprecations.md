# What's new in Python 3.14 / New deprecations — argparse, asyncio, asyncio-eventloop, asyncio-policy, asyncio-runner, codecs, ctypes, inspect

### Deprecated

### New deprecations

- Handing a complex number as either the *real* or *imag* argument to the [`complex()`](https://docs.python.org/3.14/library/functions.html#complex) constructor now carries a deprecation; a complex value belongs only as one lone positional argument. (Contributed by Serhiy Storchaka in [gh-109218](https://github.com/python/cpython/issues/109218).)

- [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse):

  - Handing the undocumented keyword argument *prefix_chars* into the [`add_argument_group()`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser.add_argument_group) method now carries a deprecation. (Contributed by Savannah Ostrowski in [gh-125563](https://github.com/python/cpython/issues/125563).)

  - A deprecation now applies to the [`argparse.FileType`](https://docs.python.org/3.14/library/argparse.html#argparse.FileType) type converter. Tasks tied to resource management belong downstream, once parsing of the arguments has finished. (Contributed by Serhiy Storchaka in [gh-58032](https://github.com/python/cpython/issues/58032).)

- [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio):

  - A deprecation now covers `asyncio.iscoroutinefunction()`, with removal slated for Python 3.16; switch to [`inspect.iscoroutinefunction()`](https://docs.python.org/3.14/library/inspect.html#inspect.iscoroutinefunction). (Contributed by Jiahao Li and Kumar Aditya in [gh-122875](https://github.com/python/cpython/issues/122875).)

  - A deprecation now covers the [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) policy system, headed for removal in Python 3.16. Specifically, these classes plus functions are deprecated:

    - [`asyncio.AbstractEventLoopPolicy`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.AbstractEventLoopPolicy)

    - [`asyncio.DefaultEventLoopPolicy`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.DefaultEventLoopPolicy)

    - [`asyncio.WindowsSelectorEventLoopPolicy`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.WindowsSelectorEventLoopPolicy)

    - [`asyncio.WindowsProactorEventLoopPolicy`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.WindowsProactorEventLoopPolicy)

    - [`asyncio.get_event_loop_policy()`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.get_event_loop_policy)

    - [`asyncio.set_event_loop_policy()`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.set_event_loop_policy)

To select the event loop implementation you want, reach for [`asyncio.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run) or [`asyncio.Runner`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.Runner) together with the *loop_factory* argument.

As an illustration, here is how you pick [`asyncio.SelectorEventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.SelectorEventLoop) under Windows:

```python
import asyncio

async def main():
    ...

asyncio.run(main(), loop_factory=asyncio.SelectorEventLoop)

```

(Contributed by Kumar Aditya in [gh-127949](https://github.com/python/cpython/issues/127949).)

- [`codecs`](https://docs.python.org/3.14/library/codecs.html#module-codecs): A deprecation now applies to the [`codecs.open()`](https://docs.python.org/3.14/library/codecs.html#codecs.open) function, which a later Python release will drop. Reach for [`open()`](https://docs.python.org/3.14/library/functions.html#open) instead. (Contributed by Inada Naoki in [gh-133036](https://github.com/python/cpython/issues/133036).)

- [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes):

  - Away from Windows, assigning [`Structure._pack_`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Structure._pack_) so an MSVC-style default memory layout applies now carries a deprecation; prefer assigning [`Structure._layout_`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Structure._layout_) to `'ms'`. Removal lands in Python 3.19. (Contributed by Petr Viktorin in [gh-131747](https://github.com/python/cpython/issues/131747).)

- Invoking [`ctypes.POINTER()`](https://docs.python.org/3.14/library/ctypes.html#ctypes.POINTER) against a string now carries a deprecation. Reach for [incomplete types](https://docs.python.org/3.14/library/ctypes.html#ctypes-incomplete-types) when a structure references itself. The internal `ctypes._pointer_type_cache` is deprecated too. Consult `ctypes.POINTER()` for the revised implementation notes. (Contributed by Sergey Myrianov in [gh-100926](https://github.com/python/cpython/issues/100926).)

- [`functools`](https://docs.python.org/3.14/library/functools.html#module-functools): Invoking the Python build of [`functools.reduce()`](https://docs.python.org/3.14/library/functools.html#functools.reduce) while supplying *function* or *sequence* as keyword arguments now carries a deprecation; those parameters turn positional-only as of Python 3.16. (Contributed by Kirill Podoprigora in [gh-121676](https://github.com/python/cpython/issues/121676).)

- [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging): A deprecation now covers custom logging handlers that rely on the *strm* argument, with removal targeted for Python 3.16. Build your handlers around the *stream* argument instead. (Contributed by Mariusz Felisiak in [gh-115032](https://github.com/python/cpython/issues/115032).)

- [`mimetypes`](https://docs.python.org/3.14/library/mimetypes.html#module-mimetypes): For [`mimetypes.MimeTypes.add_type()`](https://docs.python.org/3.14/library/mimetypes.html#mimetypes.MimeTypes.add_type), a valid extension is either blank or begins with ".". Extensions lacking a dot now carry a deprecation and will trigger a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) as of Python 3.16. (Contributed by Hugo van Kemenade in [gh-75223](https://github.com/python/cpython/issues/75223).)

- `nturl2path`: A deprecation now covers this whole module. Reach instead for [`urllib.request.url2pathname()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.url2pathname) plus [`pathname2url()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.pathname2url). (Contributed by Barney Gale in [gh-125866](https://github.com/python/cpython/issues/125866).)

- [`os`](https://docs.python.org/3.14/library/os.html#module-os): The [`os.popen()`](https://docs.python.org/3.14/library/os.html#os.popen) plus [`os.spawn*`](https://docs.python.org/3.14/library/os.html#os.spawnl) functions are now [soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated). Fresh code should steer clear of them. The recommended choice is the [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module. (Contributed by Victor Stinner in [gh-120743](https://github.com/python/cpython/issues/120743).)

- [`pathlib`](https://docs.python.org/3.14/library/pathlib.html#module-pathlib): A deprecation now covers `pathlib.PurePath.as_uri()`, headed for removal in Python 3.19. Reach for [`pathlib.Path.as_uri()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.as_uri) instead. (Contributed by Barney Gale in [gh-123599](https://github.com/python/cpython/issues/123599).)

- [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb): The undocumented `pdb.Pdb.curframe_locals` attribute is now a deprecated read-only property, slated to disappear in a later Python release. Thanks to the low overhead dynamic frame locals access introduced for Python 3.13 via [**PEP 667**](https://peps.python.org/pep-0667/), the cached frame locals reference this attribute once held is no longer required. From Python 3.13 onward, derived debuggers ought to reach `pdb.Pdb.curframe.f_locals` straight away. (Contributed by Tian Gao in [gh-124369](https://github.com/python/cpython/issues/124369) and [gh-125951](https://github.com/python/cpython/issues/125951).)

- [`symtable`](https://docs.python.org/3.14/library/symtable.html#module-symtable): Owing to little interest, [`symtable.Class.get_methods()`](https://docs.python.org/3.14/library/symtable.html#symtable.Class.get_methods) now carries a deprecation, slated for removal in Python 3.16. (Contributed by Bénédikt Tran in [gh-119698](https://github.com/python/cpython/issues/119698).)

- [`tkinter`](https://docs.python.org/3.14/library/tkinter.html#module-tkinter): A deprecation now covers the `tkinter.Variable` methods `trace_variable()`, `trace_vdelete()` and `trace_vinfo()`. Reach for `trace_add()`, `trace_remove()` and `trace_info()` in their place. (Contributed by Serhiy Storchaka in [gh-120220](https://github.com/python/cpython/issues/120220).)

- [`urllib.parse`](https://docs.python.org/3.14/library/urllib.parse.html#module-urllib.parse): Inside [`parse_qsl()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.parse_qsl) and [`parse_qs()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.parse_qs), tolerating objects that are falsy (such as `0` and `[]`) — apart from empty strings, bytes-like objects, and `None` — now carries a deprecation. (Contributed by Serhiy Storchaka in [gh-116897](https://github.com/python/cpython/issues/116897).)

[Subject index](INDEX.md) · [Previous source section](urllib.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](pending-removal-in-python-3-15.md)
