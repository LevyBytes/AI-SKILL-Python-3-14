# Python 3.10.0 beta 1 / core and builtins / functions

[bpo-43682](https://bugs.python.org/issue?@action=redirect&bpo=43682): Static methods ([`@staticmethod`](https://docs.python.org/3.14/library/functions.html#staticmethod)) can now be invoked like ordinary functions. Victor Stinner wrote the patch.

[bpo-43682](https://bugs.python.org/issue?@action=redirect&bpo=43682): Static methods ([`@staticmethod`](https://docs.python.org/3.14/library/functions.html#staticmethod)) together with class methods ([`@classmethod`](https://docs.python.org/3.14/library/functions.html#classmethod)) now carry over the method attributes (`__module__`, `__name__`, `__qualname__`, `__doc__`, `__annotations__`) and gain a fresh `__wrapped__` attribute. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
