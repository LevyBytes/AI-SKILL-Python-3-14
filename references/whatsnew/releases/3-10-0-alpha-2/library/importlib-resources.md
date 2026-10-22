# Python 3.10.0 alpha 2 / library / importlib resources

[bpo-41490](https://bugs.python.org/issue?@action=redirect&bpo=41490): Within `importlib.resources`, the `.path` method releases handles to zipfile objects earlier and more eagerly, supporting scenarios such as certifi keeping the context open while deleting the underlying zip file.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
