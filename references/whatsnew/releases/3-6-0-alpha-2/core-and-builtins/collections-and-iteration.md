# Python 3.6.0 alpha 2 / core and builtins / collections and iteration

[bpo-23275](https://bugs.python.org/issue?@action=redirect&bpo=23275): Permit assignment to an empty target list wrapped in round brackets: () = iterable.

[bpo-27243](https://bugs.python.org/issue?@action=redirect&bpo=27243): Revised the __aiter__ protocol: rather than handing back an awaitable that resolves into an asynchronous iterator, the asynchronous iterator ought to be returned outright. Sticking with the old approach raises a PendingDeprecationWarning.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
