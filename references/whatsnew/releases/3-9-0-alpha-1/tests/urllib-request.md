# Python 3.9.0 alpha 1 / tests / urllib request

[bpo-37421](https://bugs.python.org/issue?@action=redirect&bpo=37421): The urllib.request tests now invoke [`urlcleanup()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.urlcleanup) so that temporary files left behind by `urlretrieve()` tests are deleted and the `_opener` global, set by `urlopen()` and any functions that call `urlopen()` indirectly, is cleared.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
