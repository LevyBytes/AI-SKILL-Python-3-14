# What's New In Python 3.4 / Other Build and C API Changes - operator

### Other Build and C API Changes

- A new [`PyType_GetSlot()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetSlot) function joined the stable ABI, letting you pull function pointers out of named type slots while working with the limited API. (Contributed by Martin von Löwis in [bpo-17162](https://bugs.python.org/issue?@action=redirect&bpo=17162).)

- > A new `Py_SetStandardStreamEncoding()` pre-initialization API allows applications embedding the CPython interpreter to reliably force a particular encoding and error handler for the standard streams. (Contributed by Bastien Montagne and Nick Coghlan in [bpo-16129](https://bugs.python.org/issue?@action=redirect&bpo=16129).)

- The bulk of Python C APIs that leave string arguments unchanged are now properly flagged as taking `const char *` in place of `char *`. (Contributed by Serhiy Storchaka in [bpo-1772673](https://bugs.python.org/issue?@action=redirect&bpo=1772673).)

- A fresh shell flavor of `python-config` works even where no python interpreter is on hand (cross compilation, say).

- > [`PyUnicode_FromFormat()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromFormat) now supports width and precision specifications for `%s`, `%A`, `%U`, `%V`, `%S`, and `%R`. (Contributed by Ysj Ray and Victor Stinner in [bpo-7330](https://bugs.python.org/issue?@action=redirect&bpo=7330).)

- A new function [`PyStructSequence_InitType2()`](https://docs.python.org/3.14/c-api/tuple.html#c.PyStructSequence_InitType2) rounds out the already-present [`PyStructSequence_InitType()`](https://docs.python.org/3.14/c-api/tuple.html#c.PyStructSequence_InitType) function. What sets it apart is that it yields `0` when it succeeds and `-1` upon failure.

- The CPython source compiles cleanly now under the address sanity checking facilities found in newer GCC and clang releases: false alarms coming from the small object allocator have been quieted. (Contributed by Dhiru Kholia in [bpo-18596](https://bugs.python.org/issue?@action=redirect&bpo=18596).)

- The Windows build has adopted [Address Space Layout Randomization](https://en.wikipedia.org/wiki/Address_space_layout_randomization) together with [Data Execution Prevention](https://en.wikipedia.org/wiki/Data_Execution_Prevention). (Contributed by Christian Heimes in [bpo-16632](https://bugs.python.org/issue?@action=redirect&bpo=16632).)

- A new function [`PyObject_LengthHint()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_LengthHint) serves as the C API counterpart to [`operator.length_hint()`](https://docs.python.org/3.14/library/operator.html#operator.length_hint). (Contributed by Armin Ronacher in [bpo-16148](https://bugs.python.org/issue?@action=redirect&bpo=16148).)

[Subject index](INDEX.md) · [Previous source section](pep-436-argument-clinic.md) · [Next source section](other-improvements.md) · [Release/subject declaration](release-highlights.md)
