# cmath - Constants

### Constants

 cmath.pi

The mathematical constant *π*, as a float.

 cmath.e

The mathematical constant *e*, as a float.

 cmath.tau

The mathematical constant *τ*, as a float.

Added in version 3.6.

 cmath.inf

Floating-point positive infinity. Equivalent to `float('inf')`.

Added in version 3.6.

 cmath.infj

A complex value whose real part is zero and whose imaginary part is positive infinity. Equivalent to `complex(0.0, float('inf'))`.

Added in version 3.6.

 cmath.nan

A floating-point “not a number” (NaN) value. Equivalent to `float('nan')`. See also [`math.nan`](https://docs.python.org/3.14/library/math.html#math.nan).

Added in version 3.6.

 cmath.nanj

A complex value whose real part is zero and whose imaginary part is NaN. Equivalent to `complex(0.0, float('nan'))`.

Added in version 3.6.

Be aware that this set of functions resembles, without exactly matching, the one in module [`math`](https://docs.python.org/3.14/library/math.html#module-math). The two modules exist separately because some users have no interest in complex numbers and may not even know what they are. For them it is preferable that `math.sqrt(-1)` raise an exception rather than hand back a complex number. Be aware too that the functions in `cmath` invariably return a complex number, even when the answer happens to be real (where the complex number simply has a zero imaginary part).

A word about branch cuts: these are curves along which the function in question loses continuity. They are an unavoidable feature of many complex functions. The assumption is that anyone who needs to compute with complex functions will already grasp branch cuts. For clarity, turn to virtually any (not overly introductory) text on complex variables. On choosing branch cuts well for numerical work, a sound reference is the following:

See also

Kahan, W: `Branch cuts for complex elementary functions; or, Much ado about nothing’s sign bit`. Published in *The state of the art in numerical analysis*, edited by Iserles, A., and Powell, M., Clarendon Press (1987), pp165–211.

[Subject index](INDEX.md) · [Previous](cmath-isfinite-to-cmath-isclose.md) · [Continue](../cmd/cmd-cmd-class.md) · [Owning module, declaration or section: cmath](cmath-mathematical-functions-for-complex-numbers.md)
