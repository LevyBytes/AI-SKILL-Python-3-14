# Python 3.7.0 alpha 1 / core and builtins / shift operation less likely raise overflowerror

[bpo-29816](https://bugs.python.org/issue?@action=redirect&bpo=29816): The shift operation is now less likely to raise OverflowError. For negative counts, ValueError is always raised in place of OverflowError. Shifting zero by a non-negative count always yields zero.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
