# Python 3.5.0 alpha 3 / library / support arbitrary bytes like objects added needless copying memoryview within

[bpo-23688](https://bugs.python.org/issue?@action=redirect&bpo=23688): Support for arbitrary bytes-like objects was added, and needless copying of memoryview within gzip.GzipFile.write() was avoided. Wolfgang Maier supplied the original patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
