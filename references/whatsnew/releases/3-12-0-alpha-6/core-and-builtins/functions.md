# Python 3.12.0 alpha 6 / core and builtins / functions

[gh-74895](https://github.com/python/cpython/issues/74895): For [`int`](https://docs.python.org/3.14/library/functions.html#int) **port** values that fall outside the C long range, [`socket.getaddrinfo`](https://docs.python.org/3.14/library/socket.html#socket.getaddrinfo) no longer throws [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError). Reporting on out-of-range values is left to the underlying string-based C library API. You might instead see a [`socket.gaierror`](https://docs.python.org/3.14/library/socket.html#socket.gaierror) `SAI_SERVICE`, or possibly no error whatsoever, given that not every platform's C library raises one.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
