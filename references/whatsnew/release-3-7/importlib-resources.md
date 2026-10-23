# What's New In Python 3.7 / importlib.resources - importlib.resources

### importlib.resources

A fresh [`importlib.resources`](https://docs.python.org/3.14/library/importlib.resources.html#module-importlib.resources) module supplies a handful of new APIs plus one new ABC for reaching, opening, and reading *resources* held within packages. Think of resources as roughly file-like items bundled in packages, though they don't have to exist as genuine files on the underlying file system. To enable this fresh API, a module loader can expose a `get_resource_reader()` function that hands back a `importlib.abc.ResourceReader` instance. The built-in loaders for file paths as well as for zip files both back this.

Contributed by Barry Warsaw and Brett Cannon in [bpo-32248](https://bugs.python.org/issue?@action=redirect&bpo=32248).

See also

[importlib_resources](https://importlib-resources.readthedocs.io/en/latest/) ? a PyPI backport for earlier Python versions.

[Subject index](INDEX.md) · [Previous source section](dataclasses.md) · [Next source section](argparse.md) · [Release/subject declaration](summary-release-highlights.md)
