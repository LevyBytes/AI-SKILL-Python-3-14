# pdb: `pdb.runeval()`, `pdb.runcall()`, `pdb.set_trace()`, `pdb.set_trace_async()`, `pdb.post_mortem()`, `pdb.pm()`, `pdb.set_default_backend()`, `pdb.get_default_backend()`

pdb.runeval(*expression*, *globals=None*, *locals=None*)

Evaluate the *expression* (supplied as a string or a code object) with the debugger in control. On return, `runeval()` hands back the value of the *expression*. Apart from that, this function behaves like `run()`.

 pdb.runcall(*function*, **args*, ***kwds*)

Invoke the *function* (a function or method object, not a string) using the supplied arguments. On return, `runcall()` hands back whatever the function call yielded. The prompt shows up the moment the function is entered.

 pdb.set_trace(***, *header=None*, *commands=None*)

Drop into the debugger at the calling stack frame. This comes in handy for hard-coding a breakpoint at a specific spot in a program, even when the code is not otherwise under debugging (for instance, when an assertion fails). When supplied, *header* is written to the console right before debugging starts. The *commands* argument, when supplied, is a list of commands run as the debugger launches.

Changed in version 3.7: The keyword-only argument *header*.

Changed in version 3.13: `set_trace()` now drops into the debugger at once, instead of waiting for the next line of code to run.

Added in version 3.14: The *commands* argument.

 *awaitable *pdb.set_trace_async(***, *header=None*, *commands=None*)

An async counterpart to `set_trace()`. Call it from within an async function, using [`await`](https://docs.python.org/3.14/reference/expressions.html#await).

```python
async def f():
    await pdb.set_trace_async()

```

[`await`](https://docs.python.org/3.14/reference/expressions.html#await) statements are supported if the debugger is invoked by this function.

Added in version 3.14.

 pdb.post_mortem(*t=None*)

Begin post-mortem debugging on the supplied exception or [traceback object](https://docs.python.org/3.14/reference/datamodel.html#traceback-objects). When nothing is supplied, it falls back on the exception currently being handled, or raises `ValueError` when none exists.

Changed in version 3.13: Support for exception objects was added.

 pdb.pm()

Begin post-mortem debugging on the exception held in [`sys.last_exc`](https://docs.python.org/3.14/library/sys.html#sys.last_exc).

 pdb.set_default_backend(*backend*)

pdb works with two backends: `'settrace'` and `'monitoring'`. Consult [`bdb.Bdb`](https://docs.python.org/3.14/library/bdb.html#bdb.Bdb) for the details. You may choose which backend serves as the default when none is named while creating a `Pdb`. With no backend named, `'settrace'` is the default.

Note

[`breakpoint()`](https://docs.python.org/3.14/library/functions.html#breakpoint) and `set_trace()` are unaffected by this function. Their backend is always `'monitoring'`.

Added in version 3.14.

 pdb.get_default_backend()

Returns the default backend for pdb.

Added in version 3.14.

The `run*` functions along with `set_trace()` act as shortcuts that build a `Pdb` instance and call its identically named method. To reach additional features, you must do that step on your own:

[Subject index](INDEX.md) · [Previous](pdb-run.md) · [Continue](pdb-pdb-class-to-pdb-pdb-set-trace.md) · [Owning module, declaration or section: pdb](pdb-the-python-debugger.md) · [Owning module, declaration or section: Command-line interface](pdb-run.md)
