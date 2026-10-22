# Python 3.13.0 alpha 2 / library / io

[gh-111174](https://github.com/python/cpython/issues/111174): Resolve a crash in [`io.BytesIO.getbuffer()`](https://docs.python.org/3.14/library/io.html#io.BytesIO.getbuffer) when it is invoked over and over on an empty BytesIO.

[gh-111942](https://github.com/python/cpython/issues/111942): Resolve crashes inside [`io.TextIOWrapper.reconfigure()`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper.reconfigure) triggered by bad arguments, such as a non-string encoding.

[gh-111356](https://github.com/python/cpython/issues/111356): The entries [`io.text_encoding()`](https://docs.python.org/3.14/library/io.html#io.text_encoding), [`io.DEFAULT_BUFFER_SIZE`](https://docs.python.org/3.14/library/io.html#io.DEFAULT_BUFFER_SIZE), and [`io.IncrementalNewlineDecoder`](https://docs.python.org/3.14/library/io.html#io.IncrementalNewlineDecoder) were added to `io.__all__`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
