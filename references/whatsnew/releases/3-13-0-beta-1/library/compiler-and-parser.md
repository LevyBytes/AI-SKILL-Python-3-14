# Python 3.13.0 beta 1 / library / compiler and parser

[gh-86650](https://github.com/python/cpython/issues/86650): Resolves an IndexError when parsing certain emails bearing an invalid Message-ID, such as the one-off addresses produced by Microsoft Outlook.

[bpo-40943](https://bugs.python.org/issue?@action=redirect&bpo=40943): Corrects several IndexError occurrences when parsing emails whose Message-ID, address, routes, and so on are truncated, for instance `example@`.

[bpo-30988](https://bugs.python.org/issue?@action=redirect&bpo=30988): Corrects parsing of emails whose invalid address headers carry a leading or trailing dot. The patch came from tsufeki.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
