# Python 3.12.0 alpha 1 / library / ssl

[gh-94199](https://github.com/python/cpython/issues/94199): The `ssl.wrap_socket()` function, deprecated in Python 3.7, is removed; in its place build a [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) object and invoke its [`ssl.SSLContext.wrap_socket`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.wrap_socket) method. Any package still leaning on `ssl.wrap_socket()` is both broken and insecure. That function neither emits a SNI TLS extension nor checks the server hostname. Such code falls under [**CWE 295**](https://cwe.mitre.org/data/definitions/295.html) Improper Certificate Validation. Victor Stinner wrote the patch.

[gh-94101](https://github.com/python/cpython/issues/94101): Directly building [`ssl.SSLSession`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSession) objects by hand is now disallowed, because doing so produced misconfigured instances that brought down the interpreter once their attributes were read.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
