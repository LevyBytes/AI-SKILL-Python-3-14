# sys.excepthook

sys.excepthook(*type*, *value*, *traceback*)

This function writes out the supplied traceback and exception to `sys.stderr`.

Should an exception that is not [`SystemExit`](https://docs.python.org/3.14/library/exceptions.html#SystemExit) be raised and go uncaught, the interpreter calls `sys.excepthook` with three arguments: the exception class, the exception instance, and a traceback object. Within an interactive session this fires right before control returns to the prompt; within a Python program it fires right before the program exits. You can customize how such top-level exceptions are dealt with by assigning a different three-argument function to `sys.excepthook`.

Whenever an uncaught exception arises, an auditing event `sys.excepthook` fires carrying the arguments `hook`, `type`, `value`, `traceback`. Where no hook was ever set, `hook` may come through as `None`. Should any hook throw an exception that descends from [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError), the call into that hook is suppressed. In every other case, the audit hook's exception is flagged as unraisable and then `sys.excepthook` runs.

See also

The `sys.unraisablehook()` function deals with unraisable exceptions, while the [`threading.excepthook()`](https://docs.python.org/3.14/library/threading.html#threading.excepthook) function deals with exceptions raised by [`threading.Thread.run()`](https://docs.python.org/3.14/library/threading.html#threading.Thread.run).

[API family](INDEX.md) · [sys context index](../INDEX.md).
