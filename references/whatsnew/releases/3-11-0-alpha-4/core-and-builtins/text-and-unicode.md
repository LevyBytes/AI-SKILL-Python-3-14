# Python 3.11.0 alpha 4 / core and builtins / text and unicode

[bpo-46048](https://bugs.python.org/issue?@action=redirect&bpo=46048): Correct startup parsing of `._pth` files so paths that are a single character get read properly.

[bpo-46331](https://bugs.python.org/issue?@action=redirect&bpo=46331): Refrain from setting the line number on the instruction that stores a doc-string. This fixes a regression that appeared in 3.11 alpha.

[bpo-46237](https://bugs.python.org/issue?@action=redirect&bpo=46237): Correct the line number reported for tokenizer errors within f-strings. Pablo Galindo wrote the patch.

[bpo-46006](https://bugs.python.org/issue?@action=redirect&bpo=46006): Repair a regression triggered when a type method such as `__init__()` is altered inside a subinterpreter. Repair a regression in `_PyUnicode_EqualToASCIIId()` and in type `update_slot()`. The earlier change had reworked the interned-string Unicode dictionary so it would work per-subinterpreter; that is now reverted, so the internal interned dictionary is once more shared across every interpreter. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
