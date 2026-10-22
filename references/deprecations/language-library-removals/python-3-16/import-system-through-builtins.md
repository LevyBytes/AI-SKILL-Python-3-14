# Language and standard library pending removal in 3.16: import system; array; asyncio; builtins

### Pending removal in Python 3.16

- The import system:

  - Assigning [`__loader__`](https://docs.python.org/3.14/reference/datamodel.html#module.__loader__) on a module without also assigning [`__spec__.loader`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec.loader) is now deprecated. Beginning with Python 3.16, neither the import machinery nor the standard library will set or consult `__loader__`.

- [`array`](https://docs.python.org/3.14/library/array.html#module-array):

  - The `'u'` format code (`wchar_t`) has carried a documentation deprecation since Python 3.3 and a runtime one since Python 3.13. For Unicode characters, switch to the `'w'` format code ([`Py_UCS4`](https://docs.python.org/3.14/c-api/unicode.html#c.Py_UCS4)).

- [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio):

  - `asyncio.iscoroutinefunction()` is deprecated and slated for removal in Python 3.16; reach for [`inspect.iscoroutinefunction()`](https://docs.python.org/3.14/library/inspect.html#inspect.iscoroutinefunction) instead. (Contributed by Jiahao Li and Kumar Aditya in [gh-122875](https://github.com/python/cpython/issues/122875).)

  - The [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) policy system is deprecated and slated for removal in Python 3.16. Specifically, these classes and functions are deprecated:

    - [`asyncio.AbstractEventLoopPolicy`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.AbstractEventLoopPolicy)

    - [`asyncio.DefaultEventLoopPolicy`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.DefaultEventLoopPolicy)

    - [`asyncio.WindowsSelectorEventLoopPolicy`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.WindowsSelectorEventLoopPolicy)

    - [`asyncio.WindowsProactorEventLoopPolicy`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.WindowsProactorEventLoopPolicy)

    - [`asyncio.get_event_loop_policy()`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.get_event_loop_policy)

    - [`asyncio.set_event_loop_policy()`](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio.set_event_loop_policy)

To select the event loop implementation you want, pair [`asyncio.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run) or [`asyncio.Runner`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.Runner) with *loop_factory*.

As an illustration, running [`asyncio.SelectorEventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.SelectorEventLoop) on Windows looks like this:

```python
import asyncio

async def main():
    ...

asyncio.run(main(), loop_factory=asyncio.SelectorEventLoop)

```

(Contributed by Kumar Aditya in [gh-127949](https://github.com/python/cpython/issues/127949).)

- [`builtins`](https://docs.python.org/3.14/library/builtins.html#module-builtins):

  - Bitwise inversion of boolean values, `~True` or `~False`, has been deprecated since Python 3.12 because the outcomes (`-2` and `-1`) are surprising and counterintuitive. For logical negation of a Boolean, write `not x`. On the rare occasion you actually want the bitwise inversion of the backing integer, cast to `int` first (`~int(x)`).

[Subject index](INDEX.md) · [Previous source section](../python-3-15/types-through-zipimport.md) · [Next source section](functools-through-tarfile.md) · [Previous source section](../python-3-15/typing-wave-zipimport.md)
