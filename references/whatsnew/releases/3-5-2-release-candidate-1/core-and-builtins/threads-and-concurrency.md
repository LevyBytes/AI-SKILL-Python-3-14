# Python 3.5.2 release candidate 1 / core and builtins / threads and concurrency

[bpo-26154](https://bugs.python.org/issue?@action=redirect&bpo=26154): A new private function _PyThreadState_UncheckedGet() is introduced for retrieving the current Python thread state without raising a fatal error when the result is NULL. Code should now call this helper rather than reaching directly into the _PyThreadState_Current variable. Since Python 3.5.1 that variable has no longer been exposed, which conceals the precise layout of the atomic C types and sidesteps compiler problems.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
