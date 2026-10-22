# 8.6.1. Overview

### 8.6.1. Overview

The following outlines how a match statement flows logically:

1.

Evaluating the subject expression `subject_expr` yields a subject value. Where that subject expression holds a comma, [the standard rules](https://docs.python.org/3.14/library/stdtypes.html#typesseq-tuple) are applied to build a tuple.

2.

Every pattern inside a `case_block` is tried against the subject value. Below you will find the precise conditions under which each attempt passes or fails. While matching, a pattern may also bind some or all of its plain names, and the exact binding behavior differs by pattern kind, as documented further down. **Whatever names a successful match binds persist beyond the block that ran and stay usable once the match statement is over**.

Note

Subpatterns can sometimes pass even when the overall match ends up failing. Therefore you should not assume that any binding survives a failed match, nor should you assume a variable keeps its prior value once a match fails. Because the actual outcome depends on the implementation, it can differ between interpreters. That latitude is granted deliberately so that distinct implementations are free to introduce optimizations.

3.

When a pattern passes, its accompanying guard, should one exist, is then evaluated. At that point every name binding is certain to already be in place.

  - Should the guard yield true, or no guard is supplied, the `block` inside `case_block` runs.

  - If not, control moves on to the following `case_block`, handled exactly as outlined above.

  - When no additional case blocks remain, execution of the match statement finishes.

Note

As a rule, code should not depend on whether a given pattern actually gets evaluated. Some interpreters may stash values or apply other optimizations that bypass redundant evaluations.

Here is an example match statement:

```python
>>> flag = False
>>> match (100, 200):
...    case (100, 300):  # Mismatch: 200 != 300
...        print('Case 1')
...    case (100, 200) if flag:  # Successful match, but guard fails
...        print('Case 2')
...    case (100, y):  # Matches and binds y to 200
...        print(f'Case 3, y: {y}')
...    case _:  # Pattern not attempted
...        print('Case 4, I match anything!')
...
Case 3, y: 200

```

Here, the `if flag` clause acts as a guard. The following section covers guards in more detail.

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Owning language section](the-match-statement.md) · [Previous source section](the-match-statement.md) · [Following source section](guards.md)
