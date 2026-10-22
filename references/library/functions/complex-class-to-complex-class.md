# Built-in Functions

*class *complex(*number=0*, */*)

 *class *complex(*string*, */*)

 *class *complex(*real=0*, *imag=0*)

Render a lone string or number as a complex number, or assemble one out of separate real and imaginary parts.

Examples:

```pycon
>>> complex('+1.23')
(1.23+0j)
>>> complex('-4.5j')
-4.5j
>>> complex('-1.23+4.5j')
(-1.23+4.5j)
>>> complex('\t( -1.23+4.5J )\n')
(-1.23+4.5j)
>>> complex('-Infinity+NaNj')
(-inf+nanj)
>>> complex(1.23)
(1.23+0j)
>>> complex(imag=-4.5)
-4.5j
>>> complex(-1.23, 4.5)
(-1.23+4.5j)

```

A string argument has to carry either a real part (formatted just as `float()` expects) or an imaginary part (formatted likewise but ending in a `'j'` or `'J'` suffix), or both real and imaginary parts (where the imaginary part’s sign is then required). Surrounding whitespace and the round parentheses `'('` and `')'` are permitted around the string and simply ignored. No whitespace is allowed within the string between `'+'`, `'-'`, the `'j'` or `'J'` suffix, and the decimal number. So `complex('1+2j')` works, while `complex('1 + 2j')` raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError). Stated exactly, once parentheses plus leading and trailing whitespace have been stripped, the input has to satisfy the `complexvalue` production rule of the grammar below:

```text

complexvalue: floatvalue |
              floatvalue ("j" | "J") |
              floatvalue sign absfloatvalue ("j" | "J")
```

A number argument turns the constructor into a numeric conversion, on par with `int` and `float`. Given some arbitrary Python object `x`, `complex(x)` hands off to `x.__complex__()`. Where [`__complex__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__complex__) is absent, it drops back to [`__float__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__float__). Where `__float__()` is absent too, it drops back to [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__).

Supply two arguments, or use keyword arguments, and each one may be of any numeric type (complex included). When both arguments are real numbers, the result is a complex number whose real component is *real* and whose imaginary component is *imag*. When both arguments are complex numbers, the result is a complex number whose real component is `real.real-imag.imag` and whose imaginary component is `real.imag+imag.real`. When just one argument is a real number, only its real component figures into the expressions above.

Consult [`complex.from_number()`](https://docs.python.org/3.14/library/stdtypes.html#complex.from_number) too, which takes a single numeric argument and nothing more.

Omit every argument and you get `0j` back.

The complex type is covered in [Numeric Types — int, float, complex](https://docs.python.org/3.14/library/stdtypes.html#typesnumeric).

Changed in version 3.6: Separating digits with underscores, the way code literals do, is permitted.

Changed in version 3.8: Where neither [`__complex__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__complex__) nor [`__float__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__float__) is defined, it now drops back to [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__).

Deprecated since version 3.14: Handing a complex number to the *real* or *imag* argument is deprecated as of now; supply it solely as one positional argument.

[Subject index](INDEX.md) · [Previous](INDEX.md) · [Continue](delattr.md) · [Owning module, declaration or section: Built-in Functions](INDEX.md)
