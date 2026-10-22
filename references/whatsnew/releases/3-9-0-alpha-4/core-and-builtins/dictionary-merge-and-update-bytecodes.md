# Python 3.9.0 alpha 4 / core and builtins / swap out two intricate dict building bytecodes pair plainer ones

[bpo-39320](https://bugs.python.org/issue?@action=redirect&bpo=39320): Swap out two intricate dict-building bytecodes for a pair of plainer ones. The fresh bytecodes `DICT_MERGE` and `DICT_UPDATE` have been added The old bytecodes `BUILD_MAP_UNPACK` and `BUILD_MAP_UNPACK_WITH_CALL` have been removed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
