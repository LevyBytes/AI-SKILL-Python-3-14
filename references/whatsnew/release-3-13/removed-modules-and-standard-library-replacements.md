# What's New In Python 3.13 / PEP 594: Remove "dead batteries" from the standard library — ctypes, email, email.compat32-message, email.message, hashlib, urllib.parse

### Removed Modules And APIs

### PEP 594: Remove "dead batteries" from the standard library

[**PEP 594**](https://peps.python.org/pep-0594/) put forward the removal of 19 modules from the standard library; these were nicknamed "dead batteries" given their historic, obsolete, or insecure character. Every module below had been deprecated back in Python 3.11 and is gone now:

- `aifc`

  - [standard-aifc](https://pypi.org/project/standard-aifc/): Use the redistribution of `aifc` library from PyPI.

- `audioop`

  - [audioop-lts](https://pypi.org/project/audioop-lts/): Use `audioop-lts` library from PyPI.

- `chunk`

  - [standard-chunk](https://pypi.org/project/standard-chunk/): Use the redistribution of `chunk` library from PyPI.

- `cgi` and `cgitb`

  - For `GET` and `HEAD` requests, `cgi.FieldStorage` can usually give way to [`urllib.parse.parse_qsl()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.parse_qsl), while `POST` and `PUT` requests can rely on the [`email.message`](https://docs.python.org/3.14/library/email.message.html#module-email.message) module or the [multipart](https://pypi.org/project/multipart/) library.

  - For `cgi.parse()`, invoke [`urllib.parse.parse_qs()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.parse_qs) straight on the query string you want, except when the input is `multipart/form-data`, in which case follow the substitution given below for `cgi.parse_multipart()`.

  - For `cgi.parse_header()`, lean on what the [`email`](https://docs.python.org/3.14/library/email.html#module-email) package provides, since it covers the very same MIME RFCs. As an illustration, using [`email.message.EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage):

```python
from email.message import EmailMessage

msg = EmailMessage()
msg['content-type'] = 'application/json; charset="utf8"'
main, params = msg.get_content_type(), msg['content-type'].params

```

  - For `cgi.parse_multipart()`, lean on what the [`email`](https://docs.python.org/3.14/library/email.html#module-email) package provides, since it covers the very same MIME RFCs, or turn to the [multipart](https://pypi.org/project/multipart/) library. As an illustration, the [`email.message.EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) and [`email.message.Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) classes.

  - [standard-cgi](https://pypi.org/project/standard-cgi/): and [standard-cgitb](https://pypi.org/project/standard-cgitb/): Use the redistribution of `cgi` and `cgitb` library from PyPI.

- `crypt` together with the private `_crypt` extension. Where you only need to hash a value, the [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) module can serve as a fitting stand-in. Failing that, several third-party offerings on PyPI exist:

  - [bcrypt](https://pypi.org/project/bcrypt/): Modern password hashing for your software and your servers.

  - [argon2-cffi](https://pypi.org/project/argon2-cffi/): The secure Argon2 password hashing algorithm.

  - [legacycrypt](https://pypi.org/project/legacycrypt/): [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) wrapper to the POSIX crypt library call and associated functionality.

  - [crypt_r](https://pypi.org/project/crypt_r/): Fork of the `crypt` module, wrapper to the *[crypt_r(3)](https://manpages.debian.org/crypt_r(3))* library call and associated functionality.

[Subject index](INDEX.md) · [Previous source section](optimizations.md) · [Next source section](removed-modules-and-third-party-replacements.md) · [Release/subject declaration](summary-release-highlights.md)
