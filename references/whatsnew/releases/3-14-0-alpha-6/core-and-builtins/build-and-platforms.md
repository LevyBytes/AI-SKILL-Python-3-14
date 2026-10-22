# Python 3.14.0 alpha 6 / core and builtins / build and platforms

[gh-129964](https://github.com/python/cpython/issues/129964): A JIT crash on Windows on Arm has been resolved. Diego Russo and Brandt Bucher supplied the patch.

[gh-130396](https://github.com/python/cpython/issues/130396): On linux, and on other systems that define `_GNU_SOURCE`, the real stack limits taken from *[pthread_getattr_np(3)](https://manpages.debian.org/pthread_getattr_np(3))* are now used when working out C stack protection limits.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
