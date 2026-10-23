# What's New In Python 3.13 / ast - ast

### ast

- Within the [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) module, the node-type constructors have grown stricter about which arguments they take, and they behave more sensibly once arguments get left out.

Whenever an optional field on an AST node goes unsupplied as a construction argument, that field is henceforth assigned `None`. In the same way, an omitted list field defaults to an empty list, while an omitted `expr_context` field falls back to [`Load()`](https://docs.python.org/3.14/library/ast.html#ast.Load). (Formerly, across every one of these cases, the freshly built AST node simply lacked the attribute.)

For every remaining situation, namely a missing required argument, the node constructor henceforth issues a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). Python 3.15 will turn this into an exception. Likewise, handing the constructor a keyword argument that corresponds to no field on the AST node is henceforth deprecated and will become an exception in Python 3.15.

None of these changes reach user-defined subclasses of [`ast.AST`](https://docs.python.org/3.14/library/ast.html#ast.AST) unless such a class chooses the new behavior by supplying the [`AST._field_types`](https://docs.python.org/3.14/library/ast.html#ast.AST._field_types) mapping.

(Contributed by Jelle Zijlstra in [gh-105858](https://github.com/python/cpython/issues/105858), [gh-117486](https://github.com/python/cpython/issues/117486), and [gh-118851](https://github.com/python/cpython/issues/118851).)

- [`ast.parse()`](https://docs.python.org/3.14/library/ast.html#ast.parse) henceforth takes an optional *optimize* argument that it forwards along to [`compile()`](https://docs.python.org/3.14/library/functions.html#compile). That allows you to retrieve an optimized AST. (Contributed by Irit Katriel in [gh-108113](https://github.com/python/cpython/issues/108113).)

[Subject index](INDEX.md) · [Previous source section](array.md) · [Next source section](asyncio.md) · [Release/subject declaration](summary-release-highlights.md)
