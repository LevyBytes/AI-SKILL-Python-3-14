# Python 3.9.0 alpha 1 / build / build and platforms

[bpo-25361](https://bugs.python.org/issue?@action=redirect&bpo=25361): Enables use of SSE2 instructions in Windows 32-bit build.

[bpo-38809](https://bugs.python.org/issue?@action=redirect&bpo=38809): Under Windows, the build scripts will from now on detect and employ python.exe out of an active virtual env.

[bpo-38684](https://bugs.python.org/issue?@action=redirect&bpo=38684): Repair the _hashlib build for the case where Blake2 is turned off yet OpenSSL provides it.

[bpo-38301](https://bugs.python.org/issue?@action=redirect&bpo=38301): Within the Solaris family we have to make certain `-D_REENTRANT` is used. Jesús Cea Avión supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
