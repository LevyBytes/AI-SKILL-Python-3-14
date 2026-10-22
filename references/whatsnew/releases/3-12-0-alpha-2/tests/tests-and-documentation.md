# Python 3.12.0 alpha 2 / tests / tests and documentation

[gh-98903](https://github.com/python/cpython/issues/98903): The Python test suite now exits with code 4 whenever no test ran. The intent is to catch typos in test names and in test methods.

[gh-87390](https://github.com/python/cpython/issues/87390): Introduce tests covering star-unpacking under PEP 646, plus a handful of additional miscellaneous PEP 646 tests.

[gh-96853](https://github.com/python/cpython/issues/96853): Restored explicit coverage of `Py_Initialize` (and by extension `Py_InitializeEx`) to the embedding tests (the rest of the embedding tests moved over to `Py_InitializeFromConfig` back in Python 3.11)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
