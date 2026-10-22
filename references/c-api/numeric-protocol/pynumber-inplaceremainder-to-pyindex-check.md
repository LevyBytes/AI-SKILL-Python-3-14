# numeric protocol C API: In-place numeric operations and index conversion

[PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_InPlaceRemainder([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields what is left over when *o1* is divided by *o2*, or `NULL` should it fail. Where *o1* allows for it, the work happens *in-place*. It lines up with the Python statement `o1 %= o2`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_InPlacePower([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o3)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Consult the built-in function [`pow()`](https://docs.python.org/3.14/library/functions.html#pow). Gives `NULL` should it fail. Where *o1* allows for it, the work happens *in-place*. It reproduces the Python statement `o1 **= o2` when o3 is [`Py_None`](https://docs.python.org/3.14/c-api/none.html#c.Py_None), and otherwise an in-place flavor of `pow(o1, o2, o3)`. When you mean to skip *o3*, supply `Py_None` where it would go (handing `NULL` for *o3* would trigger an illegal memory access).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_InPlaceLshift([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

On success yields *o1* shifted left by *o2*, or `NULL` should it fail. Where *o1* allows for it, the work happens *in-place*. It maps onto the Python statement `o1 <<= o2`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_InPlaceRshift([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

On success yields *o1* shifted right by *o2*, or `NULL` should it fail. Where *o1* allows for it, the work happens *in-place*. It corresponds to the Python statement `o1 >>= o2`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_InPlaceAnd([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

On success yields the “bitwise and” of *o1* and *o2*, and `NULL` should it fail. Where *o1* allows for it, the work happens *in-place*. It reproduces the Python statement `o1 &= o2`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_InPlaceXor([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

On success yields the “bitwise exclusive or” of *o1* by *o2*, or `NULL` should it fail. Where *o1* allows for it, the work happens *in-place*. It maps onto the Python statement `o1 ^= o2`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_InPlaceOr([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

On success yields the “bitwise or” of *o1* and *o2*, or `NULL` should it fail. Where *o1* allows for it, the work happens *in-place*. It answers to the Python statement `o1 |= o2`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_Long([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

On success yields *o* turned into an integer object, or `NULL` should it fail. It mirrors the Python expression `int(o)`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_Float([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

On success yields *o* turned into a float object, or `NULL` should it fail. It corresponds to the Python expression `float(o)`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_Index([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

On success yields *o* turned into a Python int, or `NULL` accompanied by a raised [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception when it fails.

Changed in version 3.10: The outcome is now always of exact type [`int`](https://docs.python.org/3.14/library/functions.html#int). Before, it might have been an instance of some subclass of `int`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_ToBase([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *n, int base)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields the integer *n* rendered into base *base* as a string. The *base* argument has to be one of 2, 8, 10, or 16. With base 2, 8, or 16, a base marker of `'0b'`, `'0o'`, or `'0x'` (respectively) leads the returned string. Should *n* not already be a Python int, it gets run through `PyNumber_Index()` beforehand.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyNumber_AsSsize_t([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields *o* turned into a [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) value provided *o* can be read as an integer. Where the call fails, an exception is raised and `-1` comes back.

Where *o* does convert to a Python int yet turning it into a [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) value would raise an [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError), the *exc* argument names which exception type gets raised (commonly [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError) or `OverflowError`). When *exc* is `NULL`, the exception is instead cleared and the value is clamped — to `PY_SSIZE_T_MIN` for a negative integer or to `PY_SSIZE_T_MAX` for a positive one.

 int PyIndex_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.8.*

Yields `1` when *o* is an index integer — that is, when the `nb_index` slot of the `tp_as_number` structure is filled in — and `0` otherwise. This function always succeeds.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pynumber-check-to-pynumber-positive.md) · [Previous source contract](pynumber-absolute-to-pynumber-inplacetruedivide.md)
