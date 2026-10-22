# exceptions: `SyntaxError`

*exception *RecursionError

This exception descends from `RuntimeError`. It arises whenever the interpreter notices that the maximum recursion depth (see [`sys.getrecursionlimit()`](https://docs.python.org/3.14/library/sys.html#sys.getrecursionlimit)) has been surpassed.

Added in version 3.5: Previously, a plain `RuntimeError` was raised.

 *exception *ReferenceError

This exception arises whenever a weak reference proxy, produced by the [`weakref.proxy()`](https://docs.python.org/3.14/library/weakref.html#weakref.proxy) function, is employed to reach an attribute of the referent once that referent has already been garbage collected. To learn more about weak references, consult the [`weakref`](https://docs.python.org/3.14/library/weakref.html#module-weakref) module.

 *exception *RuntimeError

Raised whenever an error turns up that belongs to none of the other categories. The associated value is a string spelling out exactly what went amiss.

 *exception *StopIteration

Raised by the built-in function [`next()`](https://docs.python.org/3.14/library/functions.html#next) and by an [iterator](https://docs.python.org/3.14/glossary.html#term-iterator)'s [`__next__()`](https://docs.python.org/3.14/library/stdtypes.html#iterator.__next__) method to indicate that the iterator has no more items left to yield.

 value

The exception object carries one lone attribute, `value`, which is supplied as an argument while the exception is being constructed and falls back to [`None`](https://docs.python.org/3.14/library/constants.html#None).

Whenever a [generator](https://docs.python.org/3.14/glossary.html#term-generator) or [coroutine](https://docs.python.org/3.14/glossary.html#term-coroutine) function returns, a fresh `StopIteration` instance gets raised, and whatever value the function returned becomes the `value` parameter handed to the exception's constructor.

Where generator code raises `StopIteration` either directly or indirectly, it is turned into a `RuntimeError` (keeping the `StopIteration` on as the new exception's cause).

Changed in version 3.3: The `value` attribute was added, together with the capacity for generator functions to employ it when returning a value.

Changed in version 3.5: Introduced the RuntimeError transformation via `from __future__ import generator_stop`, see [**PEP 479**](https://peps.python.org/pep-0479/).

Changed in version 3.7: Turn on [**PEP 479**](https://peps.python.org/pep-0479/) by default across all code: within a generator, a raised `StopIteration` error becomes a `RuntimeError`.

 *exception *StopAsyncIteration

Has to be raised by the [`__anext__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__anext__) method of an [asynchronous iterator](https://docs.python.org/3.14/glossary.html#term-asynchronous-iterator) object in order to halt the iteration.

Added in version 3.5.

 *exception *SyntaxError(*message*, *details*)

Raised whenever the parser runs into a syntax error. This can happen within an [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statement, within a call to the built-in functions [`compile()`](https://docs.python.org/3.14/library/functions.html#compile), [`exec()`](https://docs.python.org/3.14/library/functions.html#exec), or [`eval()`](https://docs.python.org/3.14/library/functions.html#eval), or while reading the initial script or standard input (interactively as well).

The [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) of the exception instance returns the error message and nothing more. Details is a tuple whose members can additionally be reached as individual attributes.

 filename

The name of the file in which the syntax error came up.

 lineno

The line number within the file at which the error came up. Counting starts at 1: the file's first line carries a `lineno` of 1.

 offset

The column on the line at which the error came up. Counting starts at 1: the line's first character carries an `offset` of 1.

 text

The source code text bound up in the error.

 end_lineno

The line number within the file at which the error finishes. Counting starts at 1: the file's first line carries a `lineno` of 1.

 end_offset

The column on the end line at which the error comes to a close. Counting starts at 1: the line's first character carries an `offset` of 1.

SyntaxError exposes the failing source through its location attributes. Exception messages and offsets can change between interpreter versions; inspect the actual exception through its documented attributes.

Changed in version 3.10: Added the `end_lineno` and `end_offset` attributes.

 *exception *IndentationError

The base class covering syntax errors that stem from improper indentation. It is a subclass of `SyntaxError`.

 *exception *TabError

Raised whenever indentation mixes tabs and spaces in an inconsistent way. It is a subclass of `IndentationError`.

[Subject index](INDEX.md) · [Previous](notimplementederror-to-pythonfinalizationerror.md) · [Continue](systemerror-to-typeerror.md) · [Owning module, declaration or section: Concrete exceptions](assertionerror-to-nameerror.md)
