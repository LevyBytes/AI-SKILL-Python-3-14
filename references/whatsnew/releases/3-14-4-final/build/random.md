# Python 3.14.4 final / build / random

[gh-145801](https://github.com/python/cpython/issues/145801): If a Python build is PGO-optimized through GCC, the `-fprofile-update=atomic` option now applies atomic operations while profile information is updated. Using it lowers the chance of gcov Data Files (.gcda) becoming corrupted, which can lead to random GCC crashes. Victor Stinner supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
