# What's New In Python 3.10 / PEP 634: Structural Pattern Matching / Other Key Features

#### Other Key Features

A number of further key features:

- Just as with unpacking assignments, tuple and list patterns carry precisely the same meaning and in fact match any arbitrary sequence. Strictly, the subject is required to be a sequence. Hence a notable caveat: patterns will not match iterators. On top of that, to head off a frequent slip-up, sequence patterns will not match strings.

- Wildcards are honored by sequence patterns: `[x, y, *rest]` and `(x, y, *rest)` behave much like wildcards within unpacking assignments. What follows `*` is allowed to be `_` as well, so `(x, y, *_)` matches any sequence holding at least two elements without binding what remains.

- Mapping patterns: `{"bandwidth": b, "latency": l}` pulls the `"bandwidth"` and `"latency"` values out of a dict. In contrast to sequence patterns, surplus keys get ignored. A wildcard `**rest` is honored too. (Though `**_` would add nothing, so it is disallowed.)

- The `as` keyword lets you capture subpatterns:

```python
case (Point(x1, y1), Point(x2, y2) as p2): ...

```

This ties x1, y1, x2, y2 just as you'd anticipate even without the `as` clause, and ties p2 to the whole second element of the subject.

- Equality drives the comparison of most literals. The singletons `True`, `False` and `None`, however, are compared via identity.

- Patterns can refer to named constants. Such named constants are required to be dotted names, which stops the constant from being read as a capture variable:

```python
from enum import Enum
class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2

color = Color.GREEN
match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")

```

The complete specification appears in [**PEP 634**](https://peps.python.org/pep-0634/). The motivation and rationale sit in [**PEP 635**](https://peps.python.org/pep-0635/), while [**PEP 636**](https://peps.python.org/pep-0636/) holds an extended tutorial.

[Subject index](INDEX.md) · [Previous source section](pep-634-structural-pattern-matching-guard.md) · [Next source section](optional-encodingwarning-and-encoding-locale-option.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](pep-634-structural-pattern-matching.md)
