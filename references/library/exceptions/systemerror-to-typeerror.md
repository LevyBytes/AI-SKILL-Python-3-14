# exceptions: Interpreter, exit and type-error exceptions

*exception *SystemError

Raised whenever the interpreter runs into an internal error, yet the situation does not appear grave enough to make it give up entirely. The associated value is a string describing what went wrong (in low-level terms). Within [CPython](https://docs.python.org/3.14/glossary.html#term-CPython), it could be raised through misuse of Python's C API, for instance by returning a `NULL` value while no exception has been set.

Should you be sure that this exception was not caused by you, nor by a package you happen to use, you ought to report it to the author or maintainer of your Python interpreter. Take care to report the version of the Python interpreter (`sys.version`; it also prints at the outset of an interactive Python session), the precise error message (the exception's associated value), and where possible the source of the program that set off the error.

 *exception *SystemExit

The [`sys.exit()`](https://docs.python.org/3.14/library/sys.html#sys.exit) function raises this exception. Rather than `Exception`, it inherits from `BaseException` so that code catching `Exception` does not accidentally swallow it. That lets the exception propagate up properly and bring about the interpreter's exit. Left unhandled, the Python interpreter exits; no stack traceback gets printed. The constructor takes the same optional argument handed to `sys.exit()`. Where the value is an integer, it sets the system exit status (handed to C's `exit()` function); where it is `None`, the exit status comes out as zero; where it has some other type (a string, say), the object's value is printed and the exit status comes out as one.

Invoking [`sys.exit()`](https://docs.python.org/3.14/library/sys.html#sys.exit) is converted into an exception, both so that clean-up handlers ([`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) clauses of [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) statements) get to run, and so that a debugger can run a script without the danger of losing control. The [`os._exit()`](https://docs.python.org/3.14/library/os.html#os._exit) function is available for when an immediate exit is absolutely and positively required (for instance, within the child process after a call to [`os.fork()`](https://docs.python.org/3.14/library/os.html#os.fork)).

 code

The exit status or error message handed to the constructor. (Falls back to `None`.)

 *exception *TypeError

Raised whenever an operation or function is applied to an object whose type is inappropriate. The associated value is a string detailing the type mismatch.

[Subject index](INDEX.md) · [Previous](recursionerror-to-taberror.md) · [Owning module, declaration or section: Concrete exceptions](assertionerror-to-nameerror.md) · [Required continuation of the source contract](unboundlocalerror-to-windowserror.md)
