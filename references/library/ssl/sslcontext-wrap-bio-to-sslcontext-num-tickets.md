# ssl: BIO wrapping, hostname checks and TLS version limits

SSLContext.wrap_bio(*incoming*, *outgoing*, *server_side=False*, *server_hostname=None*, *session=None*)

Take the BIO objects *incoming* and *outgoing*, wrap them, and return an instance of `SSLContext.sslobject_class` (default `SSLObject`). The SSL routines pull input data from the incoming BIO and push data into the outgoing BIO.

The *server_side*, *server_hostname* and *session* parameters carry the same meaning here as they do in `SSLContext.wrap_socket()`.

Changed in version 3.6: *session* argument was added.

Changed in version 3.7: Rather than a hard-coded `SSLObject`, the method now hands back an instance of `SSLContext.sslobject_class`.

 SSLContext.sslobject_class

The type returned by `SSLContext.wrap_bio()`, which defaults to `SSLObject`. You can override this attribute on an instance of the class to make it return a custom subclass of `SSLObject`.

Added in version 3.7.

 SSLContext.session_stats()

Return statistics describing the SSL sessions this context has created or managed. The result is a dictionary mapping the name of each [piece of information](https://docs.openssl.org/1.1.1/man3/SSL_CTX_sess_number/) to its numeric value. For instance, here is the running total of hits and misses in the session cache counted since the context came into being:

```python
>>> stats = context.session_stats()
>>> stats['hits'], stats['misses']
(0, 0)

```

 SSLContext.check_hostname

Whether the peer cert's hostname gets matched in `SSLSocket.do_handshake()`. For the hostname to be matched, the context's `verify_mode` has to be set to `CERT_OPTIONAL` or `CERT_REQUIRED`, and you have to hand *server_hostname* to `wrap_socket()`. Turning on hostname checking automatically moves `verify_mode` from `CERT_NONE` up to `CERT_REQUIRED`. While hostname checking stays on, it can't be moved back to `CERT_NONE`. By default the `PROTOCOL_TLS_CLIENT` protocol switches hostname checking on. Under other protocols you have to switch hostname checking on yourself.

Example:

```python
import socket, ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
context.load_default_certs()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = context.wrap_socket(s, server_hostname='www.verisign.com')
ssl_sock.connect(('www.verisign.com', 443))

```

Added in version 3.4.

Changed in version 3.7: Whenever hostname checking gets turned on while `verify_mode` sits at `CERT_NONE`, `verify_mode` now switches over to `CERT_REQUIRED` on its own. In earlier releases that very action raised a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) instead.

 SSLContext.keylog_filename

Each time key material is produced or received, write the TLS keys into a keylog file. This keylog file exists strictly for debugging. NSS specifies the file format, which many traffic analyzers — Wireshark among them — make use of. The log file is opened in append-only mode. Writes are synchronized across threads, but not across processes.

Added in version 3.8.

 SSLContext.maximum_version

A `TLSVersion` enum member standing for the highest TLS version that is supported. Its value defaults to `TLSVersion.MAXIMUM_SUPPORTED`. For protocols other than `PROTOCOL_TLS`, `PROTOCOL_TLS_CLIENT`, and `PROTOCOL_TLS_SERVER`, the attribute is read-only.

The `maximum_version`, `minimum_version` and `SSLContext.options` attributes together shape which SSL and TLS versions the context supports. Invalid combinations are not guarded against by the implementation. For instance, a context that has `OP_NO_TLSv1_2` set in `options` while `maximum_version` is `TLSVersion.TLSv1_2` will be unable to set up a TLS 1.2 connection.

Added in version 3.7.

 SSLContext.minimum_version

The same as `SSLContext.maximum_version`, except that it represents the lowest supported version or `TLSVersion.MINIMUM_SUPPORTED`.

Added in version 3.7.

 SSLContext.num_tickets

Govern how many TLS 1.3 session tickets a `PROTOCOL_TLS_SERVER` context issues. This setting has no bearing on TLS 1.0 through 1.2 connections.

Added in version 3.8.

[Subject index](INDEX.md) · [Previous](sslcontext-sni-callback-to-sslcontext-sslsocket-class.md) · [Continue](sslcontext-options-to-sslcontext-verify-mode.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md) · [Owning module, declaration or section: ssl.SSLContext](ssl-sslcontext-class.md) · [Owning module, declaration or section: SSL contexts](ssl-sslcontext-class.md)
