# Base classes

### Base classes

The exceptions below serve primarily as base classes underpinning other exceptions.

 *exception *BaseException

The class at the root of every built-in exception. User-defined classes are not intended to inherit from it directly (use `Exception` for that purpose instead). Calling [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) on an instance of this class yields the representation of the instance's argument(s), or an empty string in the case where no arguments were supplied.

 args

The tuple holding the arguments handed to the exception constructor. Certain built-in exceptions (such as `OSError`) anticipate a specific number of arguments and attach a special meaning to this tuple's elements, whereas others are generally invoked with just one string carrying an error message.

 with_traceback(*tb*)

Calling this method installs *tb* as the exception's new traceback and hands back the exception object. Its use was more widespread prior to the arrival of the exception chaining capabilities of [**PEP 3134**](https://peps.python.org/pep-3134/). The example below demonstrates converting an instance of `SomeException` into an instance of `OtherException` while keeping the traceback intact. After it is raised, the current frame gets pushed onto the `OtherException` traceback, just as it would have been pushed onto the traceback of the original `SomeException` had we let it propagate up to the caller.

```python
try:
    ...
except SomeException:
    tb = sys.exception().__traceback__
    raise OtherException(...).with_traceback(tb)

```

 __traceback__

A writable field that stores the [traceback object](https://docs.python.org/3.14/reference/datamodel.html#traceback-objects) tied to this exception. See also: [The raise statement](https://docs.python.org/3.14/reference/simple_stmts.html#raise).

 add_note(*note*)

Append the string `note` to the exception's notes, which show up in the standard traceback following the exception string. Should `note` not be a string, a `TypeError` is raised.

Added in version 3.11.

 __notes__

The list containing this exception's notes, the ones supplied through `add_note()`. The attribute comes into existence the moment `add_note()` is invoked.

Added in version 3.11.

 *exception *Exception

Every built-in exception that is not system-exiting descends from this class. All exceptions a user defines ought to descend from it as well.

 *exception *ArithmeticError

The class underpinning those built-in exceptions raised for assorted arithmetic failures: `OverflowError`, `ZeroDivisionError`, `FloatingPointError`.

 *exception *BufferError

Raised whenever a [buffer](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects) related operation is unable to be carried out.

 *exception *LookupError

The class underpinning the exceptions raised whenever a key or index applied to a mapping or sequence turns out to be invalid: `IndexError`, `KeyError`. A direct raise of this can come from [`codecs.lookup()`](https://docs.python.org/3.14/library/codecs.html#codecs.lookup).

[Subject index](INDEX.md) · [Previous](inheriting-from-built-in-exceptions.md) · [Continue](assertionerror-to-nameerror.md)
