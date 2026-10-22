# What's New In Python 3.10 / PEP 634: Structural Pattern Matching / Syntax and operations

#### Syntax and operations

Pattern matching follows this general syntax:

```python
match subject:
    case <pattern_1>:
        <action_1>
    case <pattern_2>:
        <action_2>
    case <pattern_3>:
        <action_3>
    case _:
        <action_wildcard>

```

A match statement accepts an expression, then weighs its value against a run of patterns laid out in one or more case blocks. To be precise, pattern matching works by:

1.

drawing on data that carries a type and a shape (the `subject`)

2.

evaluating the `subject` in the `match` statement

3.

checking the subject against every pattern inside a `case` statement, working downward from the top until one matches.

4.

running the action tied to the pattern of the match that succeeded

5.

Should no precise match be found, the closing case, a wildcard `_`, where present, serves as the matching case. Should no precise match be found and there is no wildcard case, the whole match block does nothing.

[Subject index](INDEX.md) · [Previous source section](pep-634-structural-pattern-matching.md) · [Next source section](pep-634-structural-pattern-matching-declarative-approach.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](pep-634-structural-pattern-matching.md)
