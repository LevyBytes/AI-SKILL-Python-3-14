# 8.4. The `try` statement

### 8.4. The `try` statement

Exception handlers and/or cleanup code for a block of statements are designated by the `try` statement:

```text

try_stmt:  try1_stmt | try2_stmt | try3_stmt
try1_stmt: "try" ":" suite
           ("except" [expression "as" [identifier]] ":" suite)+
           ["else" ":" suite]
           ["finally" ":" suite]
try2_stmt: "try" ":" suite
           ("except" "*" expression "as" [identifier] ":" suite)+
           ["else" ":" suite]
           ["finally" ":" suite]
try3_stmt: "try" ":" suite
           "finally" ":" suite
```

You can read more about exceptions in the section [Exceptions](https://docs.python.org/3.14/reference/executionmodel.html#exceptions), and details about employing the [`raise`](https://docs.python.org/3.14/reference/simple_stmts.html#raise) statement to produce exceptions live in the section [The raise statement](https://docs.python.org/3.14/reference/simple_stmts.html#raise).

Changed in version 3.14: Grouping parentheses may now be left off, at your discretion, when several exception types are listed. See [**PEP 758**](https://peps.python.org/pep-0758/).

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Previous source section](the-for-statement.md) · [Following source section](except-clause-foo-to-foo.md)
