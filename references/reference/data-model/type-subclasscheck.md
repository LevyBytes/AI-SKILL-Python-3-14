# type.__subclasscheck__(*self*, *subclass*)

type.__subclasscheck__(*self*, *subclass*)

Return true when *subclass* ought to be treated as a (direct or indirect) subclass of *class*. When defined, it is invoked to implement `issubclass(subclass, class)`.

Be aware that these methods are looked up on the type (the metaclass) of a class. You cannot define them as class methods on the actual class. This mirrors how special methods called on instances are looked up, the difference here being that the instance is itself a class.

See also

[**PEP 3119**](https://peps.python.org/pep-3119/) - Introducing Abstract Base Classes

Lays out how to customize [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) and [`issubclass()`](https://docs.python.org/3.14/library/functions.html#issubclass) behavior by way of `__instancecheck__()` and `__subclasscheck__()`, and explains why the feature matters when bringing Abstract Base Classes (refer to the [`abc`](https://docs.python.org/3.14/library/abc.html#module-abc) module) into the language.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](customizing-instance-and-subclass-checks.md) · [Previous source section](type-instancecheck.md) · [Following source section](emulating-generic-types.md)
