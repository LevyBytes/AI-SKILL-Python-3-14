# typing: `typing.ForwardRef`

*class *typing.ForwardRef

Class used for internal typing representation of string forward references.

To illustrate, `List["SomeClass"]` is silently turned into `List[ForwardRef("SomeClass")]`. A user is not meant to instantiate `ForwardRef` directly, though introspection tools may make use of it.

Note

[**PEP 585**](https://peps.python.org/pep-0585/) generic types like `list["SomeClass"]` receive no such silent conversion to `list[ForwardRef("SomeClass")]`, so they will not resolve on their own to `list[SomeClass]`.

Added in version 3.7.4.

Changed in version 3.14: It now stands as an alias for [`annotationlib.ForwardRef`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.ForwardRef). A number of this class's undocumented behaviors have shifted; as one case, once a `ForwardRef` is evaluated, its evaluated value gets cached no longer.

[Subject index](INDEX.md) · [Previous](typing-is-typeddict.md) · [Continue](typing-evaluate-forward-ref-to-typing-nodefault.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Introspection helpers](typing-get-type-hints-to-typing-get-origin.md)
