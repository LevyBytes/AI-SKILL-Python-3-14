# Python 3.11.0 alpha 1 / library / mimetypes

[bpo-35474](https://bugs.python.org/issue?@action=redirect&bpo=35474): Invoking [`mimetypes.guess_all_extensions()`](https://docs.python.org/3.14/library/mimetypes.html#mimetypes.guess_all_extensions) under `strict=False` will no longer influence whatever a subsequent `strict=True` call returns. On top of that, editing the returned list no longer touches the global state.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
