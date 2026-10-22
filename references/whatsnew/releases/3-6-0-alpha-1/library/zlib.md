# Python 3.6.0 alpha 1 / library / zlib

[bpo-25626](https://bugs.python.org/issue?@action=redirect&bpo=25626): Three zlib functions are reworked so they accept sizes representable in Py_ssize_t, while internally those sizes get clamped down to UINT_MAX. Doing so clears a 3.5 regression where GzipFile.read() could not read chunks beyond 2 or 4 GiB. Specifically, the touched surfaces are: first, the max_length parameter of zlib.Decompress.decompress(); next, and separately, the bufsize parameter belonging to zlib.decompress(); and finally the length parameter on zlib.Decompress.flush().

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
