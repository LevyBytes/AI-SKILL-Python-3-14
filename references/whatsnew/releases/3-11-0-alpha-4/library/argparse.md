# Python 3.11.0 alpha 4 / library / argparse

[bpo-26952](https://bugs.python.org/issue?@action=redirect&bpo=26952): When rendering usage for an empty mutually exclusive group, [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) now raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) carrying a clear message. It used to raise an obscure [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError) instead.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
