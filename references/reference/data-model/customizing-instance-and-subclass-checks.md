# 3.3.4. Customizing instance and subclass checks

### 3.3.4. Customizing instance and subclass checks

The methods below let you override how the [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) and [`issubclass()`](https://docs.python.org/3.14/library/functions.html#issubclass) built-in functions normally behave.

Notably, the metaclass [`abc.ABCMeta`](https://docs.python.org/3.14/library/abc.html#abc.ABCMeta) supplies these methods so that Abstract Base Classes (ABCs) can be registered as "virtual base classes" of any class or type (built-in types included), as well as of other ABCs.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Previous source section](uses-for-metaclasses.md) · [Following source section](type-instancecheck.md)
