# Python 3.5.2 release candidate 1 / library / assertsequenceequal properly prints differing items not stringified such bytes

[bpo-26837](https://bugs.python.org/issue?@action=redirect&bpo=26837): assertSequenceEqual() now properly prints differing items that are not stringified (such as bytes under the -b mode). The change carries over to assertListEqual() and assertTupleEqual().

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
