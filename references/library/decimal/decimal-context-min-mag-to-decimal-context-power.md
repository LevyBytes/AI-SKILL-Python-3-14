# decimal.Context: `min_mag()`, `minus()`, `multiply()`, `next_minus()`, `next_plus()`, `next_toward()`, `normalize()`, `number_class()`, `plus()`, `power()`

min_mag(*x*, *y*, */*)

Compares the values numerically with their sign ignored.

 minus(*x*, */*)

Minus corresponds to the unary prefix minus operator in Python.

 multiply(*x*, *y*, */*)

Return the product of *x* and *y*.

 next_minus(*x*, */*)

Returns the largest representable number smaller than *x*.

 next_plus(*x*, */*)

Returns the smallest representable number larger than *x*.

 next_toward(*x*, *y*, */*)

Returns the number closest to *x*, in direction towards *y*.

 normalize(*x*, */*)

Reduces *x* to its simplest form.

 number_class(*x*, */*)

Returns an indication of the class of *x*.

 plus(*x*, */*)

Plus maps onto Python's unary prefix plus operator. Because it applies the context precision along with rounding, the operation is *not* an identity one.

 power(*x*, *y*, *modulo=None*)

Return `x` to the power of `y`, reduced modulo `modulo` if given.

[Subject index](INDEX.md) · [Previous](decimal-context-fma-to-decimal-context-min.md) · [Owning module, declaration or section: decimal](decimal-decimal-fixed-point-and-floating-point-arithmetic.md) · [Owning module, declaration or section: decimal.Context](decimal-context-class-to-decimal-context-create-decimal.md) · [Owning module, declaration or section: Context objects](decimal-getcontext-to-decimal-defaultcontext.md) · [Required continuation of the source contract](decimal-context-quantize-to-decimal-context-to-integral-exact.md)
