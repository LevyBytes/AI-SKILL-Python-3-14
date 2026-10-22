# Python 3.8.0 alpha 1 / core and builtins / text and unicode

[bpo-16806](https://bugs.python.org/issue?@action=redirect&bpo=16806): Correct `lineno` and `col_offset` for string tokens that span several lines.

[bpo-34854](https://bugs.python.org/issue?@action=redirect&bpo=34854): Resolved a crash when compiling string annotations that contain a lambda whose keyword-only argument carries no default value.

[bpo-34523](https://bugs.python.org/issue?@action=redirect&bpo=34523): Python now reads the filesystem encoding sooner while Python initialization is underway.

[bpo-33824](https://bugs.python.org/issue?@action=redirect&bpo=33824): Correct ?LC_ALL=C python3.7 -V?: reset the command line parser properly once the encoding shifts after the Python configuration is read.

[bpo-33475](https://bugs.python.org/issue?@action=redirect&bpo=33475): Resolved assorted bugs in turning annotations into strings and streamlined the parentheses in the string representation.

[bpo-32583](https://bugs.python.org/issue?@action=redirect&bpo=32583): Resolved a potential crash inside the builtin Unicode decoders that stemmed from out-of-bound writes triggered by custom decode error handlers.

[bpo-32285](https://bugs.python.org/issue?@action=redirect&bpo=32285): Added the function unicodedata.is_normalized, useful for testing whether a given string already sits in a particular normal form.

[bpo-35494](https://bugs.python.org/issue?@action=redirect&bpo=35494): Better syntax error messages for unbalanced parentheses inside an f-string.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
