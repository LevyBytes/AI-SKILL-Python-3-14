# Python 3.11.0 alpha 5 / library / typing

[bpo-46553](https://bugs.python.org/issue?@action=redirect&bpo=46553): Within [`typing.get_type_hints()`](https://docs.python.org/3.14/library/typing.html#typing.get_type_hints), enable evaluation of bare stringified `ClassVar` annotations. Gregory Beauregard contributed the patch.

[bpo-46539](https://bugs.python.org/issue?@action=redirect&bpo=46539): Within [`typing.get_type_hints()`](https://docs.python.org/3.14/library/typing.html#typing.get_type_hints), enable evaluation of stringified `ClassVar` and `Final` annotations nested inside `Annotated`. Gregory Beauregard wrote the patch.

[bpo-46491](https://bugs.python.org/issue?@action=redirect&bpo=46491): Permit [`typing.Annotated`](https://docs.python.org/3.14/library/typing.html#typing.Annotated) to enclose [`typing.Final`](https://docs.python.org/3.14/library/typing.html#typing.Final) and [`typing.ClassVar`](https://docs.python.org/3.14/library/typing.html#typing.ClassVar). Gregory Beauregard contributed the patch.

[bpo-46414](https://bugs.python.org/issue?@action=redirect&bpo=46414): Introduce [`typing.reveal_type()`](https://docs.python.org/3.14/library/typing.html#typing.reveal_type). Jelle Zijlstra contributed the patch.

[bpo-44791](https://bugs.python.org/issue?@action=redirect&bpo=44791): Correct substitution of [`ParamSpec`](https://docs.python.org/3.14/library/typing.html#typing.ParamSpec) within [`Concatenate`](https://docs.python.org/3.14/library/typing.html#typing.Concatenate) across differing parameter expressions. Substituting with a list of types now yields a tuple of types. Substituting with `Concatenate` now yields a `Concatenate` whose argument lists have been concatenated.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
