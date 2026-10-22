# What’s New In Python 3.5 / PEP 485: A function for testing approximate equality — cmath, math

### PEP 485: A function for testing approximate equality

[**PEP 485**](https://peps.python.org/pep-0485/) introduces the [`math.isclose()`](https://docs.python.org/3.14/library/math.html#math.isclose) and [`cmath.isclose()`](https://docs.python.org/3.14/library/cmath.html#cmath.isclose) helpers, which report whether a pair of numbers sit approximately equal or ?close? to one another. The verdict on closeness rests on supplied absolute plus relative tolerances. The relative tolerance caps the permitted gap between the `isclose` arguments, scaled against the bigger of the two magnitudes:

```python
>>> import math
>>> a = 5.0
>>> b = 4.99998
>>> math.isclose(a, b, rel_tol=1e-5)
True
>>> math.isclose(a, b, rel_tol=1e-6)
False

```

You can alternatively check a pair of numbers against an absolute tolerance, which has to stay non-negative:

```python
>>> import math
>>> a = 5.0
>>> b = 4.99998
>>> math.isclose(a, b, abs_tol=0.00003)
True
>>> math.isclose(a, b, abs_tol=0.00001)
False

```

See also

[**PEP 485**](https://peps.python.org/pep-0485/) ? A function for testing approximate equality

[Subject index](INDEX.md) · [Next source section](pep486-launcher-virtual-environment-awareness.md) · [Release/subject declaration](summary-release-highlights.md)
