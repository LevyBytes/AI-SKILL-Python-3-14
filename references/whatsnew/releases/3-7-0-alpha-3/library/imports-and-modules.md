# Python 3.7.0 alpha 3 / library / imports and modules

[bpo-31334](https://bugs.python.org/issue?@action=redirect&bpo=31334): Repair `poll.poll([timeout])` in the `select` module for any negative timeout across every OS where the value must be either a non-negative integer or -1. Riccardo Coccioli supplied the patch.

[bpo-28556](https://bugs.python.org/issue?@action=redirect&bpo=28556): Brings two small fixes to the `typing` module: shallow copying of generic-class instances is permitted, and the interplay between `__init_subclass__` and generics is improved. Ivan Levkivskyi opened the original PRs.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
