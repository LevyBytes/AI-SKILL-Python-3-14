# Python 3.9.0 beta 1 / core and builtins / text and unicode

[bpo-40246](https://bugs.python.org/issue?@action=redirect&bpo=40246): The specialised error message for invalid string prefixes, added back in [bpo-40246](https://bugs.python.org/issue?@action=redirect&bpo=40246), is being undone over backward-compatibility worries about strings placed right after a reserved keyword with no whitespace separating them. Things like `bg="#d00" if clear else"#fca"` stopped parsing, an unacceptable break to introduce with so little warning.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
