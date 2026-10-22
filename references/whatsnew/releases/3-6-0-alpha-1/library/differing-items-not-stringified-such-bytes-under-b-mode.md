# Python 3.6.0 alpha 1 / library / differing items not stringified such bytes under b mode

[bpo-26837](https://bugs.python.org/issue?@action=redirect&bpo=26837): Differing items that are not stringified (such as bytes under the -b mode) are now reported correctly by assertSequenceEqual(). The change reaches assertListEqual() and assertTupleEqual() as well.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
