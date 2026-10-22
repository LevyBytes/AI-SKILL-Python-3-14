# Python 3.7.0 alpha 1 / core and builtins / numeric behavior

[bpo-30537](https://bugs.python.org/issue?@action=redirect&bpo=30537): For its start, stop, and slice arguments, itertools.islice now tolerates integer-like objects (those exposing an __index__ method)

[bpo-29839](https://bugs.python.org/issue?@action=redirect&bpo=29839): When __len__() hands back a big negative integer, len() now raises ValueError in place of OverflowError.

[bpo-29695](https://bugs.python.org/issue?@action=redirect&bpo=29695): Keyword arguments are no longer accepted by bool(), float(), list() and tuple(). The first argument to int() may now only be supplied positionally.

[bpo-28621](https://bugs.python.org/issue?@action=redirect&bpo=28621): Accelerated the int-to-float conversion by reusing a quicker bits-counting routine. Adrian Wielgosik wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
