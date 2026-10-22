# Python 3.9.0 alpha 1 / windows / exceptions

[bpo-25172](https://bugs.python.org/issue?@action=redirect&bpo=25172): Attempting to import the `crypt` module under Windows now raises an [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) whose message clarifies that Windows does not support it. Elsewhere, when the backing `_crypt` module is missing, the ImportError carries text describing the issue.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
