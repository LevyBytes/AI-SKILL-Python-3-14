# typing.ParamSpec: ParamSpec default evaluation and availability

Before `ParamSpec` existed, the most straightforward earlier approach to annotating this was a `TypeVar` whose upper bound is `Callable[..., Any]`. That approach, though, runs into two difficulties:

1.

Because `*args` and `**kwargs` end up typed as `Any`, the type checker has no way to verify the `inner` function.

2.

Returning the `inner` function from the body of the `add_logging` decorator may force a `cast()`, or else you must instruct the static type checker to skip the `return inner`.

 args

 kwargs

A `ParamSpec` records positional as well as keyword parameters, so `P.args` and `P.kwargs` let you separate a `ParamSpec` into its two pieces. The positional-parameter tuple for a particular call is what `P.args` stands for, and it is meant solely for annotating `*args`. Likewise `P.kwargs` stands for the keyword-parameter-to-value mapping in a particular call, and it belongs only on `**kwargs`. Each attribute needs the annotated parameter to be visible in the current scope. While the program runs, `P.args` and `P.kwargs` are, respectively, instances of `ParamSpecArgs` and `ParamSpecKwargs`.

 __name__

The parameter specification's name.

 __default__

The parameter specification's default value; when none was set, this is `typing.NoDefault`.

Added in version 3.13.

 evaluate_default()

An [evaluate function](https://docs.python.org/3.14/glossary.html#term-evaluate-function) that pairs with the `__default__` attribute. Invoked on its own, this method handles only the [`VALUE`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.Format.VALUE) format, which matches reading the `__default__` attribute directly; however, you can hand the method object to [`annotationlib.call_evaluate_function()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.call_evaluate_function) so the value gets evaluated under another format.

Added in version 3.14.

 has_default()

Report whether the parameter specification carries a default value. This amounts to testing that `__default__` is not the `typing.NoDefault` singleton, with the difference that it avoids forcing evaluation of the [lazily evaluated](https://docs.python.org/3.14/reference/executionmodel.html#lazy-evaluation) default value.

Added in version 3.13.

Passing `covariant=True` or `contravariant=True` when constructing parameter specification variables lets you declare covariant or contravariant generic types. As with `TypeVar`, the `bound` argument is permitted too. The precise semantics of these keywords, however, have not yet been settled.

Added in version 3.10.

Changed in version 3.12: Declaring parameter specifications is now possible through the [type parameter](https://docs.python.org/3.14/reference/compound_stmts.html#type-params) syntax that [**PEP 695**](https://peps.python.org/pep-0695/) brought in.

Changed in version 3.13: Default values became supported.

Note

Pickling works only for parameter specification variables that are defined in the global scope.

See also

- [**PEP 612**](https://peps.python.org/pep-0612/) – Parameter Specification Variables (the PEP which introduced `ParamSpec` and `Concatenate`)

- `Concatenate`

- Annotating callable objects

[Subject index](INDEX.md) · [Continue](typing-paramspecargs-class-to-typing-paramspeckwargs-class.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: typing.ParamSpec](typing-paramspec-class.md) · [Owning module, declaration or section: Building generic types and type aliases](typing-generic-class.md) · [Preceding source contract and version conditions](typing-paramspec-class.md)
