# Python 3.5.0 alpha 4 / library / cap how much decompressed data read gzipfile bz2file or

[bpo-23529](https://bugs.python.org/issue?@action=redirect&bpo=23529): Cap how much decompressed data is read from GzipFile, BZ2File or LZMAFile. That blocks denial of service attacks built on compressed bombs (that is, compressed payloads expanding to an enormous size). Martin Panter and Nikolaus Rath wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
