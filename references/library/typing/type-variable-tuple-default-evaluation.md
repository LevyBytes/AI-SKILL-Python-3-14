# typing.TypeVarTuple: TypeVarTuple default evaluation and availability

__name__

The name of the type variable tuple.

 __default__

For the type variable tuple, its default value; this is `typing.NoDefault` whenever none was set.

Added in version 3.13.

 evaluate_default()

An [evaluate function](https://docs.python.org/3.14/glossary.html#term-evaluate-function) that pairs with the `__default__` attribute. Called on its own, this method handles only the [`VALUE`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.Format.VALUE) format, which matches reading the `__default__` attribute directly, but you can hand the method object to [`annotationlib.call_evaluate_function()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.call_evaluate_function) to compute the value in some other format.

Added in version 3.14.

 has_default()

Report whether the type variable tuple carries a default value or not. This amounts to testing whether `__default__` differs from the `typing.NoDefault` singleton, except that it avoids forcing evaluation of the [lazily evaluated](https://docs.python.org/3.14/reference/executionmodel.html#lazy-evaluation) default value.

Added in version 3.13.

Added in version 3.11.

Changed in version 3.12: Type variable tuples may now be declared with the [type parameter](https://docs.python.org/3.14/reference/compound_stmts.html#type-params) syntax that [**PEP 695**](https://peps.python.org/pep-0695/) introduced.

Changed in version 3.13: Support for default values was added.

[Subject index](INDEX.md) · [Previous](typevartuple-variadic-constraints.md) · [Continue](typing-paramspec-class.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: typing.TypeVarTuple](typing-typevartuple-class.md) · [Owning module, declaration or section: Building generic types and type aliases](typing-generic-class.md)
