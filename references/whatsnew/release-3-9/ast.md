# What's New In Python 3.9 / ast - ast

### Improved Modules

### ast

An *indent* option was supplied to [`dump()`](https://docs.python.org/3.14/library/ast.html#ast.dump) so it can emit multiline indented output. (Contributed by Serhiy Storchaka in [bpo-37995](https://bugs.python.org/issue?@action=redirect&bpo=37995).)

The function [`ast.unparse()`](https://docs.python.org/3.14/library/ast.html#ast.unparse) joined the [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) module; it takes an [`ast.AST`](https://docs.python.org/3.14/library/ast.html#ast.AST) object and returns a string whose code, once parsed, would rebuild an equivalent `ast.AST` object. (Contributed by Pablo Galindo and Batuhan Taskaya in [bpo-38870](https://bugs.python.org/issue?@action=redirect&bpo=38870).)

AST nodes received docstrings carrying the ASDL signature that builds the given node. (Contributed by Batuhan Taskaya in [bpo-39638](https://bugs.python.org/issue?@action=redirect&bpo=39638).)

[Subject index](INDEX.md) · [Previous source section](graphlib.md) · [Next source section](asyncio.md) · [Release/subject declaration](summary-release-highlights.md)
