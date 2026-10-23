# What’s New in Python 2.6 / PEP 3141: A Type Hierarchy for Numbers - fractions, math, numbers

### PEP 3141: A Type Hierarchy for Numbers

Python 3.0 brings in a handful of abstract base classes for numeric types, drawing on the numeric tower from Scheme. Those classes landed in 2.6 too, as the [`numbers`](https://docs.python.org/3.14/library/numbers.html#module-numbers) module.

`Number` is the broadest ABC. It declares no operations whatsoever and is present solely so you can verify that an object is a number with `isinstance(obj, Number)`.

`Complex` descends from `Number`. The elementary arithmetic of complex numbers — addition, subtraction, multiplication, division, and exponentiation — applies, and you can pull out the real and imaginary parts and compute a number’s conjugate. The built-in complex type in Python realizes `Complex`.

`Real`, in turn, derives from `Complex` and supplies operations limited to real numbers: `floor()`, `trunc()`, rounding, the remainder mod N, floor division, and comparisons.

Deriving from `Real`, the `Rational` numbers carry `numerator` and `denominator` properties and convert to floats. Python 2.6 contributes a straightforward rational-number class, `Fraction`, found in the [`fractions`](https://docs.python.org/3.14/library/fractions.html#module-fractions) module. (The name `Fraction` rather than `Rational` sidesteps a collision with [`numbers.Rational`](https://docs.python.org/3.14/library/numbers.html#numbers.Rational).)

The `Integral` numbers come from `Rational`; they support left and right shifts via `<<` and `>>`, bitwise combinations through operators like `&` and `|`, and use as array indexes and slice boundaries.

For Python 3.0 the PEP gently restates the existing builtins [`round()`](https://docs.python.org/3.14/library/functions.html#round), [`math.floor()`](https://docs.python.org/3.14/library/math.html#math.floor), [`math.ceil()`](https://docs.python.org/3.14/library/math.html#math.ceil), and introduces a new one, [`math.trunc()`](https://docs.python.org/3.14/library/math.html#math.trunc), which 2.6 also receives. `math.trunc()` truncates toward zero, yielding the nearest `Integral` lying between zero and the argument it is given.

See also

[**PEP 3141**](https://peps.python.org/pep-3141/) - A Type Hierarchy for Numbers

PEP written by Jeffrey Yasskin.

[Scheme’s numerical tower](https://www.gnu.org/software/guile/manual/html_node/Numerical-Tower.html#Numerical-Tower), from the Guile manual.

[Scheme’s number datatypes](https://conservatory.scheme.org/schemers/Documents/Standards/R5RS/HTML/r5rs-Z-H-9.html#%_sec_6.2) from the R5RS Scheme specification.

[Subject index](INDEX.md) · [Previous source section](pep-3129-class-decorators.md) · [Next source section](the-fractions-module.md) · [Release/subject declaration](python-3-0.md)
