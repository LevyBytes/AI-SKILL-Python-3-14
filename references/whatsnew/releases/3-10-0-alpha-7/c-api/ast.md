# Python 3.10.0 alpha 7 / c api / ast

[bpo-43244](https://bugs.python.org/issue?@action=redirect&bpo=43244): Delete the `ast.h`, `asdl.h`, and `Python-ast.h` header files. These functions went undocumented and stayed outside the limited C API. Most of the names these headers defined lacked a `Py` prefix and could therefore collide with other names. As one example, `Python-ast.h` defined a `Yield` macro that clashed with the `Yield` name from the Windows `<winbase.h>` header. Reach for the Python [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) module instead. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
