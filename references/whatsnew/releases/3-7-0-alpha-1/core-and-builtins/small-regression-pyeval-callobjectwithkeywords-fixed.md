# Python 3.7.0 alpha 1 / core and builtins / small regression pyeval callobjectwithkeywords fixed

[bpo-29684](https://bugs.python.org/issue?@action=redirect&bpo=29684): A small regression in PyEval_CallObjectWithKeywords was fixed. It ought to raise TypeError whenever kwargs isn't a dict, but it could instead segv when args=NULL and kwargs isn't a dict.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
