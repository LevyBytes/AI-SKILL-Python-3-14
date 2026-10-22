# Python 3.7.0 alpha 1 / library / compiler and parser

[bpo-28257](https://bugs.python.org/issue?@action=redirect&bpo=28257): Sharpened the error message raised when a non-iterable serves as a var-positional argument. A new BUILD_TUPLE_UNPACK_WITH_CALL opcode was added.

[bpo-30070](https://bugs.python.org/issue?@action=redirect&bpo=30070): Leaks together with crashes in the parser module's error handling were corrected.

[bpo-31499](https://bugs.python.org/issue?@action=redirect&bpo=31499): xml.etree: Repair a crash whenever a parser sits inside a reference cycle.

[bpo-30645](https://bugs.python.org/issue?@action=redirect&bpo=30645): Path computation in `imp.load_package()` was corrected so it works for packages distributed with bytecode alone. Alexandru Ardelean provided the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
