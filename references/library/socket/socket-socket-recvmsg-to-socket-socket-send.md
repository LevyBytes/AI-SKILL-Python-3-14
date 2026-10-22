# socket.socket: `recvmsg()`, `recvmsg_into()`, `recvfrom_into()`, `recv_into()`, `send()`

recvmsg(*bufsize*[, *ancbufsize*[, *flags*]])

Read ordinary data (up to *bufsize* bytes) together with ancillary data off the socket. The *ancbufsize* argument fixes, in bytes, the size of the internal buffer used to take in the ancillary data; its default of 0 means no ancillary data is received. You can compute suitable buffer sizes for ancillary data with `CMSG_SPACE()` or `CMSG_LEN()`, and any items that overflow the buffer may be truncated or dropped. The *flags* argument defaults to 0 and carries the same meaning it has for `recv()`.

A 4-tuple comes back: `(data, ancdata, msg_flags, address)`. Within it, *data* is a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object that holds the non-ancillary data received. The *ancdata* entry is a list of zero or more `(cmsg_level, cmsg_type, cmsg_data)` tuples standing for the ancillary data (control messages) received: *cmsg_level* and *cmsg_type* are integers giving the protocol level and the protocol-specific type respectively, while *cmsg_data* is a `bytes` object carrying the associated data. The *msg_flags* item is the bitwise OR of assorted flags signaling conditions on the message received; see your system documentation for the particulars. When the receiving socket is unconnected, *address* holds the address of the sending socket if that is available; otherwise its value is unspecified.

On certain systems, `sendmsg()` and `recvmsg()` let you hand file descriptors between processes across an `AF_UNIX` socket. Where this facility is in play (frequently confined to `SOCK_STREAM` sockets), `recvmsg()` delivers, within its ancillary data, items shaped like `(socket.SOL_SOCKET, socket.SCM_RIGHTS, fds)`, in which *fds* is a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object that encodes the fresh file descriptors as a binary array whose elements are the platform's native C int type. Should `recvmsg()` throw an exception once the system call has returned, it first tries to close whatever file descriptors arrived through this mechanism.

Certain systems give no sign of the truncated length for ancillary data items received only in part. When an item looks as though it runs past the buffer's end, `recvmsg()` raises a [`RuntimeWarning`](https://docs.python.org/3.14/library/exceptions.html#RuntimeWarning) and returns whatever portion of it lies within the buffer, so long as it has not been truncated ahead of the start of its associated data.

On systems offering the `SCM_RIGHTS` mechanism, the function below reads up to *maxfds* file descriptors and returns both the message data and a list holding the descriptors (while skipping past unexpected situations such as receiving unrelated control messages). See also `sendmsg()`.

```python
import socket, array

def recv_fds(sock, msglen, maxfds):
    fds = array.array("i")   # Array of ints
    msg, ancdata, flags, addr = sock.recvmsg(msglen, socket.CMSG_LEN(maxfds * fds.itemsize))
    for cmsg_level, cmsg_type, cmsg_data in ancdata:
        if cmsg_level == socket.SOL_SOCKET and cmsg_type == socket.SCM_RIGHTS:
            # Append data, ignoring any truncated integers at the end.
            fds.frombytes(cmsg_data[:len(cmsg_data) - (len(cmsg_data) % fds.itemsize)])
    return msg, list(fds)

```

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Most Unix platforms.

Added in version 3.3.

Changed in version 3.5: Should the system call be interrupted while the signal handler raises nothing, the method retries that system call rather than throwing an [`InterruptedError`](https://docs.python.org/3.14/library/exceptions.html#InterruptedError) exception (consult [**PEP 475**](https://peps.python.org/pep-0475/) for the reasoning).

 recvmsg_into(*buffers*[, *ancbufsize*[, *flags*]])

Read ordinary data and ancillary data off the socket exactly as `recvmsg()` does, but spread the non-ancillary data across a series of buffers rather than handing back a fresh bytes object. The *buffers* argument has to be an iterable of objects exposing writable buffers (for example [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) objects); each gets filled with consecutive pieces of the non-ancillary data until it is all written or no buffers remain. The operating system may impose a cap ([`sysconf()`](https://docs.python.org/3.14/library/os.html#os.sysconf) value `SC_IOV_MAX`) on how many buffers may be used. The *ancbufsize* and *flags* arguments carry the same meaning they have for `recvmsg()`.

A 4-tuple is returned: `(nbytes, ancdata, msg_flags, address)`, where *nbytes* is the total count of non-ancillary data bytes written into the buffers, while *ancdata*, *msg_flags* and *address* match those from `recvmsg()`.

Example:

```python
>>> import socket
>>> s1, s2 = socket.socketpair()
>>> b1 = bytearray(b'----')
>>> b2 = bytearray(b'0123456789')
>>> b3 = bytearray(b'--------------')
>>> s1.send(b'Mary had a little lamb')
22
>>> s2.recvmsg_into([b1, memoryview(b2)[2:9], b3])
(22, [], 0, None)
>>> [b1, b2, b3]
[bytearray(b'Mary'), bytearray(b'01 had a 9'), bytearray(b'little lamb---')]

```

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Most Unix platforms.

Added in version 3.3.

 recvfrom_into(*buffer*[, *nbytes*[, *flags*]])

Read data off the socket, depositing it into *buffer* instead of building a fresh bytestring. What comes back is a pair `(nbytes, address)`, where *nbytes* is the count of bytes received and *address* is the address of the socket that sent the data. For the sense of the optional *flags* argument, consult the Unix manual page *[recv(2)](https://manpages.debian.org/recv(2))*; it defaults to zero. Which form *address* takes is determined by the address family — see Socket families.

 recv_into(*buffer*[, *nbytes*[, *flags*]])

Read at most *nbytes* bytes off the socket, placing the data into a buffer rather than building a fresh bytestring. When *nbytes* is left out (or 0), read up to as much room as the supplied buffer offers. Returns the count of bytes received. For the sense of the optional *flags* argument, consult the Unix manual page *[recv(2)](https://manpages.debian.org/recv(2))*; it defaults to zero.

 send(*bytes*[, *flags*])

Push data onto the socket. The socket has to be connected to a remote socket. The optional *flags* argument carries the same meaning it has for `recv()`. Returns the count of bytes sent. It falls to applications to confirm that everything has gone out; when only a portion of the data was transmitted, the application must take it upon itself to deliver what remains. For more on this subject, consult the [Socket Programming HOWTO](https://docs.python.org/3.14/howto/sockets.html#socket-howto).

Changed in version 3.5: Should the system call be interrupted while the signal handler raises nothing, the method retries that system call rather than throwing an [`InterruptedError`](https://docs.python.org/3.14/library/exceptions.html#InterruptedError) exception (consult [**PEP 475**](https://peps.python.org/pep-0475/) for the reasoning).

[Subject index](INDEX.md) · [Previous](socket-socket-getsockname-to-socket-socket-recvfrom.md) · [Continue](socket-socket-sendall-to-socket-socket-sendto.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md) · [Owning module, declaration or section: socket.socket](socket-socket-class.md) · [Owning module, declaration or section: Socket Objects](socket-socket-class.md)
