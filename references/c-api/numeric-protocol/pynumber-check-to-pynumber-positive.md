# numeric protocol C API: Numeric checks and arithmetic object operations

# Number

### Number Protocol

 int PyNumber_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hands back `1` when the object *o* supplies numeric protocols, and false in any other case. This function always succeeds.

Changed in version 3.8: Now hands back `1` when *o* is an index integer.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_Add([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields the sum of *o1* and *o2*, or `NULL` should it fail. It mirrors the Python expression `o1 + o2`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_Subtract([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields what remains after *o2* is taken from *o1*, or `NULL` should it fail. It stands in for the Python expression `o1 - o2`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_Multiply([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields the product of *o1* and *o2*, or `NULL` should it fail. It corresponds to the Python expression `o1 * o2`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_MatrixMultiply([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Yields the matrix product of *o1* and *o2*, or `NULL` should it fail. It matches the Python expression `o1 @ o2`.

Added in version 3.5.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_FloorDivide([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields the floor of *o1* over *o2*, or `NULL` should it fail. It answers to the Python expression `o1 // o2`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_TrueDivide([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields a sensible approximation to the mathematical value of *o1* over *o2*, or `NULL` should it fail. That value is “approximate” precisely because binary floating-point numbers themselves are approximate — base two simply cannot capture every real number. Even handed two integers, this function may produce a floating-point value. It answers to the Python expression `o1 / o2`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_Remainder([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields what is left over when *o1* is divided by *o2*, or `NULL` should it fail. It lines up with the Python expression `o1 % o2`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_Divmod([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Consult the built-in function [`divmod()`](https://docs.python.org/3.14/library/functions.html#divmod). Gives `NULL` should it fail. It reproduces the Python expression `divmod(o1, o2)`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_Power([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o3)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Consult the built-in function [`pow()`](https://docs.python.org/3.14/library/functions.html#pow). Gives `NULL` should it fail. It reproduces the Python expression `pow(o1, o2, o3)`, in which *o3* is optional. When you mean to skip *o3*, supply [`Py_None`](https://docs.python.org/3.14/c-api/none.html#c.Py_None) where it would go (handing `NULL` for *o3* would trigger an illegal memory access).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_Negative([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

On success yields the negation of *o*, or `NULL` should it fail. It mirrors the Python expression `-o`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_Positive([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

On success yields *o* itself, or `NULL` should it fail. It stands in for the Python expression `+o`.

[Subject index](INDEX.md) · [Following source contract](pynumber-absolute-to-pynumber-inplacetruedivide.md)
