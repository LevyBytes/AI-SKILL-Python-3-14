# Python 3.5.3 release candidate 1 / core and builtins / numeric behavior

[bpo-27473](https://bugs.python.org/issue?@action=redirect&bpo=27473): Repair a possible integer overflow during bytes and bytearray concatenation. Xiang Zhang supplied the patch.

[bpo-27507](https://bugs.python.org/issue?@action=redirect&bpo=27507): Add an integer-overflow check inside bytearray.extend(). Xiang Zhang supplied the patch.

[bpo-27581](https://bugs.python.org/issue?@action=redirect&bpo=27581): Stop depending on wraparound for the overflow check inside PySequence_Tuple(). Xiang Zhang supplied the patch.

[bpo-27443](https://bugs.python.org/issue?@action=redirect&bpo=27443): __length_hint__() on bytearray iterators no longer hands back a negative integer once a bytearray is resized.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
