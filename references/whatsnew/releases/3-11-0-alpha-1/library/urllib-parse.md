# Python 3.11.0 alpha 1 / library / urllib parse

[bpo-44002](https://bugs.python.org/issue?@action=redirect&bpo=44002): [`urllib.parse`](https://docs.python.org/3.14/library/urllib.parse.html#module-urllib.parse) now relies on `functool.lru_cache()` for its internal URL splitting and quoting caches in place of hand-rolling them as though it were the ’90s.

That undocumented internal `Quoted` class API of [`urllib.parse`](https://docs.python.org/3.14/library/urllib.parse.html#module-urllib.parse) has been marked deprecated and is slated to disappear in 3.14.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
