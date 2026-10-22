# Python 3.8.0 alpha 1 / idle / text and unicode

[bpo-33204](https://bugs.python.org/issue?@action=redirect&bpo=33204): IDLE: apply uniform coloring to invalid string prefixes. The "u" prefix on a string will not combine with "r" or with "f". Working from the right, color as large a valid portion of the prefix as you can. Update and broaden the colorizer test.

[bpo-32826](https://bugs.python.org/issue?@action=redirect&bpo=32826): Pass "encoding=utf-8" into open() within IDLE's test_help_about. Although the GUI test test_file_buttons() examines only the opening ascii-only lines, it broke on platforms where open() falls back to "ascii", since readline() reads and decodes far enough internally to hit a non-ascii character inside CREDITS.txt.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
