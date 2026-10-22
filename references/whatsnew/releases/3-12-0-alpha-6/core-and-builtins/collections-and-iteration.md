# Python 3.12.0 alpha 6 / core and builtins / collections and iteration

[gh-101967](https://github.com/python/cpython/issues/101967): Repair a possible segfault inside the `positional_only_passed_as_keyword` function when a new list is created.

[gh-87849](https://github.com/python/cpython/issues/87849): Have the `SEND` instruction leave its receiver sitting on the stack. With that, the specialized variant of `SEND` can bypass the chain of C calls and go straight to the `RESUME` inside the generator or coroutine.

[gh-100719](https://github.com/python/cpython/issues/100719): Drop the gi_code field from generator objects (likewise coroutine and async generator objects), since it duplicates information. A reference to the code object is already kept by the frame.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
