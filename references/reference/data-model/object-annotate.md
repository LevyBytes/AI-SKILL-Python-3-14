# object.__annotate__(*format*)

object.__annotate__(*format*)

An [annotate function](https://docs.python.org/3.14/glossary.html#term-annotate-function). Returns a fresh dictionary object mapping attribute/parameter names to their annotation values.

Accepts a format parameter that specifies the format in which annotation values should be supplied. It must be a member of the [`annotationlib.Format`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.Format) enum, or an integer whose value corresponds to a member of the enum.

When an annotate function does not support the requested format, it must raise [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError). Annotate functions must always support the [`VALUE`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.Format.VALUE) format; they must not raise [`NotImplementedError()`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError) when invoked with this format.

When invoked with the [`VALUE`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.Format.VALUE) format, an annotate function may raise [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError); it must not raise `NameError` when invoked requesting any other format.

When an object carries no annotations, `__annotate__` should preferably be set to `None` (it cannot be deleted), instead of being set to a function returning an empty dict.

Added in version 3.14.

See also

[**PEP 649**](https://peps.python.org/pep-0649/): Deferred evaluation of annotation using descriptors

Introduces lazy evaluation of annotations and the `__annotate__` function.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](annotations.md) · [Previous source section](object-annotations.md) · [Following source section](special-method-lookup.md)
