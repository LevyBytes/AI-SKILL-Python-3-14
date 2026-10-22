# Python 3.8.0 alpha 4 / tests / test time test monotonic altered assert only lower bound elapsed time following

[bpo-36454](https://bugs.python.org/issue?@action=redirect&bpo=36454): test_time.test_monotonic() was altered to assert only the lower bound on elapsed time following a sleep command instead of the upper bound. Doing so avoids needless failures on sluggish buildbots. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
