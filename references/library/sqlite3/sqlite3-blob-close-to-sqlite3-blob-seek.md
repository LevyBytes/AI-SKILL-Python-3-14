# sqlite3.Blob: `close()`, `read()`, `write()`, `tell()`, `seek()`

close()

Close the blob.

After this the blob can no longer be used. Any subsequent operation attempted on it raises an `Error` (or subclass) exception.

 read(*length=-1*, */*)

Pull *length* bytes from the blob starting at the present offset. Should the blob's end be hit, whatever exists up to EOF comes back. With *length* left out or set negative, `read()` keeps going until the blob ends.

 write(*data*, */*)

Put *data* into the blob at the present offset. This call cannot alter the blob's length. Writing past the blob's end raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

 tell()

Hand back the blob's present access position.

 seek(*offset*, *origin=os.SEEK_SET*, */*)

Move the blob's current access position to *offset*. The *origin* argument defaults to [`os.SEEK_SET`](https://docs.python.org/3.14/library/os.html#os.SEEK_SET) (absolute blob positioning). For *origin* the other accepted values are [`os.SEEK_CUR`](https://docs.python.org/3.14/library/os.html#os.SEEK_CUR), which seeks from the present position, and [`os.SEEK_END`](https://docs.python.org/3.14/library/os.html#os.SEEK_END), which seeks from where the blob ends.

[Subject index](INDEX.md) · [Previous](sqlite3-blob-class.md) · [Continue](sqlite3-prepareprotocol-class.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md) · [Owning module, declaration or section: sqlite3.Blob](sqlite3-blob-class.md) · [Owning module, declaration or section: Blob objects](sqlite3-blob-class.md)
