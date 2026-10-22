# Python 3.6.1 release candidate 1 / library / functools lru cache honors pep keeps ordering keyword arguments

[bpo-29203](https://bugs.python.org/issue?@action=redirect&bpo=29203): functools.lru_cache() now honors [**PEP 468**](https://peps.python.org/pep-0468/) and keeps the ordering of keyword arguments. f(a=1, b=2) now gets cached apart from f(b=2, a=1), since the two calls could conceivably yield differing results.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
