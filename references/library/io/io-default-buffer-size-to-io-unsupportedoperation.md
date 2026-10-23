# io - High-level Module Interface

### High-level Module Interface

 io.DEFAULT_BUFFER_SIZE

An int holding the default buffer size that the module's buffered I/O classes rely on. Where it can, [`open()`](https://docs.python.org/3.14/library/functions.html#open) uses the file's blksize (obtained through [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat)).

 io.open(*file*, *mode='r'*, *buffering=-1*, *encoding=None*, *errors=None*, *newline=None*, *closefd=True*, *opener=None*)

This serves as an alias for the builtin `open()` function.

An [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) named `open` is raised by this function, carrying the arguments *path*, *mode* and *flags*. Note that the *mode* and *flags* values passed there may have been adjusted, or deduced, relative to the original call.

 io.open_code(*path*)

Opens the supplied file in mode `'rb'`. Reach for this function whenever your aim is to handle the contents as executable code.

*path* should be a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) and an absolute path.

A prior call to [`PyFile_SetOpenCodeHook()`](https://docs.python.org/3.14/c-api/file.html#c.PyFile_SetOpenCodeHook) can override how this function behaves. That said, provided *path* is a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) and an absolute path, `open_code(path)` ought to act identically to `open(path, 'rb')` in every case. The point of overriding the behavior is to allow extra validation or preprocessing of the file.

Added in version 3.8.

 io.text_encoding(*encoding*, *stacklevel=2*, */*)

For callables that rely on [`open()`](https://docs.python.org/3.14/library/functions.html#open) or `TextIOWrapper` and expose an `encoding=None` parameter, this acts as a helper function.

When *encoding* is not `None`, this function hands it back. If not, it returns `"locale"` or `"utf-8"` according to [UTF-8 Mode](https://docs.python.org/3.14/library/os.html#utf8-mode).

An [`EncodingWarning`](https://docs.python.org/3.14/library/exceptions.html#EncodingWarning) is emitted by this function whenever [`sys.flags.warn_default_encoding`](https://docs.python.org/3.14/library/sys.html#sys.flags) holds true and *encoding* equals `None`. The spot at which that warning surfaces is set by *stacklevel*. As an illustration:

```python
def read_text(path, encoding=None):
    encoding = io.text_encoding(encoding)  # stacklevel=2
    with open(path, encoding) as f:
        return f.read()

```

Here, the [`EncodingWarning`](https://docs.python.org/3.14/library/exceptions.html#EncodingWarning) is raised for whoever calls `read_text()`.

Refer to Text Encoding for additional information.

Added in version 3.10.

Changed in version 3.11: With UTF-8 mode turned on and *encoding* set to `None`, `text_encoding()` now hands back “utf-8”.

 *exception *io.BlockingIOError

This is a compatibility alias for the builtin `BlockingIOError` exception.

 *exception *io.UnsupportedOperation

An exception that derives from [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) and [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError), raised whenever an unsupported operation is invoked on a stream.

See also

[`sys`](https://docs.python.org/3.14/library/sys.html#module-sys)

holds the standard IO streams: [`sys.stdin`](https://docs.python.org/3.14/library/sys.html#sys.stdin), [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout), and [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr).

[Subject index](INDEX.md) · [Previous](opt-in-encodingwarning.md) · [Continue](class-hierarchy.md) · [Owning module, declaration or section: io](io-core-tools-for-working-with-streams.md)
