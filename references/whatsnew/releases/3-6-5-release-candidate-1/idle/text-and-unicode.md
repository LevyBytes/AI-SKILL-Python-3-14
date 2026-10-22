# Python 3.6.5 release candidate 1 / idle / text and unicode

[bpo-32837](https://bugs.python.org/issue?@action=redirect&bpo=32837): Relying on the system- and location-dependent default encoding for open() is a poor choice for IDLE’s system- and location-independent files.

[bpo-32826](https://bugs.python.org/issue?@action=redirect&bpo=32826): Insert “encoding=utf-8” into the open() call inside IDLE’s test_help_about. Although the GUI test test_file_buttons() inspects only the opening ascii-only lines, it broke wherever open() falls back to ‘ascii’ by default. The cause: readline() decodes ahead internally, reaching far enough that it meets a non-ascii character sitting in CREDITS.txt.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
