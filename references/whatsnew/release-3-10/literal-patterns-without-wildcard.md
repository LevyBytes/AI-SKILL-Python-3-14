# What's New In Python 3.10 / PEP 634: Structural Pattern Matching / Simple pattern: match to a literal / Behavior without the wildcard

##### Behavior without the wildcard

Were we to alter the earlier example by dropping its last case block, it would read:

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"

```

Absent the `_` inside a case statement, it is possible no match turns up. When none turns up, nothing happens. To give an example, passing a `status` of 500 results in a no-op.

[Subject index](INDEX.md) · [Previous source section](literal-pattern-matching.md) · [Next source section](literal-and-variable-patterns.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](pep-634-structural-pattern-matching.md) · [Release/subject declaration](literal-pattern-matching.md)
