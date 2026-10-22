# Python 3.11.0 alpha 7 / library / typing

[bpo-41370](https://bugs.python.org/issue?@action=redirect&bpo=41370): Strings can now be evaluated as forward references by [`typing.get_type_hints()`](https://docs.python.org/3.14/library/typing.html#typing.get_type_hints) inside [PEP 585 generic aliases](https://docs.python.org/3.14/library/stdtypes.html#types-genericalias).

[bpo-46480](https://bugs.python.org/issue?@action=redirect&bpo=46480): A new [`typing.assert_type()`](https://docs.python.org/3.14/library/typing.html#typing.assert_type) has been added. Jelle Zijlstra wrote the patch.

[bpo-46170](https://bugs.python.org/issue?@action=redirect&bpo=46170): Better wording is given to the error raised when subclassing an instance of [`typing.NewType`](https://docs.python.org/3.14/library/typing.html#typing.NewType) is attempted.

[bpo-47088](https://bugs.python.org/issue?@action=redirect&bpo=47088): Add [`typing.LiteralString`](https://docs.python.org/3.14/library/typing.html#typing.LiteralString), which forms part of [**PEP 675**](https://peps.python.org/pep-0675/). Jelle Zijlstra supplied the patch.

[bpo-46998](https://bugs.python.org/issue?@action=redirect&bpo=46998): Permit subclassing of [`typing.Any`](https://docs.python.org/3.14/library/typing.html#typing.Any). Shantanu Jain supplied the patch.

[bpo-46644](https://bugs.python.org/issue?@action=redirect&bpo=46644): Valid typeforms are no longer obliged to be callable. As a result [`typing.Annotated`](https://docs.python.org/3.14/library/typing.html#typing.Annotated) can wrap [`typing.ParamSpecArgs`](https://docs.python.org/3.14/library/typing.html#typing.ParamSpecArgs) and [`dataclasses.InitVar`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.InitVar). Gregory Beauregard supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
