# Python 3.5.1 release candidate 1 / core and builtins / corrected input prompts redirected stdout whenever sys stdout fileno fails

[bpo-24402](https://bugs.python.org/issue?@action=redirect&bpo=24402): Corrected input() so it prompts to the redirected stdout whenever sys.stdout.fileno() fails.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
