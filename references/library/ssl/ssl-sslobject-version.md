# ssl.SSLObject: `version()`

`version()`

Set against `SSLSocket`, this object is missing the following capabilities:

- Any kind of network IO; `recv()` and `send()` read from and write to nothing but the underlying `MemoryBIO` buffers.

- The *do_handshake_on_connect* machinery is absent. You must invoke `do_handshake()` by hand every time to begin the handshake.

- There is no treatment of *suppress_ragged_eofs*. Every end-of-file condition that breaches the protocol is signaled through the `SSLEOFError` exception.

- Calling the `unwrap()` method returns nothing, in contrast to an SSL socket, where the call hands back the underlying socket.

- The *server_name_callback* callback handed to `SSLContext.set_servername_callback()` receives an `SSLObject` instance as its first parameter in place of an `SSLSocket` instance.

A handful of remarks concerning the use of `SSLObject`:

- Every IO on an `SSLObject` is non-blocking. As a result, `read()` for instance will raise an `SSLWantReadError` whenever it requires more data than the incoming BIO currently holds.

Changed in version 3.7: You must build `SSLObject` instances via `wrap_bio()`. Earlier releases permitted creating instances directly. That path was never documented nor officially supported.

An SSLObject exchanges data with the outside world through memory buffers. The `MemoryBIO` class supplies a memory buffer suited to this role. It wraps an OpenSSL memory BIO (Basic IO) object:

[Subject index](INDEX.md) · [Previous](ssl-sslobject-read-to-ssl-sslobject-get-channel-binding.md) · [Continue](ssl-memorybio-class-to-ssl-memorybio-write-eof.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md) · [Owning module, declaration or section: ssl.SSLObject](ssl-sslobject-class.md) · [Owning module, declaration or section: Memory BIO support](ssl-sslobject-class.md)
