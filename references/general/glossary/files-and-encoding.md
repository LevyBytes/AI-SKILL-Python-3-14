# Files and encoding

Open when checking Python definitions for files and encoding.

## file object

An object presenting a file-style API (carrying methods like `read()` or `write()`) over some underlying resource. Based on how it came into being, a file object may broker access to an actual on-disk file or instead to some other storage or communication device (such as standard input/output, in-memory buffers, sockets, pipes, and so on). The names *file-like objects* and *streams* also apply to file objects.

In fact three kinds of file objects exist: raw binary files, buffered binary files, and text files. The [`io`](https://docs.python.org/3.14/library/io.html#module-io) module specifies their interfaces. To build a file object the standard route is the [`open()`](https://docs.python.org/3.14/library/functions.html#open) function.

## file-like object

A synonym for file object.

## path-like object

An object that represents a path on the file system. Such an object is either a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) or [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object that denotes a path, or some object that implements the [`os.PathLike`](https://docs.python.org/3.14/library/os.html#os.PathLike) protocol. Calling the [`os.fspath()`](https://docs.python.org/3.14/library/os.html#os.fspath) function converts an object supporting the `os.PathLike` protocol into a `str` or `bytes` file system path; to force a `str` or `bytes` result instead, you can use [`os.fsdecode()`](https://docs.python.org/3.14/library/os.html#os.fsdecode) and [`os.fsencode()`](https://docs.python.org/3.14/library/os.html#os.fsencode) respectively. Introduced by [**PEP 519**](https://peps.python.org/pep-0519/).

## binary file

A file object capable of reading and writing bytes-like objects. Files opened in binary mode (`'rb'`, `'wb'` or `'rb+'`) are examples of binary files, as are [`sys.stdin.buffer`](https://docs.python.org/3.14/library/sys.html#sys.stdin), [`sys.stdout.buffer`](https://docs.python.org/3.14/library/sys.html#sys.stdout), and instances of [`io.BytesIO`](https://docs.python.org/3.14/library/io.html#io.BytesIO) and [`gzip.GzipFile`](https://docs.python.org/3.14/library/gzip.html#gzip.GzipFile).

Refer as well to text file for a file object capable of reading and writing [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) objects.

## text file

A file object capable of reading and writing [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) objects. Frequently a text file is in fact reaching a byte-oriented datastream while taking care of the text encoding for you. Files opened in text mode (`'r'` or `'w'`), [`sys.stdin`](https://docs.python.org/3.14/library/sys.html#sys.stdin), [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout), and instances of [`io.StringIO`](https://docs.python.org/3.14/library/io.html#io.StringIO) are all examples of text files.

Turn to binary file as well, covering a file object that can read and write bytes-like objects.

## text encoding

In Python a string is a sequence of Unicode code points (within the range `U+0000`–`U+10FFFF`). For storage or transfer, that string has to be serialized into a sequence of bytes.

Turning a string into a sequence of bytes goes by the name "encoding", while rebuilding the string out of the sequence of bytes goes by the name "decoding".

A range of different text serialization [codecs](https://docs.python.org/3.14/library/codecs.html#standard-encodings) exists, jointly known as "text encodings".

## filesystem encoding and error handler

The encoding plus error handler that Python applies when decoding operating system bytes and when encoding Unicode for the operating system.

Every byte under 128 must be decodable by the filesystem encoding without failure. Where the file system encoding cannot promise this, API functions may raise [`UnicodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeError).

To retrieve the filesystem encoding and error handler, call the [`sys.getfilesystemencoding()`](https://docs.python.org/3.14/library/sys.html#sys.getfilesystemencoding) and [`sys.getfilesystemencodeerrors()`](https://docs.python.org/3.14/library/sys.html#sys.getfilesystemencodeerrors) functions.

At Python startup the filesystem encoding and error handler get set up by the [`PyConfig_Read()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Read) function: consult the [`filesystem_encoding`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.filesystem_encoding) and [`filesystem_errors`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.filesystem_errors) members of [`PyConfig`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig).

See also the locale encoding.

## locale encoding

Under Unix, this is the encoding belonging to the LC_CTYPE locale. You can set it through [`locale.setlocale(locale.LC_CTYPE, new_locale)`](https://docs.python.org/3.14/library/locale.html#locale.setlocale).

Under Windows, this is the ANSI code page (ex: `"cp1252"`).

On Android and VxWorks, `"utf-8"` is what Python adopts as the locale encoding.

To fetch the locale encoding you can use [`locale.getencoding()`](https://docs.python.org/3.14/library/locale.html#locale.getencoding).

See also the filesystem encoding and error handler.

## universal newlines

A manner of reading text streams in which every one of these is taken to terminate a line: the Unix end-of-line convention `'\n'`, the Windows one `'\r\n'`, plus the old Macintosh convention `'\r'`. See [**PEP 278**](https://peps.python.org/pep-0278/) and [**PEP 3116**](https://peps.python.org/pep-3116/), together with [`bytes.splitlines()`](https://docs.python.org/3.14/library/stdtypes.html#bytes.splitlines) for a further use.

[Glossary context index](INDEX.md).
