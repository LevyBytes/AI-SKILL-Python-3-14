# Python 3.6.0 alpha 4 / library / compression

[bpo-27130](https://bugs.python.org/issue?@action=redirect&bpo=27130): Within the "zlib" module, correct the handling of large buffers (around 4 GiB) during compression and decompression. Earlier, inputs were capped at 4 GiB, and neither compression nor decompression coped properly with 4 GiB results.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
