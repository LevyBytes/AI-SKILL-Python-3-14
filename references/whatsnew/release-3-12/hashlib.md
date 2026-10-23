# What’s New In Python 3.12 / hashlib - hashlib

### hashlib

- Drop the pure Python build of the [`hashlib.pbkdf2_hmac()`](https://docs.python.org/3.14/library/hashlib.html#hashlib.pbkdf2_hmac) in [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib), deprecated back in Python 3.10. From Python 3.10 onward, OpenSSL 1.1.1 is a requirement ([**PEP 644**](https://peps.python.org/pep-0644/)): that OpenSSL release ships a speedier C implementation of `pbkdf2_hmac()`. (Contributed by Victor Stinner in [gh-94199](https://github.com/python/cpython/issues/94199).)

[Subject index](INDEX.md) · [Previous source section](gzip.md) · [Next source section](importlib.md) · [Release/subject declaration](summary-release-highlights.md)
