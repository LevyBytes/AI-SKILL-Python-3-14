# Python 3.13.0 alpha 5 / library / sys

[bpo-40818](https://bugs.python.org/issue?@action=redirect&bpo=40818): At startup the asyncio REPL now invokes [`sys.__interactivehook__`](https://docs.python.org/3.14/library/sys.html#sys.__interactivehook__). That hook's default implementation of `sys.__interactivehook__` brings auto-completion into the asyncio REPL. Rémi Lapeyre contributed this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
