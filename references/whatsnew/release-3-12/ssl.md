# What’s New In Python 3.12 / ssl — os, ssl

### ssl

- Drop the `ssl.RAND_pseudo_bytes()` function of [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl), deprecated back in Python 3.6: switch to [`os.urandom()`](https://docs.python.org/3.14/library/os.html#os.urandom) or [`ssl.RAND_bytes()`](https://docs.python.org/3.14/library/ssl.html#ssl.RAND_bytes) instead. (Contributed by Victor Stinner in [gh-94199](https://github.com/python/cpython/issues/94199).)

- Drop the `ssl.match_hostname()` function. Python 3.7 deprecated it. From Python 3.7 on, OpenSSL handles the hostname matching and Python stopped calling the `ssl.match_hostname()` function. (Contributed by Victor Stinner in [gh-94199](https://github.com/python/cpython/issues/94199).)

- Drop the `ssl.wrap_socket()` function, deprecated back in Python 3.7: instead, build a [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) object and invoke its [`ssl.SSLContext.wrap_socket`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.wrap_socket) method. Whatever package still calls `ssl.wrap_socket()` is broken and insecure. That function omits a SNI TLS extension and skips validation of the server hostname. The code falls under [**CWE 295**](https://cwe.mitre.org/data/definitions/295.html) (Improper Certificate Validation). (Contributed by Victor Stinner in [gh-94199](https://github.com/python/cpython/issues/94199).)

[Subject index](INDEX.md) · [Previous source section](sqlite3.md) · [Next source section](unittest.md) · [Release/subject declaration](summary-release-highlights.md)
