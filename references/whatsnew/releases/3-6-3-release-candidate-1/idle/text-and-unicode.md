# Python 3.6.3 release candidate 1 / idle / text and unicode

[bpo-29910](https://bugs.python.org/issue?@action=redirect&bpo=29910): IDLE will no longer erase a character once a region gets commented out via a key shortcut. A `return 'break'` was added to cover this plus other possible clashes between IDLE bindings and the default key bindings.

[bpo-31477](https://bugs.python.org/issue?@action=redirect&bpo=31477): IDLE - Sharpen the rstrip entry within the doc. Trailing-whitespace stripping covers more than plain spaces. String literals spanning multiple lines are not bypassed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
