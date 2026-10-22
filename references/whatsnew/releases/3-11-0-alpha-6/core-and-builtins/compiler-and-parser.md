# Python 3.11.0 alpha 6 / core and builtins / compiler and parser

[bpo-45828](https://bugs.python.org/issue?@action=redirect&bpo=45828): The bytecode compiler will now try to perform runtime stack manipulations during compilation (in any case where that is practical).

[bpo-46808](https://bugs.python.org/issue?@action=redirect&bpo=46808): Drop the `NEXT_BLOCK` macro out of compile.c, and have the compiler emit implicit blocks on its own wherever those are required.

[bpo-46707](https://bugs.python.org/issue?@action=redirect&bpo=46707): Sidestep possible exponential backtracking that arose when emitting certain syntax errors loaded with many brackets. Pablo Galindo wrote the patch.

[bpo-46823](https://bugs.python.org/issue?@action=redirect&bpo=46823): Add a specialized combined opcode `LOAD_FAST__LOAD_ATTR_INSTANCE_VALUE`. Dennis Sweeney wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
