# Python 3.7.0 release candidate 1 / core and builtins / repaired sigint handler being reset sig dfl interpreter shutdown even

[bpo-30654](https://bugs.python.org/issue?@action=redirect&bpo=30654): Repaired the SIGINT handler being reset to SIG_DFL at interpreter shutdown even after a custom handler had been installed earlier. Patch by Philipp Kerling.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
