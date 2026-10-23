# What's New In Python 3.10 / Changes in the Python API - asyncio, asyncio-api-index, asyncio-task, atexit, collections.abc, socket, traceback, types, typing

### Changes in the Python API

- Within the [`traceback`](https://docs.python.org/3.14/library/traceback.html#module-traceback) module, the *etype* parameter on [`format_exception()`](https://docs.python.org/3.14/library/traceback.html#traceback.format_exception), [`format_exception_only()`](https://docs.python.org/3.14/library/traceback.html#traceback.format_exception_only), and [`print_exception()`](https://docs.python.org/3.14/library/traceback.html#traceback.print_exception) has been renamed *exc*. (Contributed by Zackery Spytz and Matthias Bussonnier in [bpo-26389](https://bugs.python.org/issue?@action=redirect&bpo=26389).)

- [`atexit`](https://docs.python.org/3.14/library/atexit.html#module-atexit): When Python shuts down, a failing callback that was added through [`atexit.register()`](https://docs.python.org/3.14/library/atexit.html#atexit.register) now has its exception logged. Earlier, only certain exceptions reached the log and the final one was always dropped without a trace. (Contributed by Victor Stinner in [bpo-42639](https://bugs.python.org/issue?@action=redirect&bpo=42639).)

- The [`collections.abc.Callable`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Callable) generic now collapses its type parameters the way [`typing.Callable`](https://docs.python.org/3.14/library/typing.html#typing.Callable) already does. As a result, `collections.abc.Callable[[int, str], str]` ends up with `__args__` equal to `(int, str, str)`, where it used to be `([int, str], str)`. Any code that reads those arguments through [`typing.get_args()`](https://docs.python.org/3.14/library/typing.html#typing.get_args) or `__args__` has to adapt. On top of that, parameterizing `collections.abc.Callable` in invalid ways may now throw [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) where Python 3.9 stayed quiet. (Contributed by Ken Jin in [bpo-42195](https://bugs.python.org/issue?@action=redirect&bpo=42195).)

- If the supplied argument exceeds a 16-bit unsigned integer, [`socket.htons()`](https://docs.python.org/3.14/library/socket.html#socket.htons) and [`socket.ntohs()`](https://docs.python.org/3.14/library/socket.html#socket.ntohs) now throw [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) rather than the old [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). (Contributed by Erlend E. Aasland in [bpo-42393](https://bugs.python.org/issue?@action=redirect&bpo=42393).)

- After its Python 3.8 deprecation, the `loop` parameter has been taken out of most of [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio)'s [high-level API](https://docs.python.org/3.14/library/asyncio-api-index.html).

A coroutine written today along these lines:

```python
async def foo(loop):
    await asyncio.sleep(1, loop=loop)

```

Ought to become this:

```python
async def foo():
    await asyncio.sleep(1)

```

When `foo()` was deliberately built *not* to run inside the current thread's running event loop (say, it runs in some other thread's event loop), think about using [`asyncio.run_coroutine_threadsafe()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.run_coroutine_threadsafe) instead.

(Contributed by Yurii Karabas, Andrew Svetlov, Yury Selivanov and Kyle Stanley in [bpo-42392](https://bugs.python.org/issue?@action=redirect&bpo=42392).)

- If the *globals* dictionary lacks a `"__builtins__"` key, the [`types.FunctionType`](https://docs.python.org/3.14/library/types.html#types.FunctionType) constructor now picks up the current builtins instead of falling back on `{"None": None}` — the same treatment [`eval()`](https://docs.python.org/3.14/library/functions.html#eval) and [`exec()`](https://docs.python.org/3.14/library/functions.html#exec) give. Writing a function with `def function(...): ...` is unaffected, since that form offers no way to override globals: it too picks up the current builtins. (Contributed by Victor Stinner in [bpo-42990](https://bugs.python.org/issue?@action=redirect&bpo=42990).)

[Subject index](INDEX.md) · [Previous source section](changes-in-the-python-syntax.md) · [Next source section](porting-to-python-3-10-changes-in-the-c-api.md) · [Release/subject declaration](summary-release-highlights.md)
