# numeric protocol C API: Numeric unary, bitwise and in-place arithmetic

[PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_Absolute([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields the absolute value of *o*, or `NULL` should it fail. It corresponds to the Python expression `abs(o)`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_Invert([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

On success yields the bitwise negation of *o*, or `NULL` should it fail. It matches the Python expression `~o`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_Lshift([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

On success yields *o1* shifted left by *o2*, or `NULL` should it fail. It answers to the Python expression `o1 << o2`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_Rshift([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

On success yields *o1* shifted right by *o2*, or `NULL` should it fail. It lines up with the Python expression `o1 >> o2`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_And([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

On success yields the “bitwise and” of *o1* and *o2*, and `NULL` should it fail. It reproduces the Python expression `o1 & o2`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_Xor([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

On success yields the “bitwise exclusive or” of *o1* by *o2*, or `NULL` should it fail. It maps onto the Python expression `o1 ^ o2`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_Or([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

On success yields the “bitwise or” of *o1* and *o2*, or `NULL` should it fail. It corresponds to the Python expression `o1 | o2`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_InPlaceAdd([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields the sum of *o1* and *o2*, or `NULL` should it fail. Where *o1* allows for it, the work happens *in-place*. It mirrors the Python statement `o1 += o2`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_InPlaceSubtract([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields what remains after *o2* is taken from *o1*, or `NULL` should it fail. Where *o1* allows for it, the work happens *in-place*. It stands in for the Python statement `o1 -= o2`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_InPlaceMultiply([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields the product of *o1* and *o2*, or `NULL` should it fail. Where *o1* allows for it, the work happens *in-place*. It corresponds to the Python statement `o1 *= o2`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_InPlaceMatrixMultiply([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Yields the matrix product of *o1* and *o2*, or `NULL` should it fail. Where *o1* allows for it, the work happens *in-place*. It matches the Python statement `o1 @= o2`.

Added in version 3.5.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_InPlaceFloorDivide([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields the mathematical floor of *o1* divided by *o2*, or `NULL` should it fail. Where *o1* allows for it, the work happens *in-place*. It answers to the Python statement `o1 //= o2`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyNumber_InPlaceTrueDivide([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields a sensible approximation to the mathematical value of *o1* over *o2*, or `NULL` should it fail. That value is “approximate” precisely because binary floating-point numbers themselves are approximate — base two simply cannot capture every real number. Even handed two integers, this function may produce a floating-point value. Where *o1* allows for it, the work happens *in-place*. It answers to the Python statement `o1 /= o2`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pynumber-check-to-pynumber-positive.md) · [Following source contract](pynumber-inplaceremainder-to-pyindex-check.md)
