# What's New In Python 3.10 / PEP 634: Structural Pattern Matching / Patterns with a literal and variable

#### Patterns with a literal and variable

A pattern can resemble an unpacking assignment, and it may serve to bind variables. Here a data point gets unpacked into its x-coordinate together with its y-coordinate:

```python
# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

```

That opening pattern carries a pair of literals, `(0, 0)`, and you can view it as a broadening of the literal pattern given earlier. The following two patterns blend a literal with a variable, where the variable *binds* a value out of the subject (`point`). The fourth pattern grabs two values, making it conceptually akin to the unpacking assignment `(x, y) = point`.

[Subject index](INDEX.md) · [Previous source section](literal-patterns-without-wildcard.md) · [Next source section](pep-634-structural-pattern-matching-patterns-and-classes.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](pep-634-structural-pattern-matching.md)
