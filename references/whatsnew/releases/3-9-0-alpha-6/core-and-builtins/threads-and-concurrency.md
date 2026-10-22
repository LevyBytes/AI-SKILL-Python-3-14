# Python 3.9.0 alpha 6 / core and builtins / threads and concurrency

[bpo-40082](https://bugs.python.org/issue?@action=redirect&bpo=40082): Correct the signal handler: it at this point relies on the main interpreter every time, in place of attempting to fetch the current Python thread state.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
