# Match guards, mapping patterns, captures and named constants

A pattern may carry an extra `if` clause, called a “guard”. When the guard evaluates to false, `match` moves on to the next case block. Be aware that the value capture takes place ahead of the guard’s evaluation:

```python
match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")

```

A few more notable traits of this statement:

- Just as with unpacking assignments, tuple patterns and list patterns mean precisely the same thing and in fact match any sequence. One notable exception: they will not match iterators or strings.

- Sequence patterns allow extended unpacking: `[x, y, *rest]` and `(x, y, *rest)` behave much like unpacking assignments. The name following `*` is permitted to be `_` as well, so `(x, y, *_)` matches any sequence holding two or more items while leaving the rest unbound.

- Mapping patterns: `{"bandwidth": b, "latency": l}` pulls the `"bandwidth"` and `"latency"` values out of a dictionary. In contrast to sequence patterns, additional keys are simply skipped. An unpacking of the form `**rest` is supported as well. (Yet `**_` would serve no purpose, so it isn’t permitted.)

- The `as` keyword lets you capture subpatterns:

```python
case (Point(x1, y1), Point(x2, y2) as p2): ...

```

binds the input’s second element to `p2` (provided that the input happens to be a two-point sequence)

- Equality governs the comparison of most literals; the singletons `True`, `False` and `None`, however, are matched by identity.

- Named constants are allowed within patterns. They have to be dotted names, which stops them from being read as capture variables:

```python
from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")

```

For a fuller walkthrough along with more examples, take a look at [**PEP 636**](https://peps.python.org/pep-0636/), which is presented in tutorial form.

[Subject index](INDEX.md) · [Previous source section](match-class-attributes-positional-fields-and-nested-patterns.md) · [Following source section](defining-functions.md) · [Related tutorial example and explanation](match-literals-or-patterns-and-tuple-captures.md) · [Related tutorial example and explanation](match-class-attributes-positional-fields-and-nested-patterns.md) · [Point class and positional pattern setup](match-class-attributes-positional-fields-and-nested-patterns.md)
