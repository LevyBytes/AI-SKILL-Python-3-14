# Python 3.9.0 alpha 2 / core and builtins / compiler and parser

[bpo-39080](https://bugs.python.org/issue?@action=redirect&bpo=39080): The *end_col_offset* value was corrected for Starred Expression AST nodes that sit among the elements of the *args* attribute belonging to Call AST nodes.

[bpo-39031](https://bugs.python.org/issue?@action=redirect&bpo=39031): While parsing an “elif” node, the lineno and col_offset of that node now refer to the “elif” keyword itself rather than to its condition, which lines it up with the “if” node. Lysandros Nikolaou wrote the patch.

[bpo-33387](https://bugs.python.org/issue?@action=redirect&bpo=33387): The WITH_CLEANUP_START, WITH_CLEANUP_FINISH, BEGIN_FINALLY, END_FINALLY, CALL_FINALLY and POP_FINALLY bytecodes were dropped, with RERAISE and WITH_EXCEPT_START bytecodes taking their place. For "with" and "try-except" statements, the compiler now emits distinct code along exceptional versus non-exceptional branches. With "try-finally" statements, the "finally" block is copied for every way of leaving the "try" body.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
