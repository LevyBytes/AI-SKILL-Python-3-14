# Python 3.5.1 release candidate 1 / library / zlib

[bpo-25626](https://bugs.python.org/issue?@action=redirect&bpo=25626): Three zlib functions were changed to take sizes fitting in Py_ssize_t while internally clamping those sizes down to UINT_MAX. This clears a 3.5 regression where GzipFile.read() could not read chunks above 2 or 4 GiB. Affected here are three arguments: on zlib.Decompress.decompress() its max_length parameter; on zlib.decompress() its bufsize parameter; plus, on zlib.Decompress.flush(), that call's length parameter.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
