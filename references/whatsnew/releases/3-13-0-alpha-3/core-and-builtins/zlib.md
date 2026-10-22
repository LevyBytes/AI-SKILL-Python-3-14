# Python 3.13.0 alpha 3 / core and builtins / zlib

[gh-105967](https://github.com/python/cpython/issues/105967): Worked around a defect in Apple’s macOS platform zlib library under which [`zlib.crc32()`](https://docs.python.org/3.14/library/zlib.html#zlib.crc32) and [`binascii.crc32()`](https://docs.python.org/3.14/library/binascii.html#binascii.crc32) might yield wrong results across multi-gigabyte inputs. This also covered uses of [`zipfile`](https://docs.python.org/3.14/library/zipfile.html#module-zipfile) on archives holding large data.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
