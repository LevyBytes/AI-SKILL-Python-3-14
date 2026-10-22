# exceptions: Type-error guidance and Unicode/local-name exceptions

User code can throw this exception to signal that an operation tried on an object is unsupported and was never intended to be. When an object is supposed to support a particular operation but has not yet supplied an implementation for it, the right exception to throw is `NotImplementedError`.

Handing in arguments of the wrong type (for example, a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) where an [`int`](https://docs.python.org/3.14/library/functions.html#int) is expected) ought to yield a `TypeError`, whereas handing in arguments whose value is wrong (for example, a number lying beyond the expected limits) ought to yield a `ValueError`.

 *exception *UnboundLocalError

Thrown when a local variable in a function or method is referenced while no value has yet been bound to it. It is a subclass of `NameError`.

 *exception *UnicodeError

Thrown when a Unicode-related encoding or decoding error arises. It is a subclass of `ValueError`.

`UnicodeError` carries attributes that characterize the encoding or decoding error. As an example, `err.object[err.start:err.end]` yields the specific invalid input on which the codec stumbled.

 encoding

The name belonging to the encoding that triggered the error.

 reason

A string that spells out the particular codec error.

 object

The object that the codec was trying to encode or decode.

 start

The earliest index of invalid data within [`object`](https://docs.python.org/3.14/library/functions.html#object).

Because it is read as an absolute offset, this value ought not be negative, though that requirement goes unenforced at runtime.

 end

The index just past the final piece of invalid data within [`object`](https://docs.python.org/3.14/library/functions.html#object).

Because it is read as an absolute offset, this value ought not be negative, though that requirement goes unenforced at runtime.

 *exception *UnicodeEncodeError

Thrown when a Unicode-related error arises while encoding. It is a subclass of `UnicodeError`.

 *exception *UnicodeDecodeError

Thrown when a Unicode-related error arises while decoding. It is a subclass of `UnicodeError`.

 *exception *UnicodeTranslateError

Thrown when a Unicode-related error arises while translating. It is a subclass of `UnicodeError`.

 *exception *ValueError

Thrown when an operation or function gets an argument whose type is correct yet whose value is unsuitable, in a case that no more specific exception such as `IndexError` already covers.

 *exception *ZeroDivisionError

Thrown when the second operand of a division or modulo operation is zero. The value that accompanies it is a string naming the type of the operands together with the operation.

The exceptions below are retained for backward compatibility; as of Python 3.3, each one is an alias of `OSError`.

 *exception *EnvironmentError

 *exception *IOError

 *exception *WindowsError

Present only on Windows.

[Subject index](INDEX.md) · [Continue](blockingioerror-to-timeouterror.md) · [Owning module, declaration or section: Concrete exceptions](assertionerror-to-nameerror.md) · [Owning module, declaration or section: TypeError](systemerror-to-typeerror.md) · [Preceding source contract and version conditions](systemerror-to-typeerror.md)
