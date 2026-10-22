# ssl / Memory BIO support: `ssl.MemoryBIO`, `read()`, `write()`, `write_eof()`

*class *ssl.MemoryBIO

A memory buffer usable for moving data between Python and an SSL protocol instance.

 pending

Return the count of bytes presently held in the memory buffer.

 eof

A boolean reporting whether the memory BIO currently sits at the end-of-file position.

 read(*n=-1*, */*)

Read as many as *n* bytes out of the memory buffer. When *n* is left out or negative, every byte is returned.

 write(*buf*, */*)

Write the bytes contained in *buf* into the memory BIO. The *buf* argument has to be an object that supports the buffer protocol.

What gets returned is the count of bytes written, which always matches the length of *buf*.

 write_eof()

Write an EOF marker into the memory BIO. Once you have called this method, calling `write()` is no longer permitted. The `eof` attribute turns true after every byte still in the buffer has been read.

[Subject index](INDEX.md) · [Previous](ssl-sslobject-version.md) · [Continue](ssl-sslsession-class.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md) · [Owning module, declaration or section: Memory BIO support](ssl-sslobject-class.md)
