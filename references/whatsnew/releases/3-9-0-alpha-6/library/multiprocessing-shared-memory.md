# Python 3.9.0 alpha 6 / library / multiprocessing shared memory

[bpo-38891](https://bugs.python.org/issue?@action=redirect&bpo=38891): Correct the linear-time behaviour of `__getitem__` and `__setitem__` on [`multiprocessing.shared_memory.ShareableList`](https://docs.python.org/3.14/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.ShareableList). This sidesteps quadratic cost while looping over a `ShareableList`. Thomas Krennwallner contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
