# Effects of the Python Development Mode — Section introduction and initial examples

### Effects of the Python Development Mode

Switching on the Python Development Mode roughly matches running the command below, though it carries the extra effects laid out afterward:

```python
PYTHONMALLOC=debug PYTHONASYNCIODEBUG=1 python -W default -X faulthandler

```

What the Python Development Mode brings about:

- Adds the `default` [warning filter](https://docs.python.org/3.14/library/warnings.html#describing-warning-filters). These warnings become visible:

  - [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning)

  - [`ImportWarning`](https://docs.python.org/3.14/library/exceptions.html#ImportWarning)

  - [`PendingDeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#PendingDeprecationWarning)

  - [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning)

Under ordinary conditions these warnings get screened out by the default [warning filters](https://docs.python.org/3.14/library/warnings.html#describing-warning-filters).

The effect is the same as supplying the [`-W default`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-W) command line option.

To have warnings raised as errors, apply the [`-W error`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-W) command line option or give the [`PYTHONWARNINGS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONWARNINGS) environment variable the value `error`.

- Sets up debug hooks across the memory allocators so they watch for:

  - Buffer underflow

  - Buffer overflow

  - Memory allocator API violation

  - Unsafe usage of the GIL

Consult the [`PyMem_SetupDebugHooks()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_SetupDebugHooks) C function.

This works as though the [`PYTHONMALLOC`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONMALLOC) environment variable carried the value `debug`.

Should you want the Python Development Mode active yet without those allocator debug hooks, give the [`PYTHONMALLOC`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONMALLOC) environment variable the value `default`.

- Invokes [`faulthandler.enable()`](https://docs.python.org/3.14/library/faulthandler.html#faulthandler.enable) as Python starts so that handlers are wired up for the [`SIGSEGV`](https://docs.python.org/3.14/library/signal.html#signal.SIGSEGV), [`SIGFPE`](https://docs.python.org/3.14/library/signal.html#signal.SIGFPE), [`SIGABRT`](https://docs.python.org/3.14/library/signal.html#signal.SIGABRT), [`SIGBUS`](https://docs.python.org/3.14/library/signal.html#signal.SIGBUS) and [`SIGILL`](https://docs.python.org/3.14/library/signal.html#signal.SIGILL) signals, dumping the Python traceback whenever a crash occurs.

This works as though the [`-X faulthandler`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) command line option were supplied, or the [`PYTHONFAULTHANDLER`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONFAULTHANDLER) environment variable held `1`.

- Switches on [asyncio debug mode](https://docs.python.org/3.14/library/asyncio-dev.html#asyncio-debug-mode). As one example, [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) watches for coroutines left un-awaited and records them in the log.

This works as though the [`PYTHONASYNCIODEBUG`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONASYNCIODEBUG) environment variable held `1`.

- Validates the *encoding* and *errors* arguments across string encode and decode operations. Cases in point: [`open()`](https://docs.python.org/3.14/library/functions.html#open), [`str.encode()`](https://docs.python.org/3.14/library/stdtypes.html#str.encode) and [`bytes.decode()`](https://docs.python.org/3.14/library/stdtypes.html#bytes.decode).

For top performance, the default arrangement only inspects the *errors* argument once the first encode/decode failure happens, and now and then skips the *encoding* argument when the string is empty.

-

[Subject index](INDEX.md) · [Previous](python-development-mode.md) · [Continue](iobase-destructor-close-errors.md)
