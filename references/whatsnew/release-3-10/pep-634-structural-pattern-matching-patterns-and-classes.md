# What's New In Python 3.10 / PEP 634: Structural Pattern Matching / Patterns and classes

#### Patterns and classes

When you build your data around classes, a pattern can be the class name trailed by an argument list that looks like a constructor call. Such a pattern is able to pull instance attributes into variables:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def location(point):
    match point:
        case Point(x=0, y=0):
            print("Origin is the point's location.")
        case Point(x=0, y=y):
            print(f"Y={y} and the point is on the y-axis.")
        case Point(x=x, y=0):
            print(f"X={x} and the point is on the x-axis.")
        case Point():
            print("The point is located somewhere else on the plane.")
        case _:
            print("Not a point")

```

[Subject index](INDEX.md) · [Previous source section](literal-and-variable-patterns.md) · [Next source section](class-pattern-positional-parameters.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](pep-634-structural-pattern-matching.md)
