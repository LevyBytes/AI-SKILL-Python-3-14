# Numeric utilities

#### Numeric utilities

 Py_ABS(x)

Yields the absolute value of `x`.

Its argument can be evaluated several times. For that reason, never hand this macro an expression that carries side-effects directly.

Where the outcome can't be represented (say, when `x` holds the `INT_MIN` value for the int type), the behavior is undefined.

Roughly equivalent to `((*x*) < 0 ? -(*x*) : (*x*))`

Added in version 3.3.

 Py_MAX(x, y)

 Py_MIN(x, y)

Yield, in order, the bigger or the smaller of the supplied arguments.

The arguments here can be evaluated several times. For that reason, never hand this macro an expression that carries side-effects directly.

`Py_MAX` is roughly equivalent to `(((*x*) > (*y*)) ? (*x*) : (*y*))`.

Added in version 3.3.

 Py_ARITHMETIC_RIGHT_SHIFT(type, integer, positions)

Behaves like `*integer* >> *positions*`, except it compels sign extension, since the C standard leaves it open whether right-shifting a signed integer extends the sign or fills with zeros.

*integer* may be of any signed integer type. *positions* gives the count of positions by which to shift right.

Since both *integer* and *positions* may be evaluated several times, steer clear of handing this macro a function call or any other side-effect-bearing operation directly. Stash the outcome in a variable first and pass that along instead.

*type* goes unused and lingers only for backwards compatibility. In the past, *type* served to cast *integer*.

Changed in version 3.1: This macro now works for every signed integer type, rather than only those where `unsigned type` is permitted. Accordingly, *type* is no longer in use.

 Py_CHARMASK(c)

The argument has to be a character or an integer falling within [-128, 127] or [0, 255]. This macro yields `c` cast over to an `unsigned char`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-unused-to-py-gcc-attribute.md) · [Following source contract](py-unreachable-to-py-build-assert-expr.md)
