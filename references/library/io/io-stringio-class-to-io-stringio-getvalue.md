# io / Text I/O: `io.StringIO`, `getvalue()`

*class *io.StringIO(*initial_value=''*, *newline='\n'*)

A text stream backed by an in-memory text buffer. It derives from `TextIOBase`.

Calling the `close()` method throws the text buffer away.

You can seed the buffer’s starting value through *initial_value*. With newline translation turned on, newlines are encoded just as `write()` would. Positioned at the buffer’s start, the stream behaves like an existing file freshly opened in `w+` mode: poised either to write straight away from the front, or to clobber whatever the initial value held. To mimic opening a file in `a+` mode ready for appending, call `f.seek(0, io.SEEK_END)` to move the stream to the end of the buffer.

The *newline* argument behaves as it does for `TextIOWrapper`, save that when writing output to the stream, a *newline* of `None` causes newlines to be written as `\n` on every platform.

Beyond the methods from `TextIOBase` and `IOBase`, `StringIO` supplies this method:

 getvalue()

Hand back a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) holding the buffer’s full contents. Newlines are decoded just as `read()` would, though the stream position stays put.

Example usage:

```python
import io

output = io.StringIO()
output.write('First line.\n')
print('Second line.', file=output)

# Retrieve file contents -- this will be
# 'First line.\nSecond line.\n'
contents = output.getvalue()

# Close object and discard memory buffer --
# .getvalue() will now raise an exception.
output.close()

```

[Subject index](INDEX.md) · [Previous](io-textiowrapper-seek-to-io-textiowrapper-tell.md) · [Continue](io-incrementalnewlinedecoder-class.md) · [Owning module, declaration or section: io](io-core-tools-for-working-with-streams.md) · [Owning module, declaration or section: Text I/O](io-textiobase-class.md)
