# What's New In Python 3.6 / PEP 526: Syntax for variable annotations

### PEP 526: Syntax for variable annotations

[**PEP 484**](https://peps.python.org/pep-0484/) set the convention for type annotations on function parameters, otherwise called type hints. The present PEP grows Python's grammar so that variable types — covering both class variables and instance variables — can be annotated:

```python
primes: List[int] = []

captain: str  # Note: no initial value!

class Starship:
    stats: Dict[str, int] = {}

```

Much like function annotations, the interpreter assigns no special semantics to variable annotations; it merely records them in the `__annotations__` attribute on the class or module.

Unlike variable declarations found in statically typed languages, the point of annotation syntax is to offer a convenient route for handing structured type metadata to third party tools and libraries through the abstract syntax tree and the `__annotations__` attribute.

See also

[**PEP 526**](https://peps.python.org/pep-0526/) — Syntax for variable annotations.

Authored as a PEP by Ryan Gonzalez, Philip House, Lisa Roach, Guido van Rossum, and Ivan Levkivskyi; the implementation came from Ivan Levkivskyi.

Tools that use or will use the new syntax: [mypy](https://www.mypy-lang.org/), [pytype](https://github.com/google/pytype), PyCharm, etc.

[Subject index](INDEX.md) · [Previous source section](pep-498-formatted-string-literals.md) · [Next source section](pep-515-underscores-in-numeric-literals.md) · [Release/subject declaration](summary-release-highlights.md)
