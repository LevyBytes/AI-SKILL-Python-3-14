# What's New In Python 3.10 / PEP 634: Structural Pattern Matching / Complex patterns and the wildcard

#### Complex patterns and the wildcard

So far, every example has placed `_` on its own within the closing case statement. A wildcard also fits inside richer patterns, for instance `('error', code, _)`. To illustrate:

```python
match test_variable:
    case ('warning', code, 40):
        print("A warning has been received.")
    case ('error', code, _):
        print(f"An error {code} occurred.")

```

For that case, `test_variable` matches against ("error", code, 100) as well as ("error", code, 800).

[Subject index](INDEX.md) · [Previous source section](pep-634-structural-pattern-matching-nested-patterns.md) · [Next source section](pep-634-structural-pattern-matching-guard.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](pep-634-structural-pattern-matching.md)
