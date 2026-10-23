# cmath - Conversions to and from polar coordinates

### Conversions to and from polar coordinates

Internally, a Python complex number `z` is held in *rectangular* (or *Cartesian*) coordinates. Its *real part* `z.real` and its *imaginary part* `z.imag` together fix it entirely.

There is a second way to express a complex number: *polar coordinates*. Under this scheme, a complex number *z* is set by its modulus *r* and its phase angle *phi*. Here *r* gives how far *z* sits from the origin, and *phi* is the counterclockwise angle — in radians — running from the positive x-axis around to the segment connecting the origin with *z*.

You can convert between the built-in rectangular form and polar form, in either direction, with the functions below.

 cmath.phase(*z*)

Return the phase of *z* (also called the *argument* of *z*), as a float. `phase(z)` is equivalent to `math.atan2(z.imag, z.real)`. Its result falls within [-*π*, *π*], and this operation's branch cut runs along the negative real axis. The result carries the same sign as `z.imag`, including when `z.imag` equals zero:

```python
>>> phase(-1+0j)
3.141592653589793
>>> phase(-1-0j)
-3.141592653589793

```

Note

You can obtain a complex number *z*'s modulus (absolute value) through the built-in [`abs()`](https://docs.python.org/3.14/library/functions.html#abs) function. The `cmath` module supplies no dedicated function for this.

 cmath.polar(*z*)

Return the representation of *z* in polar coordinates. The return is a pair `(r, phi)`, with *r* the modulus of *z* and *phi* its phase. `polar(z)` is equivalent to `(abs(z), phase(z))`.

 cmath.rect(*r*, *phi*)

Given polar coordinates *r* and *phi*, build and return the matching complex number *z*. Equivalent to `complex(r * math.cos(phi), r * math.sin(phi))`.

[Subject index](INDEX.md) · [Previous](cmath-mathematical-functions-for-complex-numbers.md) · [Continue](cmath-exp-to-cmath-sqrt.md) · [Owning module, declaration or section: cmath](cmath-mathematical-functions-for-complex-numbers.md)
