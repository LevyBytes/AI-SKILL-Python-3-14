# What's New In Python 3.11 / PEP 646: Variadic generics — typing

### PEP 646: Variadic generics

[**PEP 484**](https://peps.python.org/pep-0484/) earlier brought in [`TypeVar`](https://docs.python.org/3.14/library/typing.html#typing.TypeVar), which lets you build generics parameterised by exactly one type. Now [**PEP 646**](https://peps.python.org/pep-0646/) contributes [`TypeVarTuple`](https://docs.python.org/3.14/library/typing.html#typing.TypeVarTuple), so a generic can be parameterised by an *arbitrary* count of types. Put differently, a `TypeVarTuple` acts as a *variadic* type variable, which in turn supports *variadic* generics.

That opens up many possibilities. Notably, it lets array-style containers in numeric libraries such as NumPy and TensorFlow carry the array *shape* in their type. As a result, static type checkers gain the ability to flag shape-related defects in code leaning on those libraries.

Consult [**PEP 646**](https://peps.python.org/pep-0646/) for the full treatment.

[Subject index](INDEX.md) · [Previous source section](new-features-related-to-type-hints.md) · [Next source section](pep655-required-and-optional-typeddict-items.md) · [Release/subject declaration](summary-release-highlights.md)
