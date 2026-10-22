# 7.11.1. Future statements

### 7.11.1. Future statements

A *future statement* tells the compiler that some specific module ought to be compiled with syntax or semantics that a named upcoming Python release will offer once the feature turns standard.

The point of the future statement is to smooth the move to later Python versions that bring backward-incompatible language changes. It lets you adopt the new features one module at a time ahead of the release in which the feature becomes standard.

```text

future_stmt: "from" "__future__" "import" feature "as" [identifier]
             ("," feature "as" [identifier])*
             | "from" "__future__" "import" "(" feature "as" [identifier]
             ("," feature "as" [identifier])* [","] ")"
feature:     identifier
```

A future statement has to sit close to the module's start. Ahead of a future statement, the only lines allowed are:

- the module docstring (where one exists),

- comments,

- blank lines, and

- further future statements.

The single feature still demanding a future statement is `annotations` (consult [**PEP 563**](https://peps.python.org/pep-0563/)).

Python 3 continues to recognize every historical feature the future statement once switched on. That roster covers `absolute_import`, `division`, `generators`, `generator_stop`, `unicode_literals`, `print_function`, `nested_scopes` and `with_statement`. Each is now superfluous since it is permanently on, retained merely for backward compatibility.

At compile time a future statement gets singled out for special handling: shifts in the semantics of core constructs are frequently realized by emitting different code. A new feature might even bring incompatible new syntax along (a fresh reserved word, for instance), whereupon the compiler could have to parse the module in another way. Calls like these cannot be deferred to runtime.

Within any particular release, the compiler is aware of which feature names exist, and it throws a compile-time error whenever a future statement names a feature it does not recognize.

The plain runtime semantics match those of any import statement: a standard module [`__future__`](https://docs.python.org/3.14/library/__future__.html#module-__future__) exists, covered further on, and it gets imported the usual way as the future statement runs.

What makes the runtime semantics noteworthy hinges on the particular feature the future statement switches on.

Note that the statement below carries nothing special about it:

```python
import __future__ [as name]

```

That one is no future statement; it is a run-of-the-mill import statement bearing no special semantics nor any syntax restrictions.

Whenever the built-in functions [`exec()`](https://docs.python.org/3.14/library/functions.html#exec) and [`compile()`](https://docs.python.org/3.14/library/functions.html#compile) are called from inside a module `M` that holds a future statement, the code they compile defaults to the new syntax or semantics the future statement brings. Optional arguments to `compile()` let you govern this — turn to that function's documentation for the particulars.

Entering a future statement at an interactive interpreter prompt keeps it active throughout the remainder of that interpreter session. Should an interpreter launch with the [`-i`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-i) option, be handed a script name to run, and that script carry a future statement, it stays active within the interactive session that opens once the script finishes.

See also

[**PEP 236**](https://peps.python.org/pep-0236/) - Back to the __future__

Where the __future__ mechanism was first proposed.

[Subject index](INDEX.md) · [Owning language section](simple-statements.md) · [Owning language section](the-import-statement.md) · [Previous source section](the-import-statement.md) · [Following source section](the-global-statement.md)
