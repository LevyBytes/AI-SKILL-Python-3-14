# Python 3.11.0 alpha 1 / library / fnmatch

[bpo-42799](https://bugs.python.org/issue?@action=redirect&bpo=42799): Within [`fnmatch`](https://docs.python.org/3.14/library/fnmatch.html#module-fnmatch), the compiled-regex cache ([`functools.lru_cache()`](https://docs.python.org/3.14/library/functools.html#functools.lru_cache)) grew from 256 to 32768, touching the functions [`fnmatch.fnmatch()`](https://docs.python.org/3.14/library/fnmatch.html#fnmatch.fnmatch), [`fnmatch.fnmatchcase()`](https://docs.python.org/3.14/library/fnmatch.html#fnmatch.fnmatchcase), [`fnmatch.filter()`](https://docs.python.org/3.14/library/fnmatch.html#fnmatch.filter).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
