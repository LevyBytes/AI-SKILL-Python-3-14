# PYTHONBREAKPOINT

PYTHONBREAKPOINT

When this is present, it names a callable through dotted-path notation. The module that holds the callable is imported and then the callable is invoked by the default implementation of [`sys.breakpointhook()`](https://docs.python.org/3.14/library/sys.html#sys.breakpointhook), which is itself invoked by the built-in [`breakpoint()`](https://docs.python.org/3.14/library/functions.html#breakpoint). When absent, or set to the empty string, it amounts to the value "pdb.set_trace". Assigning the string "0" makes the default implementation of `sys.breakpointhook()` do nothing and return at once.

Added in version 3.7.

[Subject index](INDEX.md) · [Previous source section](pythonoptimize.md) · [Following source section](pythondebug.md)
