# What's New In Python 3.10 / PEP 634: Structural Pattern Matching / Simple pattern: match to a literal

#### Simple pattern: match to a literal

Consider this example showing pattern matching at its most basic: a value, the subject, paired against a handful of literals, the patterns. Below, `status` plays the role of the match statement's subject. Each case statement holds a pattern, where literals stand for request status codes. Once a match lands, the action attached to that case runs:

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

```

Should the function above receive a `status` of 418, "I'm a teapot" comes back. Should the function above receive a `status` of 500, the case statement holding `_` matches as a wildcard, so "Something's wrong with the internet" comes back. Observe that final block: the variable name `_` behaves as a *wildcard* and guarantees the subject always matches. Supplying `_` is optional.

Multiple literals can be merged into one pattern with `|` ("or"):

```python
case 401 | 403 | 404:
    return "Not allowed"

```

[Subject index](INDEX.md) · [Previous source section](pep-634-structural-pattern-matching-declarative-approach.md) · [Next source section](literal-patterns-without-wildcard.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](pep-634-structural-pattern-matching.md)
