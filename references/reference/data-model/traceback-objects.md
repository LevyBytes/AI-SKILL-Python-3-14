# 3.2.13.3. Traceback objects

#### 3.2.13.3. Traceback objects

A traceback object captures the stack trace of an [exception](https://docs.python.org/3.14/tutorial/errors.html#tut-errors). One gets built implicitly the moment an exception is raised, and one can also be built explicitly by invoking [`types.TracebackType`](https://docs.python.org/3.14/library/types.html#types.TracebackType).

Changed in version 3.7: Python code is now able to instantiate traceback objects explicitly.

In the implicit case, as the hunt for an exception handler unwinds the execution stack, a traceback object gets prepended ahead of the current traceback at each level that is unwound. Once an exception handler takes over, the program gains access to the stack trace. (Refer to the section [The try statement](https://docs.python.org/3.14/reference/compound_stmts.html#try).) It can be reached as the third element of the tuple that [`sys.exc_info()`](https://docs.python.org/3.14/library/sys.html#sys.exc_info) returns, and via the [`__traceback__`](https://docs.python.org/3.14/library/exceptions.html#BaseException.__traceback__) attribute of the exception that was caught.

If no fitting handler is present in the program, the stack trace is emitted (neatly formatted) to the standard error stream; and when the interpreter is running interactively, it is additionally offered to the user through [`sys.last_traceback`](https://docs.python.org/3.14/library/sys.html#sys.last_traceback).

With explicitly built tracebacks, whoever creates the traceback decides how the `tb_next` attributes ought to be chained together into a complete stack trace.

Special read-only attributes:

| traceback.tb_frame | Refers to the current level’s execution frame. Reading this attribute raises an auditing event `object.__getattr__` with arguments `obj` and `"tb_frame"`. |
| --- | --- |
| traceback.tb_lineno | Supplies the line number at which the exception arose |
| traceback.tb_lasti | Points out the “precise instruction”. |

Within the traceback, the line number and last instruction can be unlike the line number of its frame object whenever the exception arose inside a [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) statement that had no matching except clause or that carried a [`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) clause.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](internal-types.md) · [Previous source section](frame-clear.md) · [Following source section](traceback-tb-next.md)
