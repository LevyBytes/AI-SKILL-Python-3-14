# sys.exit

sys.exit([*arg*])

Raise a [`SystemExit`](https://docs.python.org/3.14/library/exceptions.html#SystemExit) exception, which signals an intent to leave the interpreter.

The optional *arg* argument may be an integer that supplies the exit status (defaulting to zero), or some other kind of object. When it is an integer, shells and similar tools read zero as “successful termination” and any nonzero value as “abnormal termination”. Most systems expect it to fall within the range 0–127, with undefined behavior otherwise. Certain systems follow a convention that ties particular meanings to particular exit codes, though these tend to be sparsely defined; Unix programs typically reserve 2 for command line syntax errors and 1 for every other kind of error. When some other object type is supplied, `None` works the same as passing zero, and any other object is printed to `stderr` and yields an exit code of 1. Notably, `sys.exit("some error message")` offers a fast way out of a program when an error happens.

Because `exit()` in the end “merely” raises an exception, it will exit the process only when invoked from the main thread and the exception goes uncaught. Cleanup actions named by finally clauses of [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) statements are respected, and you can catch the exit attempt at some outer level.

Changed in version 3.6: Where something goes wrong during the cleanup that follows the Python interpreter catching [`SystemExit`](https://docs.python.org/3.14/library/exceptions.html#SystemExit) — for instance a failure to flush buffered data in the standard streams — the exit status is set to 120 instead.

[API family](INDEX.md) · [sys context index](../INDEX.md).
