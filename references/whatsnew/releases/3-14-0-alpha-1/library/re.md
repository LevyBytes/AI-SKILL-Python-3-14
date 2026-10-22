# Python 3.14.0 alpha 1 / library / re

[gh-120244](https://github.com/python/cpython/issues/120244): Plug a memory leak in [`re.sub()`](https://docs.python.org/3.14/library/re.html#re.sub) that occurred when the replacement string held backreferences.

[gh-111259](https://github.com/python/cpython/issues/111259): The [`re`](https://docs.python.org/3.14/library/re.html#module-re) engine now treats patterns such as `"[\s\S]"` or `"\s|\S"`, which accept any character, just as efficiently as a dot paired with the `DOTALL` flag (`"(?s:.)"`).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
