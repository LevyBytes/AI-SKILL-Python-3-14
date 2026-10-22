# Python 3.14.3 final / library / io

[gh-142594](https://github.com/python/cpython/issues/142594): A crash in `TextIOWrapper.close()`, hit when the underlying buffer's `closed` property invokes [`detach()`](https://docs.python.org/3.14/library/io.html#io.TextIOBase.detach), is now fixed.

[gh-144380](https://github.com/python/cpython/issues/144380): Line iteration over [`io.BufferedReader`](https://docs.python.org/3.14/library/io.html#io.BufferedReader) is now roughly 49% faster.

[gh-143602](https://github.com/python/cpython/issues/143602): By deduplicating the buffer exports, an inconsistency in [`write()`](https://docs.python.org/3.14/library/io.html#io.RawIOBase.write) that resulted in unexpected buffer overwrite is now fixed.

[gh-143378](https://github.com/python/cpython/issues/143378): Use-after-free crashes that occurred when a [`BytesIO`](https://docs.python.org/3.14/library/io.html#io.BytesIO) object was mutated concurrently during [`write()`](https://docs.python.org/3.14/library/io.html#io.RawIOBase.write) or [`writelines()`](https://docs.python.org/3.14/library/io.html#io.IOBase.writelines) are now fixed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
