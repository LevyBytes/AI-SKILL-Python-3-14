# Python 3.7.0 beta 2 / idle / text and unicode

[bpo-32826](https://bugs.python.org/issue?@action=redirect&bpo=32826): Supply "encoding=utf-8" to open() inside IDLE's test_help_about. The GUI test test_file_buttons() inspects only the opening ascii-only lines, yet it broke on systems where open() falls back to "ascii" because readline() internally reads and decodes far enough forward to hit a non-ascii character within CREDITS.txt.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
