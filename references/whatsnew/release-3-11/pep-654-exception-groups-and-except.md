# What's New In Python 3.11 / PEP 654: Exception Groups and `except*`

### PEP 654: Exception Groups and `except*`

[**PEP 654**](https://peps.python.org/pep-0654/) brings language machinery that lets code raise and deal with several independent exceptions at once. The builtin types [`ExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#ExceptionGroup) and [`BaseExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#BaseExceptionGroup) let you bundle exceptions and surface them as a unit, while the fresh [`except*`](https://docs.python.org/3.14/reference/compound_stmts.html#except-star) form extends [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) so it can select subgroups within an exception group.

Consult [**PEP 654**](https://peps.python.org/pep-0654/) for the full treatment.

[Subject index](INDEX.md) · [Previous source section](pep-657-fine-grained-error-locations-in-tracebacks.md) · [Next source section](pep-678-exceptions-can-be-enriched-with-notes.md) · [Release/subject declaration](summary-release-highlights.md)
