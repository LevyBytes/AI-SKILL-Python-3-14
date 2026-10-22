# Python 3.5.0 alpha 1 / core and builtins / text and unicode

[bpo-15859](https://bugs.python.org/issue?@action=redirect&bpo=15859): When handed something that isn't a Unicode object, PyUnicode_EncodeFSDefault(), PyUnicode_EncodeMBCS() and PyUnicode_EncodeCodePage() now throw an exception. For PyUnicode_EncodeFSDefault(), that already held true on non-Windows platforms. Campbell Barton wrote the patch.

[bpo-23321](https://bugs.python.org/issue?@action=redirect&bpo=23321): Fixed a crash within str.decode() that occurred when the error handler returned a replacement string exceeding the length of the malformed input data.

[bpo-22286](https://bugs.python.org/issue?@action=redirect&bpo=22286): The "backslashreplace" error handlers now operate during decoding and translating too.

[bpo-20335](https://bugs.python.org/issue?@action=redirect&bpo=20335): The bytes constructor now throws TypeError whenever encoding or errors is given alongside a non-string argument. Renaud Blanch's patch served as the basis.

[bpo-22643](https://bugs.python.org/issue?@action=redirect&bpo=22643): Fix integer overflow in Unicode case operations (upper, lower, title, swapcase, casefold).

[bpo-22520](https://bugs.python.org/issue?@action=redirect&bpo=22520): Repaired the overflow check while building the repr of a unicode object.

[bpo-22518](https://bugs.python.org/issue?@action=redirect&bpo=22518): Resolved integer overflow problems within latin-1 encoding.

[bpo-22215](https://bugs.python.org/issue?@action=redirect&bpo=22215): These days ValueError, not TypeError, is raised whenever a str or bytes argument holds a forbidden null character or byte.

[bpo-22082](https://bugs.python.org/issue?@action=redirect&bpo=22082): Clear interned strings in slotdefs.

- Upgrade Unicode database to Unicode 7.0.0.

[bpo-12546](https://bugs.python.org/issue?@action=redirect&bpo=12546): Permit `\x00` as a fill character across the str, int, float, and complex __format__ methods.

[bpo-13598](https://bugs.python.org/issue?@action=redirect&bpo=13598): Adjust string.Formatter so replacement fields can auto-number themselves. Its behavior now agrees with str.format() here. Phil Elson and Ramchandra Apte contributed the patches.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
