# 8.6. The `match` statement

### 8.6. The `match` statement

Added in version 3.10.

Pattern matching is what the match statement provides. Syntax:

```text

match_stmt:   'match' subject_expr ":" NEWLINE INDENT case_block+ DEDENT
subject_expr: flexible_expression "," [flexible_expression_list [',']]
              | assignment_expression
case_block:   'case' patterns [guard] ":" suite
```

Note

In this section, single quotes mark [soft keywords](https://docs.python.org/3.14/reference/lexical_analysis.html#soft-keywords).

As its inputs, pattern matching accepts a pattern (which comes after `case`) plus a subject value (which comes after `match`). That pattern (it may hold subpatterns) is checked against the subject value. The possible results are:

- A match success or failure (also termed a pattern success or failure).

- Matched values may possibly be bound to a name. What this requires is taken up in more detail further on.

The `match` and `case` keywords are [soft keywords](https://docs.python.org/3.14/reference/lexical_analysis.html#soft-keywords).

See also

- [**PEP 634**](https://peps.python.org/pep-0634/) – Structural Pattern Matching: Specification

- [**PEP 636**](https://peps.python.org/pep-0636/) – Structural Pattern Matching: Tutorial

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Previous source section](the-with-statement-suite-to-suite.md) · [Following source section](overview.md)
