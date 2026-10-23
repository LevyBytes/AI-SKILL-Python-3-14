# What's New In Python 3.7 / PEP 563: Postponed Evaluation of Annotations - __future__, typing

### New Features

### PEP 563: Postponed Evaluation of Annotations

When type hints arrived in Python, they exposed two obvious pain points in how annotations behave, a feature first added by [**PEP 3107**](https://peps.python.org/pep-3107/) and later sharpened by [**PEP 526**](https://peps.python.org/pep-0526/):

- annotations were limited to names already visible in the enclosing scope, meaning forward references of every variety were unavailable; and

- writing annotations into source slowed down how quickly Python programs began running.

Deferring when annotations get evaluated resolves both problems. Rather than emitting bytecode that runs annotation expressions when the definition executes, the compiler keeps each annotation as a string mirroring the AST of that expression. Should you need it, [`typing.get_type_hints()`](https://docs.python.org/3.14/library/typing.html#typing.get_type_hints) resolves annotations while the program runs. Where that resolution isn't needed — the usual situation — storing the annotations costs less (because the interpreter interns short strings) and trims startup overhead.

From a usability angle, forward references in annotations are now permitted, so this code is legal:

```python
class C:
    @classmethod
    def from_string(cls, source: str) -> C:
        ...

    def validate_b(self, obj: B) -> bool:
        ...

class B:
    ...

```

Because the shift is not backward compatible, you opt into the new conduct one module at a time in Python 3.7 through a [`__future__`](https://docs.python.org/3.14/library/__future__.html#module-__future__) import:

```python
from __future__ import annotations

```

Python 3.10 will make it the default.

See also

[**PEP 563**](https://peps.python.org/pep-0563/): Postponed evaluation of annotations

PEP written and implemented by ??ukasz Langa.

[Subject index](INDEX.md) · [Previous source section](summary-release-highlights.md) · [Next source section](pep-538-legacy-c-locale-coercion.md) · [Release/subject declaration](summary-release-highlights.md)
