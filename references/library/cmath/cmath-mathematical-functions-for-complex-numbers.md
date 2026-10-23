# cmath`cmath` - Mathematical functions for complex numbers

### `cmath` - Mathematical functions for complex numbers

---

Through this module you gain access to mathematical routines that operate on complex numbers. Every function here takes integers, floating-point values, or complex numbers as its arguments. Any Python object exposing either a [`__complex__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__complex__) or a [`__float__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__float__) method is likewise accepted: such methods convert the object into a complex or floating-point number respectively, after which the function runs on whatever that conversion yields.

Note

Where a function carries branch cuts, the question arises of how to define it on the cut itself. We adopt the convention from Kahan's paper "Branch cuts for complex elementary functions," together with Annex G of C99 and the C standards that followed: the sign of zero tells the two sides of a branch cut apart. For a cut running along (some stretch of) the real axis we inspect the sign of the imaginary part, whereas for a cut running along the imaginary axis we inspect the sign of the real part.

To illustrate, the `cmath.sqrt()` function carries a branch cut down the negative real axis. The argument `-2-0j` is taken to sit *below* that cut, so the outcome lands on the negative imaginary axis:

```python
>>> cmath.sqrt(-2-0j)
-1.4142135623730951j

```

The argument `-2+0j`, by contrast, is taken to sit above the cut:

```python
>>> cmath.sqrt(-2+0j)
1.4142135623730951j

```

| **Conversions to and from polar coordinates** |  |
| --- | --- |
| `phase(z)` | Return the phase of *z* |
| `polar(z)` | Return the representation of *z* in polar coordinates |
| `rect(r, phi)` | Return the complex number *z* with polar coordinates *r* and *phi* |
| **Power and logarithmic functions** |  |
| `exp(z)` | Return *e* raised to the power *z* |
| `log(z[, base])` | Return the logarithm of *z* to the given *base* (*e* by default) |
| `log10(z)` | Return the base-10 logarithm of *z* |
| `sqrt(z)` | Return the square root of *z* |
| **Trigonometric functions** |  |
| `acos(z)` | Return the arc cosine of *z* |
| `asin(z)` | Return the arc sine of *z* |
| `atan(z)` | Return the arc tangent of *z* |
| `cos(z)` | Return the cosine of *z* |
| `sin(z)` | Return the sine of *z* |
| `tan(z)` | Return the tangent of *z* |
| **Hyperbolic functions** |  |
| `acosh(z)` | Return the inverse hyperbolic cosine of *z* |
| `asinh(z)` | Return the inverse hyperbolic sine of *z* |
| `atanh(z)` | Return the inverse hyperbolic tangent of *z* |
| `cosh(z)` | Return the hyperbolic cosine of *z* |
| `sinh(z)` | Return the hyperbolic sine of *z* |
| `tanh(z)` | Return the hyperbolic tangent of *z* |
| **Classification functions** |  |
| `isfinite(z)` | Check if all components of *z* are finite |
| `isinf(z)` | Check if any component of *z* is infinite |
| `isnan(z)` | Check if any component of *z* is a NaN |
| `isclose(a, b, *, rel_tol, abs_tol)` | Check if the values *a* and *b* are close to each other |
| **Constants** |  |
| `pi` | *π* = 3.141592… |
| `e` | *e* = 2.718281… |
| `tau` | *τ* = 2*π* = 6.283185… |
| `inf` | Positive infinity |
| `infj` | Pure imaginary infinity |
| `nan` | “Not a number” (NaN) |
| `nanj` | Pure imaginary NaN |

[Subject index](INDEX.md) · [Previous](mathematical-functions-for-complex-numbers.md) · [Continue](cmath-phase-to-cmath-rect.md)
