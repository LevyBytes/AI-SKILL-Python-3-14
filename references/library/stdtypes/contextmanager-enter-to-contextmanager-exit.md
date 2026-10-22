# Context Manager Types

### Context Manager Types

The [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement in Python builds on the notion of a runtime context that a context manager establishes. A pair of methods makes this work, letting user-defined classes specify a runtime context that is entered ahead of running the statement body and exited when the statement finishes:

 contextmanager.__enter__()

Enter the runtime context and hand back either this object itself or a different object tied to the runtime context. Whatever value this method returns is bound to the identifier named in the `as` clause of any [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statements that use this context manager.

One context manager that returns itself is a [file object](https://docs.python.org/3.14/glossary.html#term-file-object). A file object hands itself back from __enter__() so that [`open()`](https://docs.python.org/3.14/library/functions.html#open) can serve as the context expression within a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement.

For a context manager that returns a related object, look to the one produced by [`decimal.localcontext()`](https://docs.python.org/3.14/library/decimal.html#decimal.localcontext). Such managers make the active decimal context a copy of the original decimal context and then return that copy. This lets the body of the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement alter the current decimal context without touching code that lives outside the `with` statement.

 contextmanager.__exit__(*exc_type*, *exc_val*, *exc_tb*)

Exit the runtime context and hand back a Boolean flag stating whether any exception that arose ought to be suppressed. Should an exception have arisen while the body of the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement ran, the arguments carry the exception type, value and traceback information. If not, all three arguments are `None`.

Should this method hand back a true value, the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement will swallow the exception and carry on running at the statement that comes right after the `with` statement. Otherwise the exception keeps propagating once this method has run to completion.

Should this method itself throw an exception while it is dealing with an earlier exception coming out of the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) block, the new exception gets raised, and the earlier one is preserved in its [`__context__`](https://docs.python.org/3.14/library/exceptions.html#BaseException.__context__) attribute.

Never re-raise the supplied exception by hand — instead, have this method return a false value to signal that it ran successfully and is not asking to suppress the raised exception. This makes it easy for context management code to spot whether an [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) method has in fact failed.

Several context managers ship with Python to make thread synchronisation straightforward, to close files or other objects promptly, and to ease working with the active decimal arithmetic context. These particular types get no special handling beyond the fact that they implement the context management protocol. The [`contextlib`](https://docs.python.org/3.14/library/contextlib.html#module-contextlib) module holds a few examples.

Python's [generator](https://docs.python.org/3.14/glossary.html#term-generator)s in tandem with the [`contextlib.contextmanager`](https://docs.python.org/3.14/library/contextlib.html#contextlib.contextmanager) decorator give you a tidy means of implementing these protocols. Decorate a generator function with the `contextlib.contextmanager` decorator and it yields a context manager that carries the required `__enter__()` and `__exit__()` methods, rather than the iterator an undecorated generator function would produce.

Keep in mind that the type structure for Python objects in the Python/C API holds no dedicated slot for any of these methods. An extension type that wants to define them has to supply them as an ordinary Python-accessible method. Set against the cost of standing up the runtime context, a single class dictionary lookup adds negligible overhead.

[Subject index](INDEX.md) · [Previous](len-to-dictview-mapping.md) · [Continue](type-annotation-types-generic-alias-union.md)
