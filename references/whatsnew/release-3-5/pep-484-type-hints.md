# What’s New In Python 3.5 / PEP 484 - Type Hints - typing

### PEP 484 - Type Hints

Syntax for function annotations has existed in Python ever since the 3.0 release ([**PEP 3107**](https://peps.python.org/pep-3107/)), though what those annotations were supposed to mean stayed unspecified.

Practice revealed that most uses of function annotations served to attach type hints onto a function's parameters and its return value. It grew clear that Python developers would gain a lot if the standard library shipped the foundational definitions and tooling for annotating types.

To deliver those standard definitions and tooling, [**PEP 484**](https://peps.python.org/pep-0484/) brings in a [provisional module](https://docs.python.org/3.14/glossary.html#term-provisional-API), bundled with a handful of conventions covering cases in which annotations happen to be missing.

To illustrate, here's a small function where the annotations declare the parameter type as well as the return type:

```python
def greeting(name: str) -> str:
    return 'Hello ' + name

```

Although you can reach those annotations at runtime via the customary [`__annotations__`](https://docs.python.org/3.14/reference/datamodel.html#object.__annotations__) attribute, *no automatic type checking happens at runtime*. The expectation instead is that a standalone off-line type checker (for example [mypy](https://mypy-lang.org)) handles source analysis on demand.

Unions, generic types, and a distinctive type called [`Any`](https://docs.python.org/3.14/library/typing.html#typing.Any) — which stays consistent with (that is, assignable both to and from) every type — are all covered by the type system.

See also

- [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) module documentation

- [**PEP 484**](https://peps.python.org/pep-0484/) – Type Hints

PEP authored by Guido van Rossum, Jukka Lehtosalo, and Łukasz Langa; the implementation was done by Guido van Rossum.

- [**PEP 483**](https://peps.python.org/pep-0483/) – The Theory of Type Hints

PEP written by Guido van Rossum

[Subject index](INDEX.md) · [Previous source section](pep-461-percent-formatting-support-for-bytes-and-bytearray.md) · [Next source section](pep471-scandir-directory-iteration.md) · [Release/subject declaration](summary-release-highlights.md)
