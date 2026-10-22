# Python 3.9.0 alpha 3 / library / poplib

[bpo-39259](https://bugs.python.org/issue?@action=redirect&bpo=39259): [`POP3`](https://docs.python.org/3.14/library/poplib.html#poplib.POP3) and [`POP3_SSL`](https://docs.python.org/3.14/library/poplib.html#poplib.POP3_SSL) now raise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) whenever the constructor receives a timeout of zero, avoiding the creation of a non-blocking socket. Donghee Na wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
