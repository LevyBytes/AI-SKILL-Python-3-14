# Python 3.8.0 alpha 1 / core and builtins / resolved reset sigint handler back sig dfl upon interpreter shutdown

[bpo-30654](https://bugs.python.org/issue?@action=redirect&bpo=30654): Resolved the reset of the SIGINT handler back to SIG_DFL upon interpreter shutdown that happened even where a custom handler had been installed earlier. Patch by Philipp Kerling.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
