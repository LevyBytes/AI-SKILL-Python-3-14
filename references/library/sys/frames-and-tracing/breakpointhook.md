# sys.breakpointhook

sys.breakpointhook()

The built-in [`breakpoint()`](https://docs.python.org/3.14/library/functions.html#breakpoint) invokes this hook function. Out of the box it lands you inside the [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) debugger, yet you may point it at any other function to pick which debugger is used.

What this function's signature looks like hinges on what it ends up calling. For instance, the default binding (such as `pdb.set_trace()`) expects no arguments, but you could bind it to a function that wants extra arguments (positional, keyword, or both). The built-in `breakpoint()` function relays its `*args` and `**kws` directly onward. Whatever `breakpointhooks()` returns becomes the return value of `breakpoint()`.

The default implementation begins by checking the environment variable [`PYTHONBREAKPOINT`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONBREAKPOINT). When that holds `"0"`, the function returns at once — that is, it does nothing. When the environment variable is unset, or set to the empty string, `pdb.set_trace()` runs. Otherwise the variable is expected to name a function to call, written in Python's dotted-import style, for example `package.subpackage.module.function`. Here `package.subpackage.module` is imported, and the module that results must expose a callable named `function()`. That callable runs with `*args` and `**kws` passed in, and whatever `function()` gives back, `sys.breakpointhook()` returns to the built-in [`breakpoint()`](https://docs.python.org/3.14/library/functions.html#breakpoint) function.

Be aware that should anything fail while importing the callable that [`PYTHONBREAKPOINT`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONBREAKPOINT) names, a [`RuntimeWarning`](https://docs.python.org/3.14/library/exceptions.html#RuntimeWarning) is emitted and the breakpoint is skipped.

Be aware too that when `sys.breakpointhook()` has been replaced programmatically, [`PYTHONBREAKPOINT`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONBREAKPOINT) is *not* checked.

Added in version 3.7.

[API family](INDEX.md) · [sys context index](../INDEX.md).
