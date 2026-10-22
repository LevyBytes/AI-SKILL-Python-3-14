# What's New In Python 3.6 / secrets — os, random, secrets

### New Modules

### secrets

The chief reason for the brand-new [`secrets`](https://docs.python.org/3.14/library/secrets.html#module-secrets) module is to offer a clear, dependable route for generating cryptographically strong pseudo-random values fit for handling secrets, including account authentication, tokens, and the like.

Warning

Keep in mind the pseudo-random generators within the [`random`](https://docs.python.org/3.14/library/random.html#module-random) module are *NOT* meant for security work. Reach for [`secrets`](https://docs.python.org/3.14/library/secrets.html#module-secrets) on Python 3.6+ and for [`os.urandom()`](https://docs.python.org/3.14/library/os.html#os.urandom) on Python 3.5 and earlier.

See also

[**PEP 506**](https://peps.python.org/pep-0506/) – Adding A Secrets Module To The Standard Library

PEP written and implemented by Steven D’Aprano.

[Subject index](INDEX.md) · [Previous source section](other-language-changes.md) · [Next source section](array.md) · [Release/subject declaration](summary-release-highlights.md)
