# inspect: Signature annotation resolution and callable limitations

When certain annotations come through as strings (for instance, because `from __future__ import annotations` was in effect), `signature()` tries to un-stringize them on its own by calling [`annotationlib.get_annotations()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.get_annotations). While resolving the annotations, the *globals*, *locals*, and *eval_str* parameters get forwarded to `annotationlib.get_annotations()`; for guidance on applying these parameters, refer to the documentation for `annotationlib.get_annotations()`. To govern how the returned annotations are formatted, hand a member of the [`annotationlib.Format`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.Format) enum to the *annotation_format* parameter. As an illustration, pass `annotation_format=annotationlib.Format.STRING` to get annotations back in string format.

Raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when no signature is obtainable, and [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) when the object's type isn't supported. On top of that, when the annotations are stringized and *eval_str* is not false, the `eval()` call(s) used to un-stringize the annotations inside [`annotationlib.get_annotations()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.get_annotations) may raise an exception of any kind.

Within a function's signature, a slash (/) marks that every parameter ahead of it is positional-only. Further details appear in [the FAQ entry on positional-only parameters](https://docs.python.org/3.14/faq/programming.html#faq-positional-only-arguments).

Changed in version 3.5: Added the *follow_wrapped* parameter. Supply `False` to obtain the signature of *callable* itself (`callable.__wrapped__` won't be consulted to unwrap decorated callables.)

Changed in version 3.10: Added the *globals*, *locals*, and *eval_str* parameters.

Changed in version 3.14: Added the *annotation_format* parameter.

Note

Within particular Python implementations, some callables might not be introspectable. To illustrate, several C-defined built-in functions in CPython expose no metadata describing their arguments.

**CPython implementation detail:** When the supplied object carries a `__signature__` attribute, we might rely on it to build the signature. Those precise semantics count as an implementation detail and can change without notice. For the present semantics, refer to the source code.

[Subject index](INDEX.md) · [Continue](inspect-signature-class-to-inspect-signature-format.md) · [Owning module, declaration or section: inspect](inspect-inspect-live-objects.md) · [Owning module, declaration or section: Introspecting callables with the Signature object](inspect-signature.md) · [Owning module, declaration or section: inspect.signature](inspect-signature.md) · [Preceding source contract and version conditions](inspect-signature.md)
