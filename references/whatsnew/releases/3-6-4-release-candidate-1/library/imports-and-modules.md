# Python 3.6.4 release candidate 1 / library / imports and modules

[bpo-31334](https://bugs.python.org/issue?@action=redirect&bpo=31334): Corrected `poll.poll([timeout])` within the `select` module so that arbitrary negative timeouts work on every OS where the value may only be a non-negative integer or -1. Riccardo Coccioli wrote the patch.

[bpo-28556](https://bugs.python.org/issue?@action=redirect&bpo=28556): A pair of small `typing` module fixes: permit shallow copies of generic-class instances, and improve how `__init_subclass__` cooperates with generics. Ivan Levkivskyi opened the original PRs.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
