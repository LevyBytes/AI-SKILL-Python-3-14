# What's New In Python 3.10 / PEP 634: Structural Pattern Matching / Patterns and classes / Patterns with positional parameters

##### Patterns with positional parameters

Positional parameters work with certain builtin classes that supply an ordering over their attributes (e.g. dataclasses). You may likewise pin down a particular position for attributes within patterns by assigning the `__match_args__` special attribute on your classes. Were it set to ("x", "y"), all of the following patterns are equivalent (and each binds the `y` attribute to the `var` variable):

```python
Point(1, var)
Point(1, y=var)
Point(x=1, y=var)
Point(y=var, x=1)

```

[Subject index](INDEX.md) · [Previous source section](pep-634-structural-pattern-matching-patterns-and-classes.md) · [Next source section](pep-634-structural-pattern-matching-nested-patterns.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](pep-634-structural-pattern-matching.md) · [Release/subject declaration](pep-634-structural-pattern-matching-patterns-and-classes.md)
