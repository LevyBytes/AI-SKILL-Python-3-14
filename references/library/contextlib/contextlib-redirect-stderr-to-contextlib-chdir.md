# contextlib: `contextlib.redirect_stderr()`, `contextlib.chdir()`

contextlib.redirect_stderr(*new_target*)

Comparable to `redirect_stdout()`, but it routes [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr) toward another file or file-like object.

You can use this context manager reentrantly.

Added in version 3.5.

 contextlib.chdir(*path*)

A context manager (not parallel-safe) for switching the current working directory. Since it mutates a global piece of state — the working directory — it doesn't belong in most threaded or async settings. Nor does it fit most non-linear execution flows, such as generators, where execution is briefly handed off; unless you deliberately intend it, refrain from yielding while this context manager is active.

It amounts to a thin wrapper over [`chdir()`](https://docs.python.org/3.14/library/os.html#os.chdir): on entry it switches the current working directory and on exit it puts the previous one back.

You can use this context manager reentrantly.

Added in version 3.11.

[Subject index](INDEX.md) · [Previous](contextlib-suppress-to-contextlib-redirect-stdout.md) · [Continue](contextlib-contextdecorator-class.md) · [Owning module, declaration or section: contextlib](contextlib-utilities-for-with-statement-contexts.md) · [Owning module, declaration or section: Utilities](contextlib-abstractcontextmanager-class.md)
