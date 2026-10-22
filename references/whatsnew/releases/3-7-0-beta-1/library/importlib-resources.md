# Python 3.7.0 beta 1 / library / importlib resources

[bpo-32248](https://bugs.python.org/issue?@action=redirect&bpo=32248): Introduce [`importlib.resources`](https://docs.python.org/3.14/library/importlib.resources.html#module-importlib.resources) along with `importlib.abc.ResourceReader` to serve as one consistent API for pulling resources held inside packages. Any loader that wants resource-reading support has to supply the `get_resource_reader()` method. Both file-based and zipimport-based loaders ship these APIs. In favor of this new interface, [`importlib.abc.ResourceLoader`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.ResourceLoader) is now deprecated.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
