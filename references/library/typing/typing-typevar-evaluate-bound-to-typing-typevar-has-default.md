# typing.TypeVar: TypeVar bound, constraint and default evaluation

__name__

The name of the type variable.

 __covariant__

Whether the type var has been explicitly marked as covariant.

 __contravariant__

Whether the type var has been explicitly marked as contravariant.

 __infer_variance__

Whether the type variable's variance should be inferred by type checkers.

Added in version 3.12.

 __bound__

The upper bound of the type variable, if any.

Changed in version 3.12: For type variables built via the [type parameter syntax](https://docs.python.org/3.14/reference/compound_stmts.html#type-params), the bound is computed only at the moment the attribute is read, rather than when the type variable comes into being (see [Lazy evaluation](https://docs.python.org/3.14/reference/executionmodel.html#lazy-evaluation)).

 evaluate_bound()

An [evaluate function](https://docs.python.org/3.14/glossary.html#term-evaluate-function) that pairs with the `__bound__` attribute. Called on its own, this method handles only the [`VALUE`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.Format.VALUE) format, which matches reading the `__bound__` attribute directly, but you can hand the method object to [`annotationlib.call_evaluate_function()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.call_evaluate_function) to compute the value in some other format.

Added in version 3.14.

 __constraints__

A tuple containing the constraints of the type variable, if any.

Changed in version 3.12: For type variables built via the [type parameter syntax](https://docs.python.org/3.14/reference/compound_stmts.html#type-params), the constraints are computed only at the moment the attribute is read, rather than when the type variable comes into being (see [Lazy evaluation](https://docs.python.org/3.14/reference/executionmodel.html#lazy-evaluation)).

 evaluate_constraints()

An [evaluate function](https://docs.python.org/3.14/glossary.html#term-evaluate-function) that pairs with the `__constraints__` attribute. Called on its own, this method handles only the [`VALUE`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.Format.VALUE) format, which matches reading the `__constraints__` attribute directly, but you can hand the method object to [`annotationlib.call_evaluate_function()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.call_evaluate_function) to compute the value in some other format.

Added in version 3.14.

 __default__

For the type variable, its default value; this is `typing.NoDefault` whenever none was set.

Added in version 3.13.

 evaluate_default()

An [evaluate function](https://docs.python.org/3.14/glossary.html#term-evaluate-function) that pairs with the `__default__` attribute. Called on its own, this method handles only the [`VALUE`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.Format.VALUE) format, which matches reading the `__default__` attribute directly, but you can hand the method object to [`annotationlib.call_evaluate_function()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.call_evaluate_function) to compute the value in some other format.

Added in version 3.14.

 has_default()

Report whether the type variable carries a default value or not. This amounts to testing whether `__default__` differs from the `typing.NoDefault` singleton, except that it avoids forcing evaluation of the [lazily evaluated](https://docs.python.org/3.14/reference/executionmodel.html#lazy-evaluation) default value.

Added in version 3.13.

Changed in version 3.12: Type variables may now be declared with the [type parameter](https://docs.python.org/3.14/reference/compound_stmts.html#type-params) syntax that [**PEP 695**](https://peps.python.org/pep-0695/) introduced. The `infer_variance` parameter was added.

Changed in version 3.13: Support for default values was added.

[Subject index](INDEX.md) · [Previous](generic-concatenation-type-example.md) · [Continue](typing-typevartuple-class.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: typing.TypeVar](typing-typevar-class.md) · [Owning module, declaration or section: Building generic types and type aliases](typing-generic-class.md)
