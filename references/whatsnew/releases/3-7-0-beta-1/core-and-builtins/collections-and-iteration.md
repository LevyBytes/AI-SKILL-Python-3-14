# Python 3.7.0 beta 1 / core and builtins / collections and iteration

[bpo-32703](https://bugs.python.org/issue?@action=redirect&bpo=32703): Correct a coroutine's ResourceWarning that appeared when an active error was set at the moment it was being finalized.

[bpo-28685](https://bugs.python.org/issue?@action=redirect&bpo=28685): Speed up list.sort() and sorted() by employing type-specialized comparisons wherever feasible.

[bpo-32690](https://bugs.python.org/issue?@action=redirect&bpo=32690): The locals() dictionary now shows up in the lexical order in which the variables were defined. Formerly, that order came out reversed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
