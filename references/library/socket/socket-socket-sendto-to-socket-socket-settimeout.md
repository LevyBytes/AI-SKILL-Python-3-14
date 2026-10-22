# socket.socket: `sendto()`, `sendmsg()`, `sendmsg_afalg()`, `sendfile()`, `set_inheritable()`, `setblocking()`, `sock.setblocking()`, `settimeout()`

sendto(*bytes*, *flags*, *address*)

Push data out through the socket. The socket ought not be connected to any remote socket here, given that *address* is what names the destination socket. The optional *flags* argument carries the same sense it does for `recv()`. The count of bytes sent comes back. Which form *address* takes hinges on the address family — see Socket families.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `socket.sendto` with arguments `self`, `address`.

Changed in version 3.5: Should the system call be interrupted while the signal handler raises no exception, nowadays the method retries that system call rather than throwing an [`InterruptedError`](https://docs.python.org/3.14/library/exceptions.html#InterruptedError) exception (consult [**PEP 475**](https://peps.python.org/pep-0475/) for the reasoning).

 sendmsg(*buffers*[, *ancdata*[, *flags*[, *address*]]])

Push both normal and ancillary data through the socket, pulling the non-ancillary portion together from a run of buffers and joining it into one message. The *buffers* argument hands over the non-ancillary data as an iterable of [bytes-like objects](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) (such as [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) objects); the operating system can impose a cap ([`sysconf()`](https://docs.python.org/3.14/library/os.html#os.sysconf) value `SC_IOV_MAX`) on how many buffers may be in play. The *ancdata* argument hands over the ancillary data (control messages) as an iterable holding zero or more tuples `(cmsg_level, cmsg_type, cmsg_data)`, in which *cmsg_level* and *cmsg_type* are integers naming the protocol level and the protocol-specific type respectively, while *cmsg_data* is a bytes-like object carrying the associated data. Be aware that certain systems (notably those lacking `CMSG_SPACE()`) may permit only a single control message per call. The *flags* argument defaults to 0 and matches the sense it has for `send()`. Where *address* is given and not `None`, it fixes a destination address for the message. What gets returned is the count of non-ancillary data bytes sent.

The function below pushes the list of file descriptors *fds* across an `AF_UNIX` socket, on those systems that back the `SCM_RIGHTS` mechanism. See also `recvmsg()`.

```python
import socket, array

def send_fds(sock, msg, fds):
    return sock.sendmsg([msg], [(socket.SOL_SOCKET, socket.SCM_RIGHTS, array.array("i", fds))])

```

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

Most Unix platforms.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `socket.sendmsg` with arguments `self`, `address`.

Added in version 3.3.

Changed in version 3.5: When the system call gets interrupted yet the signal handler raises no exception, the method now repeats that system call instead of surfacing an [`InterruptedError`](https://docs.python.org/3.14/library/exceptions.html#InterruptedError) exception (refer to [**PEP 475**](https://peps.python.org/pep-0475/) for the reasoning behind this).

 sendmsg_afalg([*msg*, ]***, *op*[, *iv*[, *assoclen*[, *flags*]]])

A `sendmsg()` variant tailored to an `AF_ALG` socket. It sets the mode, IV, AEAD associated data length, and flags for that `AF_ALG` socket.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.38.

Added in version 3.6.

 sendfile(*file*, *offset=0*, *count=None*)

Transmit a file right up to EOF by leaning on the high-performance [`os.sendfile`](https://docs.python.org/3.14/library/os.html#os.sendfile), handing back the grand total of bytes that went out. *file* has to be a regular file object opened in binary mode. Where `os.sendfile` is unavailable (Windows, for example) or *file* isn't a regular file, `send()` steps in instead. *offset* says where in the file reading should begin. When given, *count* is the total byte count to push out, rather than transmitting the file all the way to EOF. The file position gets refreshed on return — and likewise after an error, in which case [`file.tell()`](https://docs.python.org/3.14/library/io.html#io.IOBase.tell) helps you work out how many bytes went out. The socket has to be of `SOCK_STREAM` type. Non-blocking sockets aren't supported.

Added in version 3.5.

 set_inheritable(*inheritable*)

Set the [inheritable flag](https://docs.python.org/3.14/library/os.html#fd-inheritance) of the socket’s file descriptor or socket’s handle.

Added in version 3.4.

 setblocking(*flag*)

Switch the socket between blocking and non-blocking mode: a false *flag* puts the socket into non-blocking mode, otherwise into blocking mode.

Think of this method as shorthand for particular `settimeout()` calls:

- `sock.setblocking(True)` is equivalent to `sock.settimeout(None)`

- `sock.setblocking(False)` is equivalent to `sock.settimeout(0.0)`

Changed in version 3.7: The method no longer applies `SOCK_NONBLOCK` flag on `socket.type`.

 settimeout(*value*)

Put a timeout on blocking socket operations. For *value* you may pass a nonnegative real number of seconds, or `None`. With a non-zero value, any later socket operation raises a `timeout` exception once the timeout span *value* runs out before that operation finishes. Pass zero and the socket goes into non-blocking mode; pass `None` and the socket goes into blocking mode.

For more detail, please look over the notes on socket timeouts.

Changed in version 3.7: The method no longer toggles `SOCK_NONBLOCK` flag on `socket.type`.

[Subject index](INDEX.md) · [Continue](socket-socket-setsockopt-to-socket-socket-share.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md) · [Owning module, declaration or section: socket.socket](socket-socket-class.md) · [Owning module, declaration or section: Socket Objects](socket-socket-class.md) · [Owning module, declaration or section: sendto](socket-socket-sendall-to-socket-socket-sendto.md)
