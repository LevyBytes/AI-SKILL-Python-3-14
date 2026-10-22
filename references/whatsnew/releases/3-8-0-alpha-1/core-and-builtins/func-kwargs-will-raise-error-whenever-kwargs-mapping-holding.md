# Python 3.8.0 alpha 1 / core and builtins / func kwargs will raise error whenever kwargs mapping holding

[bpo-35634](https://bugs.python.org/issue?@action=redirect&bpo=35634): `func(**kwargs)` will from now on raise an error whenever `kwargs` is a mapping holding several entries that share a key. An error already arose when other keyword arguments came before `**kwargs` starting with Python 3.6.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
