# What's New In Python 3.10 / PEP 634: Structural Pattern Matching / Guard

#### Guard

An `if` clause, termed a "guard", can be attached to a pattern. Should the guard turn out false, `match` proceeds to attempt the following case block. Be aware that value capture takes place ahead of evaluating the guard:

```python
match point:
    case Point(x, y) if x == y:
        print(f"The point is located on the diagonal Y=X at {x}.")
    case Point(x, y):
        print(f"Point is not on the diagonal.")

```

[Subject index](INDEX.md) · [Previous source section](pattern-matching-complex-patterns-and-wildcard.md) · [Next source section](pep-634-structural-pattern-matching-other-key-features.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](pep-634-structural-pattern-matching.md)
