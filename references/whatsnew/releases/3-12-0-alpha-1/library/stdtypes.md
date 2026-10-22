# Python 3.12.0 alpha 1 / library / stdtypes

[bpo-39264](https://bugs.python.org/issue?@action=redirect&bpo=39264): Adjusted `collections.UserDict.get()` so that it no longer invokes [`__missing__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__missing__) on a missing value. The result now lines up with how [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) behaves. Bar Harel provided the patch.

[bpo-47025](https://bugs.python.org/issue?@action=redirect&bpo=47025): Stop accepting [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) entries on [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
