# Transferring files

### Transferring files

 *async *loop.sendfile(*transport*, *file*, *offset=0*, *count=None*, ***, *fallback=True*)

Push a *file* across a *transport*. The grand total of bytes sent is what gets returned.

When it is available, the method takes advantage of high-performance [`os.sendfile()`](https://docs.python.org/3.14/library/os.html#os.sendfile).

*file* must be a regular file object opened in binary mode.

*offset* indicates the point from which file reading begins. When supplied, *count* is the overall byte count to send, rather than transmitting the file all the way to EOF. The file position always advances, even if this method raises an error, and [`file.tell()`](https://docs.python.org/3.14/library/io.html#io.IOBase.tell) serves to retrieve the true count of bytes sent.

Giving *fallback* the value `True` lets asyncio read and send the file by hand wherever the platform offers no sendfile system call (for instance Windows, or an SSL socket on Unix).

Raise [`SendfileNotAvailableError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.SendfileNotAvailableError) where the *sendfile* syscall is unsupported by the system and *fallback* holds `False`.

Added in version 3.7.

[Subject index](INDEX.md) · [Previous](loop-create-unix-server-to-loop-connect-accepted-socket.md) · [Continue](loop-start-tls.md)
