# Python 3.6.6 release candidate 1 / core and builtins / repaired sigint handler no longer resets sig dfl interpreter shutdown

[bpo-30654](https://bugs.python.org/issue?@action=redirect&bpo=30654): Repaired the SIGINT handler so it no longer resets to SIG_DFL at interpreter shutdown even where a custom handler had been installed beforehand. Philipp Kerling provided the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
