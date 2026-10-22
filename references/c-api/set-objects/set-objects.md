# set objects C API: Set and frozenset C API purpose

# Set, Slice

## Overview

Covers: Set Objects; Slice Objects.

## Set Objects

### Set Objects

The public interface for [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) and [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset) objects is described here. For anything not enumerated below, reach for either the abstract object protocol (which provides [`PyObject_CallMethod()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_CallMethod), [`PyObject_RichCompareBool()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_RichCompareBool), [`PyObject_Hash()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_Hash), [`PyObject_Repr()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_Repr), [`PyObject_IsTrue()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_IsTrue), [`PyObject_Print()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_Print), and [`PyObject_GetIter()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GetIter)) or else the abstract number protocol (which provides [`PyNumber_And()`](https://docs.python.org/3.14/c-api/number.html#c.PyNumber_And), [`PyNumber_Subtract()`](https://docs.python.org/3.14/c-api/number.html#c.PyNumber_Subtract), [`PyNumber_Or()`](https://docs.python.org/3.14/c-api/number.html#c.PyNumber_Or), [`PyNumber_Xor()`](https://docs.python.org/3.14/c-api/number.html#c.PyNumber_Xor), [`PyNumber_InPlaceAnd()`](https://docs.python.org/3.14/c-api/number.html#c.PyNumber_InPlaceAnd), [`PyNumber_InPlaceSubtract()`](https://docs.python.org/3.14/c-api/number.html#c.PyNumber_InPlaceSubtract), [`PyNumber_InPlaceOr()`](https://docs.python.org/3.14/c-api/number.html#c.PyNumber_InPlaceOr), and [`PyNumber_InPlaceXor()`](https://docs.python.org/3.14/c-api/number.html#c.PyNumber_InPlaceXor)).

[Subject index](INDEX.md) · [Following source contract](pysetobject-to-pyset-get-size.md)
