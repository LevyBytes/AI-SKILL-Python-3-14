# Python 3.6.3 release candidate 1 / library / build and platforms

[bpo-27340](https://bugs.python.org/issue?@action=redirect&bpo=27340): To build slices of data, SSLSocket.sendall() now relies on memoryview. This brings support for every bytes-like object, and on top of that it is faster and skips expensive copies.

[bpo-9146](https://bugs.python.org/issue?@action=redirect&bpo=9146): Repair a segmentation fault inside _hashopenssl whenever standard hash functions like md5 are missing from the linked OpenSSL library, as happens in certain special FIPS-140 build environments.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
