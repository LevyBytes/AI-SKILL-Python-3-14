# Python 3.14.0 beta 1 / core and builtins / collections and iteration

[gh-100239](https://github.com/python/cpython/issues/100239): Specialisation is added for `BINARY_OP/SUBSCR` over list and slice.

[gh-127682](https://github.com/python/cpython/issues/127682): When a generator expression is built and run, `__iter__` is no longer invoked twice. Building a generator expression over a non-interable will now raise only once the generator expression actually runs. This aligns generator expression behavior with that of other generators.

[gh-132261](https://github.com/python/cpython/issues/132261): For annotations and annotate functions on classes, the internal storage now relies on different keys within the class dictionary. Several edge cases in which access to the `__annotate__` and `__annotations__` attributes behaved unpredictably are thereby removed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
