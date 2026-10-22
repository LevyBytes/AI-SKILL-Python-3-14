# Built-in Functions — Signature and initial contract

open(*file*, *mode='r'*, *buffering=-1*, *encoding=None*, *errors=None*, *newline=None*, *closefd=True*, *opener=None*)

Open *file* and hand back a matching [file object](https://docs.python.org/3.14/glossary.html#term-file-object). Should the file fail to open, an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) gets raised. Consult [Reading and Writing Files](https://docs.python.org/3.14/tutorial/inputoutput.html#tut-files) for additional examples of putting this function to use.

*file* is a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) supplying the pathname (either absolute or relative to the present working directory) of the file to open, or alternatively an integer file descriptor of the file to wrap. (When a file descriptor is supplied, it closes once the returned I/O object closes, unless *closefd* has been set to `False`.)

*mode* is an optional string naming the mode the file opens in. Its default is `'r'`, signifying open for reading in text mode. Among the other common values: `'w'` handles writing (and truncates the file when one is already there), `'x'` handles exclusive creation, while `'a'` handles appending (where, across *some* Unix systems, *all* writes land at the file's end regardless of the present seek position). In text mode, when *encoding* goes unspecified the encoding chosen is platform-dependent: [`locale.getencoding()`](https://docs.python.org/3.14/library/locale.html#locale.getencoding) is invoked to fetch the current locale encoding. (To read and write raw bytes, use binary mode and leave *encoding* unspecified.) These are the available modes:

| Character | Meaning |
| --- | --- |
| `'r'` | open for reading (default) |
| `'w'` | open for writing, truncating the file first |
| `'x'` | open for exclusive creation, failing if the file already exists |
| `'a'` | open for writing, appending to the end of file if it exists |
| `'b'` | binary mode |
| `'t'` | text mode (default) |
| `'+'` | open for updating (reading and writing) |

By default the mode is `'r'` (reading text, equivalent to `'rt'`). The pair `'w+'` and `'w+b'` both open the file while truncating it. The pair `'r+'` and `'r+b'` both open it leaving it untruncated.

Per the [Overview](https://docs.python.org/3.14/library/io.html#io-overview), Python draws a line between binary and text I/O. Files opened in binary mode (which includes `'b'` in the *mode* argument) hand back contents as [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) objects free of any decoding. In text mode (the default, or whenever `'t'` appears in the *mode* argument), the file’s contents come back as [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), the bytes having first been decoded with a platform-dependent encoding or with the supplied *encoding* when one is given.

Note

Python does not lean on the underlying operating system’s notion of text files; the whole of the processing is carried out by Python itself, making it platform-independent.

*buffering* is an optional integer that sets the buffering policy. Pass 0 to turn buffering off (permitted only in binary mode), 1 to choose line buffering (usable only when writing in text mode), and an integer > 1 to give the size in bytes of a fixed-size chunk buffer. Note that giving a buffer size in this manner applies to binary buffered I/O, yet `TextIOWrapper` (that is, files opened with `mode='r+'`) would have its own separate buffering. To turn off buffering in `TextIOWrapper`, think about using the `write_through` flag for [`io.TextIOWrapper.reconfigure()`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper.reconfigure). When no *buffering* argument is supplied, the default buffering policy operates as follows:

- Binary files get buffered in fixed-size chunks; the buffer’s size is `max(min(blocksize, 8 MiB), DEFAULT_BUFFER_SIZE)` whenever the device block size can be determined. On the majority of systems, the buffer is usually 128 kilobytes long.

- “Interactive” text files (those for which [`isatty()`](https://docs.python.org/3.14/library/io.html#io.IOBase.isatty) yields `True`) employ line buffering. Remaining text files follow the policy laid out above for binary files.

*encoding* is the name of the encoding employed to decode or encode the file. It should be used only in text mode. The default encoding hinges on the platform (whatever [`locale.getencoding()`](https://docs.python.org/3.14/library/locale.html#locale.getencoding) yields), yet any [text encoding](https://docs.python.org/3.14/glossary.html#term-text-encoding) that Python supports may be used. Consult the [`codecs`](https://docs.python.org/3.14/library/codecs.html#module-codecs) module for the roster of supported encodings.

*errors* is an optional string naming how encoding and decoding errors get handled—this is unavailable in binary mode. A range of standard error handlers can be had (catalogued under [Error Handlers](https://docs.python.org/3.14/library/codecs.html#error-handlers)), though any error handling name registered through [`codecs.register_error()`](https://docs.python.org/3.14/library/codecs.html#codecs.register_error) is valid too. The standard names take in:

- `'strict'` to raise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) exception whenever an encoding error occurs. The default value of `None` carries the same effect.

- `'ignore'` skips over errors. Be aware that disregarding encoding errors may bring about data loss.

- `'replace'` brings about a replacement marker (such as `'?'`) being placed where the data is malformed.

- `'surrogateescape'` will render any erroneous bytes as low surrogate code units running from U+DC80 to U+DCFF. These surrogate code units then convert back into the very same bytes whenever the `surrogateescape` error handler is in use while writing data. This proves useful for handling files whose encoding is unknown.

- `'xmlcharrefreplace'` works only while writing to a file. Characters the encoding cannot handle get swapped out for the corresponding XML character reference `&#*nnn*;`.

- `'backslashreplace'` swaps malformed data for Python’s backslashed escape sequences.

- `'namereplace'` (likewise available only while writing) swaps unsupported characters for `\N{...}` escape sequences.

*newline* governs how newline characters are parsed out of the stream. It may be `None`, `''`, `'\n'`, `'\r'`, and `'\r\n'`. Its behavior is as follows:

- While reading input out of the stream, when *newline* is `None`, universal newlines mode switches on. Lines within the input may end in `'\n'`, `'\r'`, or `'\r\n'`, and these get translated into `'\n'` before reaching the caller. When it is `''`, universal newlines mode switches on, yet line endings reach the caller untranslated. When it holds any of the other legal values, input lines are terminated solely by the given string, and the line ending reaches the caller untranslated.

- While writing output to the stream, when *newline* is `None`, any `'\n'` characters written get translated into the system default line separator, [`os.linesep`](https://docs.python.org/3.14/library/os.html#os.linesep). When *newline* is `''` or `'\n'`, no translation happens. When *newline* is any of the other legal values, any `'\n'` characters written get translated into the given string.

When *closefd* is `False` and a file descriptor rather than a filename was supplied, the underlying file descriptor stays open after the file closes. When a filename is supplied *closefd* has to be `True` (the default); if not, an error gets raised.

A custom opener is available when you pass a callable for *opener*. The file object's underlying file descriptor is then obtained by invoking *opener* with (*file*, *flags*). *opener* has to hand back an open file descriptor (passing [`os.open`](https://docs.python.org/3.14/library/os.html#os.open) as *opener* yields functionality akin to passing `None`).

The freshly created file is [non-inheritable](https://docs.python.org/3.14/library/os.html#fd-inheritance).

[Subject index](INDEX.md) · [Previous](oct.md) · [Continue](file-opening-relative-to-directory-descriptor.md) · [Owning module, declaration or section: Built-in Functions](INDEX.md)
