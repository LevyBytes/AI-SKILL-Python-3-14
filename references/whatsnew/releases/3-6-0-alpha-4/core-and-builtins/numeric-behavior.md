# Python 3.6.0 alpha 4 / core and builtins / numeric behavior

[bpo-27507](https://bugs.python.org/issue?@action=redirect&bpo=27507): Add an integer overflow check inside bytearray.extend(). Xiang Zhang wrote the patch.

[bpo-27581](https://bugs.python.org/issue?@action=redirect&bpo=27581): Within PySequence_Tuple(), stop depending on wrapping for the overflow check. Xiang Zhang wrote the patch.

[bpo-1621](https://bugs.python.org/issue?@action=redirect&bpo=1621): Steer clear of signed integer overflow in list and tuple operations. Xiang Zhang wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
