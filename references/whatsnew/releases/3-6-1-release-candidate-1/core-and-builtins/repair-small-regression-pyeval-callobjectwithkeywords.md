# Python 3.6.1 release candidate 1 / core and builtins / repair small regression pyeval callobjectwithkeywords

[bpo-29684](https://bugs.python.org/issue?@action=redirect&bpo=29684): Repair a small regression of PyEval_CallObjectWithKeywords. Whenever kwargs is not a dict, it ought to raise TypeError. A segv could nonetheless result if args=NULL together with a kwargs that is not a dict.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
