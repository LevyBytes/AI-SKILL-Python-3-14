# Python 3.13.0 alpha 2 / library / unicodedata

[gh-96954](https://github.com/python/cpython/issues/96954): Move the storage of unicode codepoint names onto a different data structure, a [directed acyclic word graph](https://en.wikipedia.org/wiki/Deterministic_acyclic_finite_state_automaton). The unicodedata shared library shrinks by roughly 440 KiB as a result. Carl Friedrich Bolz-Tereick contributed it, drawing on code from the PyPy project.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
