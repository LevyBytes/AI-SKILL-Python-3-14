# Available static markers

### Available static markers

 function__entry(str filename, str funcname, int lineno)

This marker signals that a Python function has started running. It fires solely for pure-Python (bytecode) functions.

The script receives the filename, the function name, and the line number as positional arguments, which it reaches through `$arg1`, `$arg2`, `$arg3`:

>
- `$arg1` : the `(const char *)` filename, read via `user_string($arg1)`

- `$arg2` : the `(const char *)` function name, read via `user_string($arg2)`

- `$arg3` : `int` line number

 function__return(str filename, str funcname, int lineno)

Serving as the opposite of `function__entry()`, this marker reports that a Python function has finished (whether through `return` or because an exception was raised). It fires solely for pure-Python (bytecode) functions.

Its arguments match those of `function__entry()`

 line(str filename, str funcname, int lineno)

This marker shows that a Python line is on the verge of running. Think of it as the line-by-line tracing you would get from a Python profiler. Inside C functions it does not fire.

Its arguments match those of `function__entry()`.

 gc__start(int generation)

Triggers as the Python interpreter begins a garbage collection cycle. Here `arg0` gives the generation to scan, mirroring [`gc.collect()`](https://docs.python.org/3.14/library/gc.html#gc.collect).

 gc__done(long collected)

Triggers once the Python interpreter wraps up a garbage collection cycle. Here `arg0` holds how many objects were collected.

 import__find__load__start(str modulename)

Triggers just before [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib) tries to locate and load the module. Here `arg0` carries the module name.

Added in version 3.7.

 import__find__load__done(str modulename, int found)

Triggers after the find_and_load function of [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib) has run. Here `arg0` carries the module name, while `arg1` reports whether the module loaded successfully.

Added in version 3.7.

 audit(str event, void *tuple)

Triggers on a call to [`sys.audit()`](https://docs.python.org/3.14/library/sys.html#sys.audit) or [`PySys_Audit()`](https://docs.python.org/3.14/c-api/sys.html#c.PySys_Audit). Here `arg0` is the event name given as a C string, and `arg1` is a [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) pointer referring to a tuple object.

Added in version 3.8.

[Subject index](INDEX.md) · [Previous source context](static-systemtap-markers.md) · [Following source context](c-entry-points.md)
