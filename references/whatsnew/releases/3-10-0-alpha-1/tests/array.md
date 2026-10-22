# Python 3.10.0 alpha 1 / tests / array

[bpo-41085](https://bugs.python.org/issue?@action=redirect&bpo=41085): Patch the integer overflow in the [`array.array.index()`](https://docs.python.org/3.14/library/array.html#array.array.index) method on 64-bit Windows whenever the index runs larger than `2**31`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
