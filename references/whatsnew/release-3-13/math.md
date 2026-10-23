# What's New In Python 3.13 / math - math

### math

- A freshly added [`fma()`](https://docs.python.org/3.14/library/math.html#math.fma) function carries out fused multiply-add work. It evaluates `x * y + z` using just one rounding step, sidestepping any precision lost in between. The implementation wraps C99's `fma()` and matches the IEEE 754 ?fusedMultiplyAdd? specification on its special cases. (Contributed by Mark Dickinson and Victor Stinner in [gh-73468](https://github.com/python/cpython/issues/73468).)

[Subject index](INDEX.md) · [Previous source section](marshal.md) · [Next source section](mimetypes.md) · [Release/subject declaration](summary-release-highlights.md)
