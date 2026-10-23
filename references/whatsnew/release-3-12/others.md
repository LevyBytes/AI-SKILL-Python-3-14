# What’s New In Python 3.12 / Others - ctypes, ftplib, http.client, imaplib, poplib, smtplib

### Others

- Drop the `suspicious` rule out of both the documentation `Makefile` and `Doc/tools/rstlint.py`, preferring [sphinx-lint](https://github.com/sphinx-contrib/sphinx-lint) for that role. (Contributed by Julien Palard in [gh-98179](https://github.com/python/cpython/issues/98179).)

- Drop the *keyfile* plus *certfile* parameters out of the [`ftplib`](https://docs.python.org/3.14/library/ftplib.html#module-ftplib), [`imaplib`](https://docs.python.org/3.14/library/imaplib.html#module-imaplib), [`poplib`](https://docs.python.org/3.14/library/poplib.html#module-poplib) and [`smtplib`](https://docs.python.org/3.14/library/smtplib.html#module-smtplib) modules, together with the *key_file*, *cert_file* and *check_hostname* parameters out of the [`http.client`](https://docs.python.org/3.14/library/http.client.html#module-http.client) module, every one of which had been deprecated since Python 3.6. Reach for the *context* parameter (named *ssl_context* over in `imaplib`) instead. (Contributed by Victor Stinner in [gh-94172](https://github.com/python/cpython/issues/94172).)

- Drop the `Jython` compatibility hacks out of a handful of stdlib modules plus their tests. (Contributed by Nikita Sobolev in [gh-99482](https://github.com/python/cpython/issues/99482).)

- Drop the `_use_broken_old_ctypes_structure_semantics_` flag out of the [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) module. (Contributed by Nikita Sobolev in [gh-99285](https://github.com/python/cpython/issues/99285).)

[Subject index](INDEX.md) · [Previous source section](zipimport.md) · [Next source section](porting-to-python-3-12.md) · [Release/subject declaration](summary-release-highlights.md)
