# What's New In Python 3.0 / Removed Syntax

### Removed Syntax

- [**PEP 3113**](https://peps.python.org/pep-3113/): Tuple parameter unpacking taken out. Writing `def foo(a, (b, c)): ...` is no longer possible. Use `def foo(a, b_c): b, c = b_c` in its place.

- Backticks taken out (reach for [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) in their place).

- `<>` taken out (reach for `!=` in its place).

- A keyword removed: [`exec()`](https://docs.python.org/3.14/library/functions.html#exec) is a keyword no longer; it survives as a function. (Happily the function form was already valid in 2.x.) Note as well that `exec()` has dropped its stream argument; in lieu of `exec(f)` reach for `exec(f.read())`.

- Integer literals have dropped support for a trailing `l` or `L`.

- String literals have dropped support for a leading `u` or `U`.

- The [`from`](https://docs.python.org/3.14/reference/simple_stmts.html#from) *module* [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) `*` syntax is permitted at the module level alone, no longer within functions.

- The lone valid syntax for relative imports is `from .[*module*] import *name*`. Every [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) form that doesn't begin with `.` reads as an absolute import. ([**PEP 328**](https://peps.python.org/pep-0328/))

- Classic classes are no more.

[Subject index](INDEX.md) · [Previous source section](changed-syntax.md) · [Next source section](changes-already-present-in-python-2-6.md) · [Release/subject declaration](common-stumbling-blocks.md)
