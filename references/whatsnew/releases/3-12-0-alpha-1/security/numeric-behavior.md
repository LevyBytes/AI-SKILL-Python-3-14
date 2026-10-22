# Python 3.12.0 alpha 1 / security / numeric behavior

[gh-97616](https://github.com/python/cpython/issues/97616): Repair the case of multiplying a list by an integer (`list *= int`): the integer overflow is now caught when the freshly allocated length approaches the maximum size. Jordan Limor flagged this issue; Victor Stinner supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
