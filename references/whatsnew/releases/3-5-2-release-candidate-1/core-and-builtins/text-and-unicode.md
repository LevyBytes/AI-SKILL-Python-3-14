# Python 3.5.2 release candidate 1 / core and builtins / text and unicode

[bpo-26464](https://bugs.python.org/issue?@action=redirect&bpo=26464): A defect in str.translate() is corrected for the case where the string is ASCII, the first replacement strips a character, and a later replacement supplies either a non-ASCII character or a string of more than one character. This was a regression that first appeared in Python 3.5.0.

[bpo-26302](https://bugs.python.org/issue?@action=redirect&bpo=26302): Behavior was corrected so that a comma is no longer treated as a permitted character within cookie names.

[bpo-25709](https://bugs.python.org/issue?@action=redirect&bpo=25709): A problem involving in-place string concatenation together with the utf-8 cache has been fixed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
