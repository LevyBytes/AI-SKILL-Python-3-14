# What's New In Python 3.10 / PEP 612: Parameter Specification Variables - typing

To start with, there is the parameter specification variable. Its job is to relay the parameter types from one callable onto another callable – something you run into often with higher order functions plus decorators. Worked examples live at [`typing.ParamSpec`](https://docs.python.org/3.14/library/typing.html#typing.ParamSpec). Up to this point, expressing that dependency between parameter types at this level of precision lacked any convenient mechanism.

Following that is the freshly added `Concatenate` operator. You pair it with parameter specification variables when annotating a higher order callable that tacks on or strips out parameters belonging to another callable. Worked examples live at [`typing.Concatenate`](https://docs.python.org/3.14/library/typing.html#typing.Concatenate).

Consult [`typing.Callable`](https://docs.python.org/3.14/library/typing.html#typing.Callable), [`typing.ParamSpec`](https://docs.python.org/3.14/library/typing.html#typing.ParamSpec), [`typing.Concatenate`](https://docs.python.org/3.14/library/typing.html#typing.Concatenate), [`typing.ParamSpecArgs`](https://docs.python.org/3.14/library/typing.html#typing.ParamSpecArgs), [`typing.ParamSpecKwargs`](https://docs.python.org/3.14/library/typing.html#typing.ParamSpecKwargs), and [**PEP 612**](https://peps.python.org/pep-0612/) if you want the full picture.

(Ken Jin contributed this work in [bpo-41559](https://bugs.python.org/issue?@action=redirect&bpo=41559); Jelle Zijlstra added small refinements in [bpo-43783](https://bugs.python.org/issue?@action=redirect&bpo=43783). Mark Mendoza authored the PEP.)

> (Contributed by Maggie Moss and Philippe Prados in [bpo-41428](https://bugs.python.org/issue?@action=redirect&bpo=41428), with additions by Yurii Karabas and Serhiy Storchaka in [bpo-44490](https://bugs.python.org/issue?@action=redirect&bpo=44490).)

### PEP 612: Parameter Specification Variables

A pair of new options that sharpen the data handed to static type checkers for [**PEP 484**](https://peps.python.org/pep-0484/)'s `Callable` were added to the [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) module.

[Subject index](INDEX.md) · [Next source section](pep-613-typealias.md) · [Release/subject declaration](summary-release-highlights.md) · [Previous source section](pep-604-new-type-union-operator.md)
