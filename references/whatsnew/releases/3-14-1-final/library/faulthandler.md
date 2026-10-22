# Python 3.14.1 final / library / faulthandler

[gh-125434](https://github.com/python/cpython/issues/125434): On Windows, [`faulthandler`](https://docs.python.org/3.14/library/faulthandler.html#module-faulthandler) now shows the thread name. Victor Stinner contributed the patch.

[gh-140815](https://github.com/python/cpython/issues/140815): [`faulthandler`](https://docs.python.org/3.14/library/faulthandler.html#module-faulthandler) is now able to spot an invalid or freed frame or code object. Victor Stinner authored the patch.

[gh-137185](https://github.com/python/cpython/issues/137185): Address a possible async-signal-safety problem inside [`faulthandler`](https://docs.python.org/3.14/library/faulthandler.html#module-faulthandler) that arose while dumping C stack traces.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
