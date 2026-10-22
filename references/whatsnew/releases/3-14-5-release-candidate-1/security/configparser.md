# Python 3.14.5 release candidate 1 / security / configparser

[gh-146333](https://github.com/python/cpython/issues/146333): Eliminate quadratic backtracking in the option-parsing regexes of [`configparser.RawConfigParser`](https://docs.python.org/3.14/library/configparser.html#configparser.RawConfigParser) (`OPTCRE` and `OPTCRE_NV`). A maliciously built config line loaded with whitespace could drive CPU usage sky-high.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
