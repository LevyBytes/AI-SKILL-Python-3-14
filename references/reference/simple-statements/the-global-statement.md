# 7.12. The `global` statement

### 7.12. The `global` statement

```text

global_stmt: "global" identifier ("," identifier)*
```

With the `global` statement, the identifiers it lists get read as globals. Assigning to a global variable would be unachievable absent `global`, though free variables can point at globals without any global declaration.

Across the whole of the present scope (a module, a function body or a class definition) the `global` statement holds. Where a variable is used or assigned before its global declaration within the scope, a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) gets raised.

Every variable is already global at module level, leaving a `global` statement with nothing to do. Even so, variables still must not be used or assigned ahead of their `global` declaration. That rule is loosened at the interactive prompt ([REPL](https://docs.python.org/3.14/glossary.html#term-REPL)).

**Programmer’s note:** the parser is what `global` directs. It bears only on code parsed alongside the `global` statement itself. Specifically, a `global` statement sitting in a string or code object passed to the built-in [`exec()`](https://docs.python.org/3.14/library/functions.html#exec) function leaves the code block *containing* the function call untouched, and code held within such a string stays unaffected by any `global` statements in the code surrounding the call. The very same goes for the [`eval()`](https://docs.python.org/3.14/library/functions.html#eval) and [`compile()`](https://docs.python.org/3.14/library/functions.html#compile) functions.

[Subject index](INDEX.md) · [Owning language section](simple-statements.md) · [Previous source section](future-statements.md) · [Following source section](the-nonlocal-statement.md)
