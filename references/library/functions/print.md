# print

print(**objects*, *sep=' '*, *end='\n'*, *file=None*, *flush=False*)

Write each of the *objects* onto the text stream *file*, placing *sep* between them and appending *end* at the close. Whenever *sep*, *end*, *file*, or *flush* appear, they have to be supplied by keyword.

Every positional argument gets turned into text the same way [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) would, then emitted to the stream with *sep* dividing them and *end* trailing. *sep* and *end* alike are required to be strings; alternatively either can be `None`, signaling that the defaults apply. When you pass no *objects* at all, `print()` simply emits *end*.

Whatever you supply for *file* has to expose a `write(string)` method; should that argument be missing or `None`, the call falls back to [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout). Because the things passed in get rendered as text strings, you can't hand `print()` a file object opened in binary mode. When that's your situation, reach for `file.write(...)` instead.

How the stream buffers normally hinges on *file*. That said, a true value for *flush* forces the stream to flush right away.

Changed in version 3.3: The *flush* keyword argument was introduced.

[Builtin task index](INDEX.md).
