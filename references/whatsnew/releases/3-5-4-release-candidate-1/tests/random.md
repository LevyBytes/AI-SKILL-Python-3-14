# Python 3.5.4 release candidate 1 / tests / random

[bpo-30357](https://bugs.python.org/issue?@action=redirect&bpo=30357): test_thread: setUp() now relies on support.threading_setup() together with support.threading_cleanup() so it waits for threads to finish, preventing random side effects on later tests. Grzegorz Grzywacz wrote the initial patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
