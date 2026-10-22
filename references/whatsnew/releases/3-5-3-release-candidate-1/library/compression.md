# Python 3.5.3 release candidate 1 / library / compression

[bpo-28449](https://bugs.python.org/issue?@action=redirect&bpo=28449): tarfile.open() in mode "r" or "r:" now attempts to open a tar file with compression before attempting it without compression. Otherwise there was a 50% chance of failure when ignore_zeros=True.

[bpo-27130](https://bugs.python.org/issue?@action=redirect&bpo=27130): Within the "zlib" module, corrected the treatment of large buffers (commonly 4 GiB) during compression and decompression. Beforehand, inputs were capped at 4 GiB, and neither the compress nor the decompress paths dealt correctly with 4 GiB results.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
