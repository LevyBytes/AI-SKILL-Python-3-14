# Python 3.7.0 beta 1 / core and builtins / hasattr obj name along getattr obj name default run

[bpo-32544](https://bugs.python.org/issue?@action=redirect&bpo=32544): `hasattr(obj, name)` along with `getattr(obj, name, default)` run roughly 4 times quicker than before whenever `name` is missing and `obj` does not override `__getattr__` or `__getattribute__`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
