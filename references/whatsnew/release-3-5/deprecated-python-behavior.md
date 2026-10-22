# What’s New In Python 3.5 / Deprecated Python Behavior

### Deprecated Python Behavior

When a generator raises the [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) exception, that now emits a silent [`PendingDeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#PendingDeprecationWarning); it turns into a loud deprecation warning in Python 3.6 and raises a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) in Python 3.7. Consult PEP 479: Change StopIteration handling inside generators for details.

[Subject index](INDEX.md) · [Previous source section](new-keywords.md) · [Next source section](unsupported-operating-systems.md) · [Release/subject declaration](summary-release-highlights.md)
