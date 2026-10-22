# Python 3.14.5 release candidate 1 / build / random

[gh-148535](https://github.com/python/cpython/issues/148535): Stop applying the `gcc -fprofile-update=atomic` flag on i686. That flag had been introduced to address a random GCC internal error on the PGO build ([gh-145801](https://github.com/python/cpython/issues/145801)) brought on by corrupted profile data (.gcda files). The catch is that it drags the PGO build down enormously (as much as 47x slower) on i686. Because that GCC internal error has not shown up on i686 to date, `-fprofile-update=atomic` is no longer applied there. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
