# What's New In Python 3.3 / faulthandler — faulthandler, signal

### New Modules

### faulthandler

[`faulthandler`](https://docs.python.org/3.14/library/faulthandler.html#module-faulthandler), this new debugging module, holds functions that explicitly dump Python tracebacks — whether on a fault (some crash such as a segmentation fault), once a timeout elapses, or upon a user signal. Invoke [`faulthandler.enable()`](https://docs.python.org/3.14/library/faulthandler.html#faulthandler.enable) to put fault handlers in place for the [`SIGSEGV`](https://docs.python.org/3.14/library/signal.html#signal.SIGSEGV), [`SIGFPE`](https://docs.python.org/3.14/library/signal.html#signal.SIGFPE), [`SIGABRT`](https://docs.python.org/3.14/library/signal.html#signal.SIGABRT), [`SIGBUS`](https://docs.python.org/3.14/library/signal.html#signal.SIGBUS), and [`SIGILL`](https://docs.python.org/3.14/library/signal.html#signal.SIGILL) signals. Turning them on at startup is also possible, either by defining the [`PYTHONFAULTHANDLER`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONFAULTHANDLER) environment variable or by supplying the [`-X`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) `faulthandler` command line option.

Example of a segmentation fault on Linux:

```shell
$ python -q -X faulthandler
>>> import ctypes
>>> ctypes.string_at(0)
Fatal Python error: Segmentation fault

Current thread 0x00007fb899f39700:
  File "/home/python/cpython/Lib/ctypes/__init__.py", line 486 in string_at
  File "<stdin>", line 1 in <module>
Segmentation fault

```

[Subject index](INDEX.md) · [Previous source section](builtin-functions-and-types.md) · [Next source section](ipaddress.md) · [Release/subject declaration](summary-release-highlights.md)
