# decimal.Context: Decimal context classification, logarithms and logical operations

fma(*x*, *y*, *z*, */*)

Returns *x* multiplied by *y*, plus *z*.

 is_canonical(*x*, */*)

Returns `True` if *x* is canonical; otherwise returns `False`.

 is_finite(*x*, */*)

Returns `True` if *x* is finite; otherwise returns `False`.

 is_infinite(*x*, */*)

Returns `True` if *x* is infinite; otherwise returns `False`.

 is_nan(*x*, */*)

Returns `True` if *x* is a qNaN or sNaN; otherwise returns `False`.

 is_normal(*x*, */*)

Returns `True` if *x* is a normal number; otherwise returns `False`.

 is_qnan(*x*, */*)

Returns `True` if *x* is a quiet NaN; otherwise returns `False`.

 is_signed(*x*, */*)

Returns `True` if *x* is negative; otherwise returns `False`.

 is_snan(*x*, */*)

Returns `True` if *x* is a signaling NaN; otherwise returns `False`.

 is_subnormal(*x*, */*)

Returns `True` if *x* is subnormal; otherwise returns `False`.

 is_zero(*x*, */*)

Returns `True` if *x* is a zero; otherwise returns `False`.

 ln(*x*, */*)

Returns the natural (base e) logarithm of *x*.

 log10(*x*, */*)

Returns the base 10 logarithm of *x*.

 logb(*x*, */*)

Returns the exponent of the magnitude of the operand's MSD.

 logical_and(*x*, *y*, */*)

Applies the logical operation *and* between each operand's digits.

 logical_invert(*x*, */*)

Invert all the digits in *x*.

 logical_or(*x*, *y*, */*)

Applies the logical operation *or* between each operand's digits.

 logical_xor(*x*, *y*, */*)

Applies the logical operation *xor* between each operand's digits.

 max(*x*, *y*, */*)

Compares two values numerically and returns the maximum.

 max_mag(*x*, *y*, */*)

Compares the values numerically with their sign ignored.

 min(*x*, *y*, */*)

Compares two values numerically and returns the minimum.

[Subject index](INDEX.md) · [Previous](decimal-context-conversion-and-exponential.md) · [Continue](decimal-context-min-mag-to-decimal-context-power.md) · [Owning module, declaration or section: decimal](decimal-decimal-fixed-point-and-floating-point-arithmetic.md) · [Owning module, declaration or section: decimal.Context](decimal-context-class-to-decimal-context-create-decimal.md) · [Owning module, declaration or section: Context objects](decimal-getcontext-to-decimal-defaultcontext.md)
