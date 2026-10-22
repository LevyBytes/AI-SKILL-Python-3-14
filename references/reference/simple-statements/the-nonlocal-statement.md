# 7.13. The `nonlocal` statement

### 7.13. The `nonlocal` statement

```text

nonlocal_stmt: "nonlocal" identifier ("," identifier)*
```

Where a function's or class's definition nests (sits enclosed) inside the definitions of other functions, its nonlocal scopes amount to the local scopes of those enclosing functions. By way of the `nonlocal` statement, the identifiers it lists come to refer to names already bound in nonlocal scopes. This lets encapsulated code reassign such nonlocal identifiers. Where a name is bound across more than one nonlocal scope, the closest binding wins. Where a name has no binding in any nonlocal scope, or where no nonlocal scope exists at all, a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) gets raised.

Across the entire scope of a function or class body the `nonlocal` statement holds. Where a variable is used or assigned before its nonlocal declaration within the scope, a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) gets raised.

See also

[**PEP 3104**](https://peps.python.org/pep-3104/) - Access to Names in Outer Scopes

Where the `nonlocal` statement is specified.

**Programmer’s note:** the parser is what `nonlocal` directs, and it bears only on code parsed together with it. Refer to the note covering the `global` statement.

[Subject index](INDEX.md) · [Owning language section](simple-statements.md) · [Previous source section](the-global-statement.md) · [Following source section](the-type-statement.md)
