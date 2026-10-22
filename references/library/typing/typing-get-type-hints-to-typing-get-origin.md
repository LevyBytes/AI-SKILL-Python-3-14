# typing: `typing.get_type_hints()`, `typing.get_origin()`

### Introspection helpers

 typing.get_type_hints(*obj*, *globalns=None*, *localns=None*, *include_extras=False*, ***, *format=Format.VALUE*)

Return a dictionary of type hints for a function, a method, a module, a class object, or any other callable.

In many cases the result matches [`annotationlib.get_annotations()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.get_annotations), yet this function applies the following adjustments to the annotations dictionary:

- Forward references written as string literals or `ForwardRef` objects are resolved by evaluating them within *globalns*, *localns*, and, where it applies, *obj*'s [type parameter](https://docs.python.org/3.14/reference/compound_stmts.html#type-params) namespace. When *globalns* or *localns* goes unsupplied, fitting namespace dictionaries are derived from *obj*.

- `None` is replaced with [`types.NoneType`](https://docs.python.org/3.14/library/types.html#types.NoneType).

- If `@no_type_check` has been applied to *obj*, an empty dictionary is returned.

- When *obj* is a class `C`, the function hands back a dictionary that blends the annotations from the base classes of `C` with the ones placed directly on `C`. The work proceeds by walking [`C.__mro__`](https://docs.python.org/3.14/reference/datamodel.html#type.__mro__) and progressively merging the [annotations](https://docs.python.org/3.14/glossary.html#term-variable-annotation) of every base class. Whenever a class sits earlier in the [method resolution order](https://docs.python.org/3.14/glossary.html#term-method-resolution-order), its annotations win out over those from any class positioned later in that order.

- Every appearance of `Annotated[T, ...]`, `Required[T]`, `NotRequired[T]`, and `ReadOnly[T]` is swapped for `T` recursively by the function, except when *include_extras* carries the value `True` (consult `Annotated` for further detail).

Caution

Arbitrary code held inside annotations may be run by this function. Consult [Security implications of introspecting annotations](https://docs.python.org/3.14/library/annotationlib.html#annotationlib-security) for further detail.

Note

When [`Format.VALUE`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.Format.VALUE) is in effect and one of *obj*'s annotations holds a forward reference that cannot be resolved, a [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError) exception gets raised. This may arise, for instance, with names brought in beneath `if TYPE_CHECKING`. Speaking broadly, an annotation containing invalid Python code can trigger an exception of any kind.

Note

Passing an instance to `get_type_hints()` is unsupported. When you need the annotations belonging to an instance, invoke `get_type_hints()` against the instance's class in its place (for example, `get_type_hints(type(obj))`).

Changed in version 3.9: The `include_extras` parameter was introduced under [**PEP 593**](https://peps.python.org/pep-0593/). Consult the `Annotated` documentation for further detail.

Changed in version 3.11: Formerly, `Optional[t]` got applied to function and method annotations whenever a default of `None` was assigned. The annotation now comes back untouched.

Changed in version 3.14: The `format` parameter was introduced. Consult the [`annotationlib.get_annotations()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.get_annotations) documentation for further detail.

Changed in version 3.14: Passing instances to `get_type_hints()` is no longer supported. Prior releases accepted certain instances, which was an undocumented quirk of the implementation.

 typing.get_origin(*tp*)

Get a type stripped of its subscript: given a typing object shaped like `X[Y, Z, ...]`, yield `X`.

Should `X` be a typing-module alias standing in for a builtin or [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) class, it is normalized back to the original class. Should `X` be an instance of `ParamSpecArgs` or `ParamSpecKwargs`, the underlying `ParamSpec` is returned. For objects that are not supported, `None` comes back.

Examples:

```python
assert get_origin(str) is None
assert get_origin(Dict[str, int]) is dict
assert get_origin(Union[int, str]) is Union
assert get_origin(Annotated[str, "metadata"]) is Annotated
P = ParamSpec('P')
assert get_origin(P.args) is P
assert get_origin(P.kwargs) is P

```

Added in version 3.8.

[Subject index](INDEX.md) · [Previous](functions-and-decorators.md) · [Continue](typing-get-args-to-typing-is-protocol.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md)
