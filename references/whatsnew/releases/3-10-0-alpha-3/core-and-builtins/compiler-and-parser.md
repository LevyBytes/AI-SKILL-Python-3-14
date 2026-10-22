# Python 3.10.0 alpha 3 / core and builtins / compiler and parser

[bpo-42374](https://bugs.python.org/issue?@action=redirect&bpo=42374): Repair a regression brought in by the new parser whereby an unparenthesized walrus operator was disallowed inside generator expressions.

[bpo-42349](https://bugs.python.org/issue?@action=redirect&bpo=42349): Guarantee the compiler front-end emits a well-formed control flow graph. The compiler back-end can now be more aggressive, since doing so is now safe.

[bpo-42282](https://bugs.python.org/issue?@action=redirect&bpo=42282): Optimise constant subexpressions occurring within named expressions (the AST optimiser had not previously recursed into named expressions). Nick Coghlan wrote the patch.

[bpo-42266](https://bugs.python.org/issue?@action=redirect&bpo=42266): Repaired a defect in the LOAD_ATTR opcode cache that ignored monkey-patching a class-level attribute into a descriptor. Pablo Galindo supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
