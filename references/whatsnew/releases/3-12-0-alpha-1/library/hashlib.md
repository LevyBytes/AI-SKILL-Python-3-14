# Python 3.12.0 alpha 1 / library / hashlib

[gh-94199](https://github.com/python/cpython/issues/94199): [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib): The pure Python version of [`hashlib.pbkdf2_hmac()`](https://docs.python.org/3.14/library/hashlib.html#hashlib.pbkdf2_hmac), which had been deprecated as of Python 3.10, has been dropped. From Python 3.10 onward OpenSSL 1.1.1 is mandatory ([**PEP 644**](https://peps.python.org/pep-0644/)), and that release ships a faster C-based `pbkdf2_hmac()`. Victor Stinner supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
