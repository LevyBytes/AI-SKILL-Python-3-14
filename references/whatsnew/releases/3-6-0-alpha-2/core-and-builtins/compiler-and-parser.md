# Python 3.6.0 alpha 2 / core and builtins / compiler and parser

[bpo-27286](https://bugs.python.org/issue?@action=redirect&bpo=27286): Corrected the compilation of the BUILD_MAP_UNPACK_WITH_CALL opcode. Invoking a function with generalized unpacking (PEP 448) alongside clashing keyword names could trigger undefined behavior.

[bpo-27140](https://bugs.python.org/issue?@action=redirect&bpo=27140): Introduced the BUILD_CONST_KEY_MAP opcode.

[bpo-26647](https://bugs.python.org/issue?@action=redirect&bpo=26647): The Python interpreter has switched to 16-bit wordcode rather than bytecode. Demur Rumed wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
