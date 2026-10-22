# Python 3.6.0 beta 2 / library / memory and lifetimes

[bpo-27778](https://bugs.python.org/issue?@action=redirect&bpo=27778): Closed an os.getrandom() memory leak that occurred whenever a signal interrupts getrandom() and the corresponding signal handler then raises a Python exception.

[bpo-27932](https://bugs.python.org/issue?@action=redirect&bpo=27932): Stopped a memory leak inside win32_ver().

- Corrects an UnboundLocalError within socket._sendfile_use_sendfile.

[bpo-28275](https://bugs.python.org/issue?@action=redirect&bpo=28275): Closed a possible use-after-free in the decompress() methods belonging to the LZMADecompressor and BZ2Decompressor classes. John Leitch supplied the original patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
