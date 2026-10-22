# Python 3.6.2 release candidate 1 / core and builtins / text and unicode

[bpo-30682](https://bugs.python.org/issue?@action=redirect&bpo=30682): Dropped an overly strict assertion that broke for a few f-strings, for example `eval("f'\n'")` and `eval("f'\r'")`.

[bpo-29104](https://bugs.python.org/issue?@action=redirect&bpo=29104): Repaired the parsing of backslashes inside f-strings.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
