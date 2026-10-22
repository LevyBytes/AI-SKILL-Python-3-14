# io: `io.FileIO`

### Raw File I/O

 *class *io.FileIO(*name*, *mode='r'*, *closefd=True*, *opener=None*)

A raw binary stream that stands for an OS-level file holding bytes data. It derives from `RawIOBase` and carries out that class’s low-level access design. As a result, `write()` makes no promise that every byte lands, and `read()` can come back with fewer bytes than asked for even though additional bytes might sit in the backing file. For “write all” and “read at least” semantics, reach for Binary I/O instead.

The *name* may take either of two forms:

- a character string or [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object giving the path of the file to be opened. Here closefd has to be `True` (its default), or else an error is raised.

- an integer giving the number of an already-open OS-level file descriptor that the resulting `FileIO` object will work through. That fd is closed together with the FileIO object unless *closefd* has been set to `False`.

The *mode* may be `'r'`, `'w'`, `'x'` or `'a'`, standing for reading (the default), writing, exclusive creation, or appending. A file opened for writing or appending is created when it is absent; opening for writing also truncates it. Opening for creation raises [`FileExistsError`](https://docs.python.org/3.14/library/exceptions.html#FileExistsError) should the file already be present. Because creation entails writing, this mode operates much like `'w'`. Append a `'+'` to the mode to permit reading and writing together.

To supply a custom opener, hand a callable in as *opener*. The file object’s backing file descriptor then comes from invoking *opener* with (*name*, *flags*). *opener* has to hand back an open file descriptor (supplying [`os.open`](https://docs.python.org/3.14/library/os.html#os.open) as *opener* yields behavior much like supplying `None`).

The file just created is [non-inheritable](https://docs.python.org/3.14/library/os.html#fd-inheritance).

Consult the [`open()`](https://docs.python.org/3.14/library/functions.html#open) built-in function for samples that demonstrate the *opener* parameter.

Warning

`FileIO` is a low-level I/O object, and its members—`read()` and `write()` among them—require that their return values be examined directly within a retry loop to achieve “write all” and “read at least” semantics. The high-level I/O objects Binary I/O and Text I/O handle retrying for you.

Changed in version 3.3: Introduced the *opener* parameter, along with the `'x'` mode.

Changed in version 3.4: Files are non-inheritable from this release onward.

On top of the attributes inherited from `RawIOBase` and `IOBase`, `FileIO` exposes these data attributes:

[Subject index](INDEX.md) · [Previous](io-bufferediobase-read1-to-io-bufferediobase-write.md) · [Continue](raw-file-i-o.md) · [Owning module, declaration or section: io](io-core-tools-for-working-with-streams.md)
