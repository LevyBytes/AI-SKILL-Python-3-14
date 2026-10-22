# StreamReader: `feed_eof()`, `read()`, `readline()`, `readexactly()`, `readuntil()`, `at_eof()`

feed_eof()

Register the EOF.

 `*async *read(*n=-1*)`

Pull as many as *n* bytes off the stream.

When *n* is omitted or set to `-1`, keep reading up to EOF and then return everything read as [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes). Should EOF have arrived with the internal buffer empty, an empty `bytes` object comes back.

When *n* is `0`, an empty `bytes` object is returned at once.

When *n* is positive, hand back up to *n* available `bytes` the moment at least 1 byte sits in the internal buffer. Should EOF arrive before a single byte is read, return an empty `bytes` object.

 `*async *readline()`

Read a lone line, a “line” being a run of bytes terminated by `\n`.

Should EOF arrive without `\n` having turned up, the method gives back whatever was read so far.

Should EOF arrive while the internal buffer is empty, an empty `bytes` object is returned.

 `*async *readexactly(*n*)`

Read precisely *n* bytes.

Raise an [`IncompleteReadError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.IncompleteReadError) when EOF turns up before *n* bytes are available. The [`IncompleteReadError.partial`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.IncompleteReadError.partial) attribute then yields the data read up to that point.

 `*async *readuntil(*separator=b'\n'*)`

Keep reading from the stream until *separator* shows up.

On a hit, the data together with the separator is pulled out of the internal buffer (consumed). The data handed back carries the separator at its tail.

Should the volume read pass the stream's configured limit, a [`LimitOverrunError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.LimitOverrunError) exception fires, and the data remains in the internal buffer for a later read.

Should EOF arrive before the whole separator turns up, an [`IncompleteReadError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.IncompleteReadError) exception fires and the internal buffer is cleared. The [`IncompleteReadError.partial`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.IncompleteReadError.partial) attribute might then hold a fragment of the separator.

*separator* is allowed to be a tuple of separators as well. Then the value returned is the shortest one whose suffix is any of those separators. As far as [`LimitOverrunError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.LimitOverrunError) is concerned, the shortest possible separator is taken to be whichever one matched.

Added in version 3.5.2.

Changed in version 3.13: A [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple) of separators is now allowed for the *separator* parameter.

 at_eof()

Return `True` when the buffer holds nothing and `feed_eof()` has been called.

[Subject index](INDEX.md) · [Previous](asyncio-streamreader-class.md) · [Continue](asyncio-streamwriter-class.md) · [Owning module, declaration or section: asyncio.StreamReader](asyncio-streamreader-class.md) · [Owning module, declaration or section: StreamReader](asyncio-streamreader-class.md)
