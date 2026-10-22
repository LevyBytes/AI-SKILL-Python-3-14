# codeop: `codeop.Compile`

*class *codeop.Compile

Objects of this class expose [`__call__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__call__) methods whose signature matches the built-in function [`compile()`](https://docs.python.org/3.14/library/functions.html#compile); the distinction is that when an instance compiles program text holding a [`__future__`](https://docs.python.org/3.14/library/__future__.html#module-__future__) statement, that instance "remembers" it and keeps that statement in force while compiling every later program text.

[Subject index](INDEX.md) · [Previous](codeop-compile-command.md) · [Continue](codeop-commandcompiler-class.md) · [Owning module, declaration or section: codeop](codeop-compile-command.md)
