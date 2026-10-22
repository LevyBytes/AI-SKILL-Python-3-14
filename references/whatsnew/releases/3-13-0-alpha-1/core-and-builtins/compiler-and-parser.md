# Python 3.13.0 alpha 1 / core and builtins / compiler and parser

[gh-105017](https://github.com/python/cpython/issues/105017): Avoid emitting an extra final `NL` token while parsing files that carry CRLF lines. Marta Gómez prepared the patch.

[gh-109719](https://github.com/python/cpython/issues/109719): Jump target labels that went missing when the compiler reordered cold/warm blocks are now restored.

[gh-109627](https://github.com/python/cpython/issues/109627): A bug was fixed in which the compiler did not give a fresh jump target label to a duplicated small exit block.

[gh-107265](https://github.com/python/cpython/issues/107265): Opcodes that the executor hides are deopted whenever the base opcode is required

[gh-109351](https://github.com/python/cpython/issues/109351): A crash while compiling a malformed AST that contains a named (walrus) expression is now fixed.

[gh-109256](https://github.com/python/cpython/issues/109256): Specialized opcodes now receive their opcode IDs from a dedicated range, so the IDs of the "real" opcodes stay more stable.

[gh-109889](https://github.com/python/cpython/issues/109889): The compiler's redundant NOP detection was corrected so it steps past NOPs lacking a line number while searching for the next instruction's lineno.

[gh-109823](https://github.com/python/cpython/issues/109823): A defect was fixed where the compiler failed to adjust labels while deleting an empty basic block that served as a jump target.

[gh-105375](https://github.com/python/cpython/issues/105375): Repair a defect in the compiler that allowed an exception to wind up overwritten.

[gh-109052](https://github.com/python/cpython/issues/109052): The base opcode is now used when code objects are compared, keeping instrumentation from interfering

[gh-105481](https://github.com/python/cpython/issues/105481): The regen-opcode build stage was dropped, and its job is now carried out within regen-cases.

[gh-107971](https://github.com/python/cpython/issues/107971): Opcode IDs are now produced from bytecodes.c rather than being hard coded inside opcode.py.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
