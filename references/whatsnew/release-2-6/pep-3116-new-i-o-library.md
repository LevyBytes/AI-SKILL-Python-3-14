# What’s New in Python 2.6 / PEP 3116: New I/O Library — io, readline

### PEP 3116: New I/O Library

Although Python's built-in file objects come with many methods, file-like objects need not provide all of them. Things that mimic files normally offer `read()` and `write()`, yet they might lack `readline()`, say. Python 3.0 brings a layered I/O library inside the [`io`](https://docs.python.org/3.14/library/io.html#module-io) module, peeling the buffering and text-handling layers apart from the basic read and write primitives.

The [`io`](https://docs.python.org/3.14/library/io.html#module-io) module furnishes three tiers of abstract base classes:

- [`RawIOBase`](https://docs.python.org/3.14/library/io.html#io.RawIOBase) spells out raw I/O operations: [`read()`](https://docs.python.org/3.14/library/io.html#io.RawIOBase.read), [`readinto()`](https://docs.python.org/3.14/library/io.html#io.RawIOBase.readinto), [`write()`](https://docs.python.org/3.14/library/io.html#io.RawIOBase.write), [`seek()`](https://docs.python.org/3.14/library/io.html#io.IOBase.seek), [`tell()`](https://docs.python.org/3.14/library/io.html#io.IOBase.tell), [`truncate()`](https://docs.python.org/3.14/library/io.html#io.IOBase.truncate), and [`close()`](https://docs.python.org/3.14/library/io.html#io.IOBase.close). Frequently each of this class's methods corresponds to one system call. It additionally supplies [`readable()`](https://docs.python.org/3.14/library/io.html#io.IOBase.readable), [`writable()`](https://docs.python.org/3.14/library/io.html#io.IOBase.writable), and [`seekable()`](https://docs.python.org/3.14/library/io.html#io.IOBase.seekable) methods so you can discover which operations a particular object permits.

Python 3.0 ships concrete versions of this class covering files and sockets, but Python 2.6 has not reworked its own file and socket objects along these lines.

- [`BufferedIOBase`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase) is an abstract base class that holds data in memory to cut down on the system calls performed, which makes I/O handling more efficient. It carries every method of [`RawIOBase`](https://docs.python.org/3.14/library/io.html#io.RawIOBase) and tacks on a [`raw`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase.raw) attribute that points to the underlying raw object.

Five concrete classes realize this ABC. [`BufferedWriter`](https://docs.python.org/3.14/library/io.html#io.BufferedWriter) and [`BufferedReader`](https://docs.python.org/3.14/library/io.html#io.BufferedReader) serve objects that are write-only or read-only and that own a [`seek()`](https://docs.python.org/3.14/library/io.html#io.IOBase.seek) method for random access. [`BufferedRandom`](https://docs.python.org/3.14/library/io.html#io.BufferedRandom) objects allow both reading and writing against one shared underlying stream, while [`BufferedRWPair`](https://docs.python.org/3.14/library/io.html#io.BufferedRWPair) targets objects like TTYs that pair read and write operations over two unconnected data streams. The [`BytesIO`](https://docs.python.org/3.14/library/io.html#io.BytesIO) class permits reading, writing, and seeking across a buffer kept in memory.

- [`TextIOBase`](https://docs.python.org/3.14/library/io.html#io.TextIOBase): Offers functions for reading and writing strings (recall that in Python 3.0 strings are Unicode), and backs [universal newlines](https://docs.python.org/3.14/glossary.html#term-universal-newlines). `TextIOBase` declares the [`readline()`](https://docs.python.org/3.14/library/readline.html#module-readline) method and lets you iterate over objects.

Two concrete versions exist. [`TextIOWrapper`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper) wraps around a buffered I/O object, providing every text I/O method and gaining a [`buffer`](https://docs.python.org/3.14/library/io.html#io.TextIOBase.buffer) attribute for reaching the wrapped object. [`StringIO`](https://docs.python.org/3.14/library/io.html#io.StringIO) merely keeps it all in memory, never committing anything to disk.

(Inside Python 2.6, [`io.StringIO`](https://docs.python.org/3.14/library/io.html#io.StringIO) is coded entirely in pure Python and is therefore quite slow. For the moment you ought to keep using the existing `StringIO` module or `cStringIO`. Eventually Python 3.0's [`io`](https://docs.python.org/3.14/library/io.html#module-io) module will be reimplemented in C for speed, and that C version may well be backported into the 2.x releases.)

Within Python 2.6, the actual implementations have not been rebuilt on top of the [`io`](https://docs.python.org/3.14/library/io.html#module-io) module's classes. The module is shipped chiefly to ease writing code that stays forward-compatible with 3.0 and to spare developers from coding their own buffering and text I/O machinery.

See also

[**PEP 3116**](https://peps.python.org/pep-3116/) - New I/O

The PEP's authors were Daniel Stutzbach, Mike Verdone, and Guido van Rossum. Its code came from Guido van Rossum, Georg Brandl, Walter Doerwald, Jeremy Hylton, Martin von Löwis, Tony Lownds, plus additional contributors.

[Subject index](INDEX.md) · [Previous source section](pep-3112-byte-literals.md) · [Next source section](pep-3118-revised-buffer-protocol.md) · [Release/subject declaration](python-3-0.md)
