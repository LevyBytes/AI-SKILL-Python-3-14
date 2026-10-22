# bdb — `bdb` — Debugger framework

format_stack_entry(*frame_lineno*, *lprefix=': '*)

Return a string holding information about a stack entry, which is a `(frame, lineno)` tuple. The returned string contains:

- The canonical filename which contains the frame.

- The function name or `"<lambda>"`.

- The input arguments.

- The return value.

- The line of code (if it exists).

The two methods below can be invoked by clients to put a debugger to work debugging a [statement](https://docs.python.org/3.14/glossary.html#term-statement) supplied as a string.

 run(*cmd*, *globals=None*, *locals=None*)

Debug a statement run by way of the [`exec()`](https://docs.python.org/3.14/library/functions.html#exec) function. The default for *globals* is `__main__.__dict__`, and the default for *locals* is *globals*.

 runeval(*expr*, *globals=None*, *locals=None*)

Debug an expression run by way of the [`eval()`](https://docs.python.org/3.14/library/functions.html#eval) function. Here *globals* and *locals* carry the same meaning they do in `run()`.

 runctx(*cmd*, *globals*, *locals*)

For backwards compatibility. Calls the `run()` method.

 runcall(*func*, */*, **args*, ***kwds*)

Debug a single function call, and return its result.

Lastly, the module defines the following functions:

[Subject index](INDEX.md) · [Previous](bdb-bdb-set-continue-to-bdb-bdb-get-stack.md) · [Continue](bdb-checkfuncname-to-bdb-set-trace.md) · [Owning module, declaration or section: bdb](bdb-bdbquit.md) · [Owning module, declaration or section: bdb.Bdb](bdb-bdb-class-to-bdb-bdb-dispatch-line.md)
