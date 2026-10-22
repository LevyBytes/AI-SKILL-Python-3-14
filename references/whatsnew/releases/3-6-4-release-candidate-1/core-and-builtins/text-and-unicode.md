# Python 3.6.4 release candidate 1 / core and builtins / text and unicode

[bpo-31825](https://bugs.python.org/issue?@action=redirect&bpo=31825): Repaired an OverflowError inside the ‘unicode-escape’ codec and inside codecs.escape_decode() while decoding an escaped non-ascii byte.

[bpo-31315](https://bugs.python.org/issue?@action=redirect&bpo=31315): Repair an assertion failure in imp.create_dynamic() that fires when spec.name is not a string. Oren Milman wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
