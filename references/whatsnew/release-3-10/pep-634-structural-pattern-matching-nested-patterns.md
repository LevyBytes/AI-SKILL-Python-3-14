# What's New In Python 3.10 / PEP 634: Structural Pattern Matching / Nested patterns

#### Nested patterns

Nesting of patterns has no fixed limit. To give an example, were our data a brief list of points, matching it might look like:

```python
match points:
    case []:
        print("No points in the list.")
    case [Point(0, 0)]:
        print("The origin is the only point in the list.")
    case [Point(x, y)]:
        print(f"A single point {x}, {y} is in the list.")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two points on the Y axis at {y1}, {y2} are in the list.")
    case _:
        print("Something else is found in the list.")

```

[Subject index](INDEX.md) · [Previous source section](class-pattern-positional-parameters.md) · [Next source section](pattern-matching-complex-patterns-and-wildcard.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](pep-634-structural-pattern-matching.md)
