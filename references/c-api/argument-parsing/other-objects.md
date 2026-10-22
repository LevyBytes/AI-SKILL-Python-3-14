# Other objects

### Other objects

`O` (object) [PyObject *]

Keep a Python object (with no conversion at all) in a C object pointer. What the C program receives is thus the very object that was passed. No new [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to the object is made (that is, its reference count stays the same). The pointer kept is never `NULL`.

`O!` (object) [*typeobject*, PyObject *]

Keep a Python object in a C object pointer. While this resembles `O`, it accepts a pair of C arguments: one supplies the address of a Python type object, and the other supplies the address of the C variable (of type [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*) where the object pointer is kept. Should the Python object lack the required type, a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised.

`O&` (object) [*converter*, *address*]

Turn a Python object into a C variable by way of a *converter* function. This takes two arguments: the first is a function, while the second is the address of a C variable (of any type), cast to void*. In turn, the *converter* function is invoked like so:

```c
status = converter(object, address);

```

where *object* is the Python object being converted and *address* is the void* argument that was handed to the `PyArg_Parse*` function. A returned *status* of `1` signals a successful conversion, while `0` signals that the conversion has failed. When the conversion does not succeed, the *converter* function ought to raise an exception while leaving whatever sits at *address* unchanged.

Should the *converter* return `Py_CLEANUP_SUPPORTED`, it may be invoked a second time if the argument parsing ultimately fails, letting the converter free any memory it had already reserved. On this second call, the *object* parameter will be `NULL`; *address* will carry the same value it held in the first call.

Examples of converters: [`PyUnicode_FSConverter()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FSConverter) and [`PyUnicode_FSDecoder()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FSDecoder).

Changed in version 3.1: `Py_CLEANUP_SUPPORTED` was added.

`p` ([`bool`](https://docs.python.org/3.14/library/functions.html#bool)) [int]

Checks the value passed in for truth (a boolean **p**redicate) and turns the outcome into the matching C true/false integer value. The int is set to `1` when the expression was true and `0` when it was false. Any valid Python value is accepted here. Consult [Truth Value Testing](https://docs.python.org/3.14/library/stdtypes.html#truth) for further detail on how Python checks values for truth.

Added in version 3.3.

`(items)` (sequence) [*matching-items*]

The object has to be a Python sequence (other than [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) or [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray)) whose length equals the count of format units in *items*. Each C argument has to line up with the respective format unit in *items*. Format units for sequences are allowed to nest.

When *items* holds format units that keep a borrowed buffer (`s`, `s#`, `z`, `z#`, `y`, or `y#`) or a [borrowed reference](https://docs.python.org/3.14/glossary.html#term-borrowed-reference) (`S`, `Y`, `U`, `O`, or `O!`), the object has to be a Python tuple. The *converter* belonging to the `O&` format unit inside *items* must not keep a borrowed buffer or a borrowed reference.

Changed in version 3.14: a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) or [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) object is no longer taken as a valid sequence here.

Deprecated since version 3.14: when *items* holds format units that keep a borrowed buffer or a borrowed reference, supplying a non-tuple sequence is deprecated.

Several other characters carry meaning within a format string. They may not show up inside nested parentheses. They are:

`|`

Signals that whatever arguments remain in the Python argument list are optional. C variables that correspond to optional arguments ought to be set to their default value first — when an optional argument goes unspecified, `PyArg_ParseTuple()` leaves the contents of the matching C variable(s) alone.

`$`

`PyArg_ParseTupleAndKeywords()` only: Signals that whatever arguments remain in the Python argument list are keyword-only. At present every keyword-only argument also has to be an optional argument, so `|` always has to appear ahead of `$` within the format string.

Added in version 3.3.

`:`

Here the list of format units ends; whatever string follows the colon serves as the function name within error messages (the “associated value” of the exception that `PyArg_ParseTuple()` raises).

`;`

Here the list of format units ends; whatever string follows the semicolon stands in *instead* of the default error message as the error message. You cannot use `:` and `;` together.

Bear in mind that any Python object references handed to the caller are *borrowed* references; do not release them (that is, do not decrement their reference count)!

Further arguments handed to these functions have to be addresses of variables whose type the format string dictates; they serve to store values drawn from the input tuple. In a few cases — described within the list of format units above — these parameters act as input values; when that happens, they should match whatever is specified for the matching format unit.

For the conversion to come off, the *arg* object has to match the format and the format has to be used up. On success, the `PyArg_Parse*` functions return true; otherwise they return false and raise a fitting exception. Whenever a `PyArg_Parse*` function fails owing to one format unit not converting, every variable whose address is tied to that unit, plus the ones after it, is left untouched.

[Subject index](INDEX.md) · [Previous source contract](numbers.md) · [Following source contract](pyarg-parsetuple.md)
