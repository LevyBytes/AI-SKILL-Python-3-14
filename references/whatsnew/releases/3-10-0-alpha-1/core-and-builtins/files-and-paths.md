# Python 3.10.0 alpha 1 / core and builtins / files and paths

[bpo-41056](https://bugs.python.org/issue?@action=redirect&bpo=41056): Corrects a reference into freed stack space at startup while assembling sys.path through a relative symlink, in the case where code came in via -c. (surfaced by Coverity)

[bpo-41431](https://bugs.python.org/issue?@action=redirect&bpo=41431): Tunes `dict_merge()` for the dict-copy path (for instance `dict(d)` together with `{}.update(d)`).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
