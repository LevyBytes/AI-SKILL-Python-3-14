# Python 3.6.0 alpha 3 / core and builtins / numeric behavior

[bpo-27473](https://bugs.python.org/issue?@action=redirect&bpo=27473): Closed a potential integer overflow during bytes and bytearray concatenation. Xiang Zhang provided the patch.

[bpo-27443](https://bugs.python.org/issue?@action=redirect&bpo=27443): After a bytearray is resized, __length_hint__() on its iterators stops handing back a negative integer.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
