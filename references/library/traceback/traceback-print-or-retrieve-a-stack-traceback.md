# traceback — `traceback` — Print or retrieve a stack traceback

### `traceback` — Print or retrieve a stack traceback

**Source code:** [Lib/traceback.py](https://github.com/python/cpython/tree/3.14/Lib/traceback.py)

---

A consistent way to pull out, format, and display the stack traces produced by Python programs is supplied by this module. Because it gives you more control than the default traceback rendering the interpreter performs, you can tailor several characteristics of what gets emitted. The module also offers a helper that records enough detail about an exception so that it can be displayed afterwards, without you having to keep a handle on the exception itself. Given that exceptions may anchor sizeable object graphs, leaning on this helper can yield meaningful gains for memory usage.

Internally the module relies on [traceback objects](https://docs.python.org/3.14/reference/datamodel.html#traceback-objects) — instances of [`types.TracebackType`](https://docs.python.org/3.14/library/types.html#types.TracebackType), which Python stores on the [`__traceback__`](https://docs.python.org/3.14/library/exceptions.html#BaseException.__traceback__) field of every [`BaseException`](https://docs.python.org/3.14/library/exceptions.html#BaseException).

See also

Module [`faulthandler`](https://docs.python.org/3.14/library/faulthandler.html#module-faulthandler)

Dumps Python tracebacks on demand — when a fault hits, when a timeout elapses, or in response to a signal the user sends.

Module [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb)

An interactive debugger that works through the source code of Python programs.

You can think of the module's API as falling into two groups:

- A set of module-level functions covering the essentials, handy when you want to poke at exceptions and tracebacks interactively.

- The `TracebackException` class together with its companion classes `StackSummary` and `FrameSummary`. This pairing grants greater control over the produced output along with a way to retain everything needed for formatting at a later time, all without keeping handles on the underlying exception and traceback objects.

Added in version 3.13: By default the output now carries color, which you may [control using environment variables](https://docs.python.org/3.14/using/cmdline.html#using-on-controlling-color).

[Subject index](INDEX.md) · [Continue](traceback-print-tb-to-traceback-format-exception-only.md)
