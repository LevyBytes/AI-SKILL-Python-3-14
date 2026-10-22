# What's new in Python 3.14 / PEP 765: Control flow in `finally` blocks — warnings

### PEP 765: Control flow in [`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) blocks

Whenever a [`return`](https://docs.python.org/3.14/reference/simple_stmts.html#return), [`break`](https://docs.python.org/3.14/reference/simple_stmts.html#break), or [`continue`](https://docs.python.org/3.14/reference/simple_stmts.html#continue) statement results in exiting a [`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) block, the compiler now produces a [`SyntaxWarning`](https://docs.python.org/3.14/library/exceptions.html#SyntaxWarning). [**PEP 765**](https://peps.python.org/pep-0765/) specifies this change.

When the change proves awkward (for instance where code linting makes the warnings redundant), the [warning filter](https://docs.python.org/3.14/library/warnings.html#warning-filter) lets you switch off every syntax warning by adding `ignore::SyntaxWarning` as a filter. You may state this alongside a filter that promotes other warnings into errors (for example by passing `-Werror -Wignore::SyntaxWarning` as CLI options, or by setting `PYTHONWARNINGS=error,ignore::SyntaxWarning`).

Keep in mind that applying such a filter at runtime through the [`warnings`](https://docs.python.org/3.14/library/warnings.html#module-warnings) module suppresses the warning only in code compiled *after* the filter gets adjusted. Whatever was compiled ahead of the filter adjustment (say, when a module is imported) continues to emit the syntax warning.

(Contributed by Irit Katriel in [gh-130080](https://github.com/python/cpython/issues/130080).)

[Subject index](INDEX.md) · [Previous source section](pep-758-allow-except-and-except-expressions-without-brackets.md) · [Next source section](garbage-collection.md) · [Release/subject declaration](summary-release-highlights.md)
