# 3.2.4.2. `numbers.Real` (`float`)

#### 3.2.4.2. [`numbers.Real`](https://docs.python.org/3.14/library/numbers.html#numbers.Real) ([`float`](https://docs.python.org/3.14/library/functions.html#float))

These stand for machine-level double precision floating-point numbers. The accepted range and the way overflow is dealt with are left to the underlying machine architecture (and the C or Java implementation), so you are at its mercy. Single-precision floating-point numbers are not offered by Python; the processor and memory savings that ordinarily justify them are overwhelmed by the cost of using objects in Python, so there is no point in burdening the language with two flavors of floating-point numbers.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](numbers-number.md) · [Previous source section](numbers-integral.md) · [Following source section](numbers-complex.md)
