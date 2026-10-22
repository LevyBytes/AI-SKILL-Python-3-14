# Code Objects

### Code Objects

The implementation relies on code objects to stand for “pseudo-compiled” executable Python code, such as a function body. Unlike function objects, they hold no reference to their global execution environment. The built-in [`compile()`](https://docs.python.org/3.14/library/functions.html#compile) function returns code objects, and you can pull one out of a function object via its [`__code__`](https://docs.python.org/3.14/reference/datamodel.html#function.__code__) attribute. See also the [`code`](https://docs.python.org/3.14/library/code.html#module-code) module.

Reading [`__code__`](https://docs.python.org/3.14/reference/datamodel.html#function.__code__) raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `object.__getattr__` whose arguments are `obj` and `"__code__"`.

To run or evaluate a code object, hand it (rather than a source string) to the [`exec()`](https://docs.python.org/3.14/library/functions.html#exec) or [`eval()`](https://docs.python.org/3.14/library/functions.html#eval) built-in functions.

For further detail, consult [The standard type hierarchy](https://docs.python.org/3.14/reference/datamodel.html#types).

[Subject index](INDEX.md) · [Previous](methods.md) · [Continue](type-objects.md)
