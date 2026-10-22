# locals

locals()

Yield a mapping object that represents the present local symbol table, where the keys are the variable names and the values are the references currently bound to them.

Within module scope, and likewise when `exec()` or `eval()` runs with a lone namespace, this function hands back the identical namespace that `globals()` does.

Within class scope, it hands back the namespace destined to be forwarded to the metaclass constructor.

Whenever `exec()` or `eval()` runs with distinct local and global arguments, it hands back the local namespace that was supplied to the function call.

For every one of the situations described above, each `locals()` invocation inside a particular execution frame hands back the *same* mapping object. Edits performed through the mapping object that `locals()` returned are observable as local variables being assigned, reassigned, or deleted, and assigning, reassigning, or deleting local variables instantly alters what the returned mapping object holds.

Within an [optimized scope](https://docs.python.org/3.14/glossary.html#term-optimized-scope) (which covers functions, generators, and coroutines), each `locals()` invocation instead hands back a brand-new dictionary holding the present bindings of the function’s local variables together with any nonlocal cell references. Here, name binding edits applied through the returned dict are *not* propagated back to the matching local variables or nonlocal cell references. Conversely, when you assign, reassign, or delete local variables and nonlocal cell references, that does *not* alter what dictionaries returned earlier hold.

Invoking `locals()` within a comprehension inside a function, generator, or coroutine amounts to invoking it within the enclosing scope, with the difference that the comprehension’s initialised iteration variables are added in. In other scopes, it acts as though the comprehension were executing as a nested function.

Invoking `locals()` within a generator expression amounts to invoking it within a nested generator function.

Changed in version 3.12: The conduct of `locals()` inside a comprehension was revised in the way detailed by [**PEP 709**](https://peps.python.org/pep-0709/).

Changed in version 3.13: Per [**PEP 667**](https://peps.python.org/pep-0667/), the semantics for mutating the mapping objects this function returns are now specified. The conduct within [optimized scopes](https://docs.python.org/3.14/glossary.html#term-optimized-scope) is now what was described above. Apart from now being specified, the conduct within other scopes stays the same as in earlier versions.

[Builtin task index](INDEX.md).
