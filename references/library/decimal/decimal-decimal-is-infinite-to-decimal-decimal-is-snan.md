# decimal.Decimal: `is_infinite()`, `is_nan()`, `is_normal()`, `is_qnan()`, `is_signed()`, `is_snan()`

is_infinite()

Return [`True`](https://docs.python.org/3.14/library/constants.html#True) if the argument is either positive or negative infinity and [`False`](https://docs.python.org/3.14/library/constants.html#False) otherwise.

 is_nan()

Return [`True`](https://docs.python.org/3.14/library/constants.html#True) if the argument is a (quiet or signaling) NaN and [`False`](https://docs.python.org/3.14/library/constants.html#False) otherwise.

 is_normal(*context=None*)

Return [`True`](https://docs.python.org/3.14/library/constants.html#True) when the argument is a *normal* finite number. Return [`False`](https://docs.python.org/3.14/library/constants.html#False) should it instead be zero, subnormal, infinite or a NaN.

 is_qnan()

Return [`True`](https://docs.python.org/3.14/library/constants.html#True) if the argument is a quiet NaN, and [`False`](https://docs.python.org/3.14/library/constants.html#False) otherwise.

 is_signed()

Return [`True`](https://docs.python.org/3.14/library/constants.html#True) when the argument bears a negative sign and [`False`](https://docs.python.org/3.14/library/constants.html#False) otherwise. Keep in mind that both zeros and NaNs may carry signs.

 is_snan()

[Subject index](INDEX.md) · [Previous](decimal-decimal-copy-sign-to-decimal-decimal-is-finite.md) · [Owning module, declaration or section: decimal](decimal-decimal-fixed-point-and-floating-point-arithmetic.md) · [Owning module, declaration or section: decimal.Decimal](decimal-decimal-class.md) · [Owning module, declaration or section: Decimal objects](decimal-decimal-class.md) · [Required continuation of the source contract](decimal-decimal-is-subnormal-to-decimal-decimal-normalize.md)
