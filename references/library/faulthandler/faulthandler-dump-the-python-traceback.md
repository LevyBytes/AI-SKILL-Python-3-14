# faulthandler`faulthandler` - Dump the Python traceback

### `faulthandler` - Dump the Python traceback

Added in version 3.3.

---

The functions in this module let you emit Python tracebacks deliberately — upon a fault, once a timeout elapses, or in response to a user signal. Invoking `faulthandler.enable()` installs fault handlers covering the [`SIGSEGV`](https://docs.python.org/3.14/library/signal.html#signal.SIGSEGV), [`SIGFPE`](https://docs.python.org/3.14/library/signal.html#signal.SIGFPE), [`SIGABRT`](https://docs.python.org/3.14/library/signal.html#signal.SIGABRT), [`SIGBUS`](https://docs.python.org/3.14/library/signal.html#signal.SIGBUS), and [`SIGILL`](https://docs.python.org/3.14/library/signal.html#signal.SIGILL) signals. Alternatively, they can be turned on during startup, either by defining the [`PYTHONFAULTHANDLER`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONFAULTHANDLER) environment variable or by supplying the [`-X`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) `faulthandler` command line option.

This fault handler interoperates with platform fault handlers such as Apport or the Windows fault handler. When the `sigaltstack()` function is present, the module relies on a separate stack for its signal handlers. That arrangement lets it produce the traceback even during a stack overflow.

Since the fault handler runs in catastrophic situations, it is restricted to signal-safe functions (for instance, it cannot perform heap allocations). Owing to that restriction, the traceback output is sparse relative to ordinary Python tracebacks:

- Encoding accepts ASCII alone. The `backslashreplace` error handler handles the encoding step.

- No string may exceed 500 characters.

- Output shows only the filename, function name, and line number. (no source code)

- A ceiling of 100 frames and 100 threads applies.

- Ordering runs backwards: the latest call appears at the top.

The Python traceback goes to [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr) by default. Programs need to run inside the terminal for tracebacks to be visible. As an alternative, you may hand a log file to `faulthandler.enable()`.

Because the module is written in C, it can emit tracebacks during a crash or while Python sits deadlocked.

When [Python Development Mode](https://docs.python.org/3.14/library/devmode.html#devmode) is active, it invokes `faulthandler.enable()` as Python starts up.

See also

Module [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb)

Interactive source code debugger for Python programs.

Module [`traceback`](https://docs.python.org/3.14/library/traceback.html#module-traceback)

Standard interface to extract, format and print stack traces of Python programs.

[Subject index](INDEX.md) · [Previous](dump-the-python-traceback.md) · [Continue](faulthandler-dump-traceback.md)
