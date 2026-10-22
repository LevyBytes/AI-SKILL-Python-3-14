# Python 3.7.0 alpha 1 / tests / random

[bpo-30357](https://bugs.python.org/issue?@action=redirect&bpo=30357): test_thread: its setUp() routine now calls support.threading_setup() and support.threading_cleanup() so it blocks until threads finish, which stops random spillover into later tests. Grzegorz Grzywacz authored the first version of the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
