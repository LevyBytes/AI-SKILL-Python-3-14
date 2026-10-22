# Python 3.9.0 alpha 1 / core and builtins / compiler and parser

[bpo-37213](https://bugs.python.org/issue?@action=redirect&bpo=37213): Pablo Galindo contributed a fix that correctly handles negative line offsets inside the peephole optimizer.

[bpo-38310](https://bugs.python.org/issue?@action=redirect&bpo=38310): Brandt Bucher contributed a change that predicts `BUILD_MAP_UNPACK_WITH_CALL` -> `CALL_FUNCTION_EX` opcode pairs within the principal interpreter loop.

[bpo-38640](https://bugs.python.org/issue?@action=redirect&bpo=38640): Corrected a compiler bug that caused it to raise when break statements and continue statements appeared inside while loops that are always false. Pablo Galindo wrote the patch.

[bpo-37340](https://bugs.python.org/issue?@action=redirect&bpo=37340): Dropped the object cache (`free_list`) that backed bound method objects. Transient bound method objects appear less frequently than they once did, owing to the `LOAD_METHOD` opcode together with the `_PyObject_VectorcallMethod` C API.

[bpo-37593](https://bugs.python.org/issue?@action=redirect&bpo=37593): Exchanged the order of the *posonlyargs* and *args* parameters within the constructor for `ast.parameters` nodes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
