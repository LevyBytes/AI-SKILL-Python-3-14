# ssl - Notes on non-blocking sockets

### Notes on non-blocking sockets

In non-blocking mode, SSL sockets act a bit differently from ordinary sockets. Consequently, when you deal with non-blocking sockets, there are a number of points you must keep in mind:

- Should an I/O operation be about to block, the majority of `SSLSocket` methods will raise either `SSLWantWriteError` or `SSLWantReadError` rather than [`BlockingIOError`](https://docs.python.org/3.14/library/exceptions.html#BlockingIOError). A `SSLWantReadError` gets raised whenever a read on the underlying socket is required, and a `SSLWantWriteError` whenever a write on the underlying socket is required. Be aware that *writing* to an SSL socket can demand *reading* from the underlying socket beforehand, and that *reading* from the SSL socket can demand a preceding *write* to the underlying socket.

Changed in version 3.5: In prior Python releases, the `SSLSocket.send()` method gave back zero rather than raising `SSLWantWriteError` or `SSLWantReadError`.

- Invoking [`select()`](https://docs.python.org/3.14/library/select.html#select.select) reports that the OS-level socket is readable (or writable), yet that does not guarantee enough data exists at the higher SSL layer. As an example, perhaps only a portion of an SSL frame has shown up. For that reason you have to be prepared for `SSLSocket.recv()` and `SSLSocket.send()` to fail, and to try again following a further call to `select()`.

- On the other hand, because the SSL layer maintains its own framing, an SSL socket might still hold readable data even though [`select()`](https://docs.python.org/3.14/library/select.html#select.select) is unaware of it. So you ought to first invoke `SSLSocket.recv()` to clear out any data that may be waiting, and only afterward block on a `select()` call should that still be required.

(naturally, comparable considerations hold when you use other primitives like [`poll()`](https://docs.python.org/3.14/library/select.html#select.poll), or the ones in the [`selectors`](https://docs.python.org/3.14/library/selectors.html#module-selectors) module)

- The SSL handshake will itself run in non-blocking fashion: you have to keep retrying the `SSLSocket.do_handshake()` method until it comes back successfully. The following outline employs [`select()`](https://docs.python.org/3.14/library/select.html#select.select) to await the socket becoming ready:

```python
while True:
    try:
        sock.do_handshake()
        break
    except ssl.SSLWantReadError:
        select.select([sock], [], [])
    except ssl.SSLWantWriteError:
        select.select([], [sock], [])

```

See also

The [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) module accommodates non-blocking SSL sockets and offers a higher level [Streams API](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio-streams). For event polling it relies on the [`selectors`](https://docs.python.org/3.14/library/selectors.html#module-selectors) module and copes with `SSLWantWriteError`, `SSLWantReadError`, and [`BlockingIOError`](https://docs.python.org/3.14/library/exceptions.html#BlockingIOError) exceptions. The SSL handshake is likewise carried out asynchronously.

[Subject index](INDEX.md) · [Previous](server-side-operation.md) · [Continue](ssl-sslobject-class.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md)
