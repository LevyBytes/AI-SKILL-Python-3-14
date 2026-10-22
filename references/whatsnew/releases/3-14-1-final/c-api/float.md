# Python 3.14.1 final / c api / float

[gh-141042](https://github.com/python/cpython/issues/141042): Produce qNaN within [`PyFloat_Pack2()`](https://docs.python.org/3.14/c-api/float.html#c.PyFloat_Pack2) plus [`PyFloat_Pack4()`](https://docs.python.org/3.14/c-api/float.html#c.PyFloat_Pack4), if during conversion toward a narrower precision floating-point format — what remains of the payload after truncation will be zero. Sergey B Kirpichev supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
