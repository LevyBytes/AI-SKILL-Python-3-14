# Match class attributes, positional fields and nested patterns

When classes organize your data, you can write the class name trailed by an argument list that looks like a constructor call, except it can also pull attributes out into variables:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

```

Positional parameters work with certain builtin classes that establish an ordering over their attributes (dataclasses, for example). You can likewise fix a particular position for attributes in patterns by assigning the `__match_args__` special attribute inside your classes. Were it set to (“x”, “y”), every one of the patterns below is equivalent (and each one binds the `y` attribute to the `var` variable):

```python
Point(1, var)
Point(1, y=var)
Point(x=1, y=var)
Point(y=var, x=1)

```

A good habit when reading patterns is to view them as a stretched-out version of whatever you’d place to the left of an assignment, so you can figure out which variables end up holding what. Within a match statement, only the bare names (such as `var` earlier) get assigned. Dotted names (for instance `foo.bar`), attribute names (the `x=` and `y=` above), and class names (the ones marked by the “(…)” following them, like `Point` earlier) are never targets of assignment.

There is no limit to how deeply patterns may nest. Suppose, for instance, we hold a brief list of Points with `__match_args__` in place; we might match it as follows:

```python
class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")

```

[Subject index](INDEX.md) · [Previous source section](match-literals-or-patterns-and-tuple-captures.md) · [Following source section](match-guards-mapping-patterns-captures-and-named-constants.md) · [Related tutorial example and explanation](match-literals-or-patterns-and-tuple-captures.md) · [Related tutorial example and explanation](match-guards-mapping-patterns-captures-and-named-constants.md)
