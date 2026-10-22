# Python 3.8.0 alpha 2 / core and builtins / should main interpreter terminate because uncaught keyboardinterrupt process exits

[bpo-1054041](https://bugs.python.org/issue?@action=redirect&bpo=1054041): Should the main interpreter terminate because of an uncaught KeyboardInterrupt, the process from now on exits in the proper fashion so that its parent process can recognize that a SIGINT or ^C ended it. Shells and batch scripts can thereby learn that the user requested they halt.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
