# math — Special functions

### Special functions

 math.erf(*x*)

Give back the [error function](https://en.wikipedia.org/wiki/Error_function) at *x*.

You can lean on the `erf()` function to build classic statistical functions like the [cumulative standard normal distribution](https://en.wikipedia.org/wiki/Cumulative_distribution_function):

```python
def phi(x):
    'Cumulative distribution function for the standard normal distribution'
    return (1.0 + erf(x / sqrt(2.0))) / 2.0

```

Added in version 3.2.

 math.erfc(*x*)

Give back the complementary error function at *x*. The [complementary error function](https://en.wikipedia.org/wiki/Error_function) is defined as `1.0 - erf(x)`. It serves for large *x* values where subtracting from one would trigger a [loss of significance](https://en.wikipedia.org/wiki/Loss_of_significance).

Added in version 3.2.

 math.gamma(*x*)

Give back the [Gamma function](https://en.wikipedia.org/wiki/Gamma_function) at *x*.

Added in version 3.2.

 math.lgamma(*x*)

Give back the natural log of the Gamma function's absolute value evaluated at *x*.

Added in version 3.2.

[Subject index](INDEX.md) · [Previous](math-acosh-to-math-tanh.md) · [Continue](math-pi-to-math-nan.md) · [Owning module, declaration or section: math](math-mathematical-functions.md)
