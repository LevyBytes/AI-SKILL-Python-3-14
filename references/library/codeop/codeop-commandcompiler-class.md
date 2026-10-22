# codeop: `codeop.CommandCompiler`

*class *codeop.CommandCompiler

Objects of this class expose [`__call__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__call__) methods whose signature matches `compile_command()`; here the distinction is that when an instance compiles program text holding a [`__future__`](https://docs.python.org/3.14/library/__future__.html#module-__future__) statement, that instance "remembers" it and keeps that statement in force while compiling every later program text.

[Subject index](INDEX.md) · [Previous](codeop-compile-class.md) · [Continue](../collections-abc/collections-abc-abstract-base-classes-for-containers.md) · [Owning module, declaration or section: codeop](codeop-compile-command.md)
