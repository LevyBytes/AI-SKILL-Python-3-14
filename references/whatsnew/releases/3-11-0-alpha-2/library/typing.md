# Python 3.11.0 alpha 2 / library / typing

[bpo-45679](https://bugs.python.org/issue?@action=redirect&bpo=45679): Repair caching for multi-value [`typing.Literal`](https://docs.python.org/3.14/library/typing.html#typing.Literal). `Literal[True, 2]` no longer compares equal to `Literal[1, 2]`.

[bpo-45489](https://bugs.python.org/issue?@action=redirect&bpo=45489): Extend [`ForwardRef`](https://docs.python.org/3.14/library/typing.html#typing.ForwardRef) so it handles the `|` operator. Donghee Na wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
