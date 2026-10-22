# What’s New In Python 3.12 / PEP 709: Comprehension inlining — symtable

### PEP 709: Comprehension inlining

Comprehensions for dictionaries, lists, and sets are now inlined, instead of building a throwaway function object every time a comprehension runs. Running a comprehension thereby becomes as much as twice as quick. Further specifics live in [**PEP 709**](https://peps.python.org/pep-0709/).

A comprehension’s iteration variables stay sealed off: they neither clobber an outer-scope variable bearing the same name nor remain visible once the comprehension ends. Inlining nevertheless brings a handful of observable changes:

- Tracebacks no longer carry a distinct frame for the comprehension, and tracing/profiling stops reporting the comprehension as a function call.

- For every comprehension, the [`symtable`](https://docs.python.org/3.14/library/symtable.html#module-symtable) module stops emitting a child symbol table; rather, that comprehension’s locals fold into the symbol table of the enclosing function.

- Invoking [`locals()`](https://docs.python.org/3.14/library/functions.html#locals) within a comprehension now picks up variables defined outside the comprehension, and it drops the synthetic `.0` variable that stood for the comprehension “argument”.

- When a comprehension loops straight over `locals()` (for example `[k for k in locals()]`), it can hit “RuntimeError: dictionary changed size during iteration” while tracing is active (such as during code coverage measurement). The same thing already happens with, say, `for k in locals():`. Sidestep the error by building a key list first to loop across: `keys = list(locals()); [k for k in keys]`.

(Contributed by Carl Meyer and Vladimir Matveev in [**PEP 709**](https://peps.python.org/pep-0709/).)

[Subject index](INDEX.md) · [Previous source section](pep-688-making-the-buffer-protocol-accessible-in-python.md) · [Next source section](improved-error-messages.md) · [Release/subject declaration](summary-release-highlights.md)
