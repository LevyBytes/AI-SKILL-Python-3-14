# What’s New In Python 3.5 / PEP 492 - Coroutines with async and await syntax

Note

Changed in version 3.5.2: From CPython 3.5.2 onward, `__aiter__` is allowed to hand back [asynchronous iterators](https://docs.python.org/3.14/glossary.html#term-asynchronous-iterator) directly. Handing back an [awaitable](https://docs.python.org/3.14/glossary.html#term-awaitable) object instead produces a [`PendingDeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#PendingDeprecationWarning).

See more details in the [Asynchronous Iterators](https://docs.python.org/3.14/reference/datamodel.html#async-iterators) documentation section.

See also

[**PEP 492**](https://peps.python.org/pep-0492/) – Coroutines with async and await syntax

PEP written and implemented by Yury Selivanov.

[Subject index](INDEX.md) · [Previous source section](pep492-async-await-coroutine-examples.md) · [Next source section](pep-465-a-dedicated-infix-operator-for-matrix-multiplication.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](pep492-async-await-coroutine-examples.md)
