# How can I execute arbitrary Python statements from C?

### How can I execute arbitrary Python statements from C?

At the top of the hierarchy sits [`PyRun_SimpleString()`](https://docs.python.org/3.14/c-api/veryhigh.html#c.PyRun_SimpleString), which accepts one string argument, runs it within the `__main__` module's context, and hands back `0` on success or `-1` should an exception arise (a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) included). For finer command, reach for [`PyRun_String()`](https://docs.python.org/3.14/c-api/veryhigh.html#c.PyRun_String); the source of `PyRun_SimpleString()` lives in `Python/pythonrun.c`.

[Subject index](INDEX.md)
