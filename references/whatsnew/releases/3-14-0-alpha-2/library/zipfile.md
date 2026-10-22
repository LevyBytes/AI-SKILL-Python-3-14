# Python 3.14.0 alpha 2 / library / zipfile

[gh-120754](https://github.com/python/cpython/issues/120754): Revise the unbounded `read` calls inside [`zipfile`](https://docs.python.org/3.14/library/zipfile.html#module-zipfile) so they pass an explicit `size` that caps how many bytes they can consume. This likewise revises handling of the ZIP max comment size to follow the standard rather than reading comments that run one byte over.

[gh-126565](https://github.com/python/cpython/issues/126565): Boost [`zipfile.Path.open()`](https://docs.python.org/3.14/library/zipfile.html#zipfile.Path.open) performance for the non-reading modes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
