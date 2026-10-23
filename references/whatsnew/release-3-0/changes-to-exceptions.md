# What's New In Python 3.0 / Changes To Exceptions - sys

### Changes To Exceptions

The interfaces used to raise and to catch exceptions were tidied up, and several capable new features were introduced:

- [**PEP 352**](https://peps.python.org/pep-0352/): Every exception is now required to descend (whether directly or through some chain) from [`BaseException`](https://docs.python.org/3.14/library/exceptions.html#BaseException), which sits at the very top of the exception tree. As advice this was nothing new, but enforcing inheritance from `BaseException` as a hard rule is. (Back in Python 2.6 you could still raise old-style classes and catch absolutely anything.) The upshot is that string exceptions are at last completely and permanently extinct.

- In practice nearly every exception ought to inherit from [`Exception`](https://docs.python.org/3.14/library/exceptions.html#Exception); reserve [`BaseException`](https://docs.python.org/3.14/library/exceptions.html#BaseException) as a parent class only for the kind of exceptions meant to be caught at the outermost level, like [`SystemExit`](https://docs.python.org/3.14/library/exceptions.html#SystemExit) and [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt). To trap everything besides that last group, the preferred pattern is [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) `Exception`.

- `StandardError` was removed.

- An exception object can no longer be treated like a sequence; reach for the [`args`](https://docs.python.org/3.14/library/exceptions.html#BaseException.args) attribute in its place.

- [**PEP 3109**](https://peps.python.org/pep-3109/): Raising exceptions. The spelling you must adopt is now `raise *Exception*(*args*)` rather than `raise *Exception*, *args*`. On top of that, supplying a traceback explicitly is no longer permitted; should you genuinely need to, assign straight to the [`__traceback__`](https://docs.python.org/3.14/library/exceptions.html#BaseException.__traceback__) attribute (described further down).

- [**PEP 3110**](https://peps.python.org/pep-3110/): Catching exceptions. The required form becomes `except *SomeException* as *variable*` in place of `except *SomeException*, *variable*`. Beyond that, the bound name is removed deliberately once control exits the [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) block.

- [**PEP 3134**](https://peps.python.org/pep-3134/): Exception chaining. Two scenarios exist — implicit and explicit chaining. The implicit kind arises whenever an exception is thrown from inside an [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) or [`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) handler. Typically that signals a defect in the handler code, and we term the resulting exception a `secondary` one. When it occurs, whatever exception was originally under treatment gets stashed in the secondary exception's [`__context__`](https://docs.python.org/3.14/library/exceptions.html#BaseException.__context__) attribute. To trigger explicit chaining, you write:

```python
raise SecondaryException() from primary_exception

```

(here `primary_exception` stands for any expression yielding an exception object, most likely one caught earlier). Under this scheme the primary exception ends up recorded in the secondary exception's [`__cause__`](https://docs.python.org/3.14/library/exceptions.html#BaseException.__cause__) attribute. Whenever an unhandled exception surfaces, the traceback that gets printed traverses the linked `__cause__` and [`__context__`](https://docs.python.org/3.14/library/exceptions.html#BaseException.__context__) attributes, emitting a distinct traceback for every link in that chain and placing the primary exception at the very top. (Anyone coming from Java will find this familiar.)

- [**PEP 3134**](https://peps.python.org/pep-3134/): An exception object now keeps its own traceback in the [`__traceback__`](https://docs.python.org/3.14/library/exceptions.html#BaseException.__traceback__) attribute. Consequently a single exception object holds every piece of data relevant to that exception, leaving far fewer occasions to call [`sys.exc_info()`](https://docs.python.org/3.14/library/sys.html#sys.exc_info) (which has nonetheless been kept).

- Several of the messages raised when Windows cannot load an extension module are now clearer. To illustrate, `error code 193` reads as `%1 is not a valid Win32 application` these days. Such strings also cope properly with locales other than English now.

[Subject index](INDEX.md) · [Previous source section](pep-3101-a-new-approach-to-string-formatting.md) · [Next source section](operators-and-special-methods.md) · [Release/subject declaration](common-stumbling-blocks.md)
