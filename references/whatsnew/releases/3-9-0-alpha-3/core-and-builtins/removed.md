# Python 3.9.0 alpha 3 / core and builtins / removed

[bpo-39320](https://bugs.python.org/issue?@action=redirect&bpo=39320): Swap four intricate sequence-building bytecodes for three simpler ones.

These four bytecodes have been removed:

  - BUILD_LIST_UNPACK

  - BUILD_TUPLE_UNPACK

  - BUILD_SET_UNPACK

  - BUILD_TUPLE_UNPACK_WITH_CALL

These three bytecodes have been added:

  - LIST_TO_TUPLE

  - LIST_EXTEND

  - SET_UPDATE

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
