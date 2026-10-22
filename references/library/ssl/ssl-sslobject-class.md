# ssl: `ssl.SSLObject`

### Memory BIO support

Added in version 3.5.

From the moment the SSL module landed in Python 2.6, the `SSLSocket` class has delivered two connected yet separate kinds of functionality:

- SSL protocol handling

- Network IO

The network IO API matches the one furnished by [`socket.socket`](https://docs.python.org/3.14/library/socket.html#socket.socket), which `SSLSocket` additionally inherits from. Thanks to this, an SSL socket can stand in directly for an ordinary socket, which makes bolting SSL onto an existing application quite straightforward.

Pairing SSL protocol handling with network IO generally functions fine, although there are certain situations where it falls short. Take async IO frameworks that wish to adopt an IO multiplexing model other than the "select/poll on a file descriptor" (readiness based) model presumed by [`socket.socket`](https://docs.python.org/3.14/library/socket.html#socket.socket) and by OpenSSL's internal socket IO routines. This chiefly matters on platforms such as Windows where that model performs poorly. To address it, a narrower variant of `SSLSocket` named `SSLObject` is supplied.

 *class *ssl.SSLObject

A narrower variant of `SSLSocket` that represents an SSL protocol instance while carrying none of the network IO methods. Framework authors aiming to build asynchronous IO for SSL by means of memory buffers commonly rely on this class.

The class layers an interface over a low-level SSL object as supplied by OpenSSL. That object holds the state of an SSL connection yet supplies no network IO of its own. IO has to happen by way of separate "BIO" objects, which constitute OpenSSL's IO abstraction layer.

This class exposes no public constructor. You have to build an `SSLObject` instance through the `wrap_bio()` method. That method creates the `SSLObject` instance and ties it to a pair of BIOs. The *incoming* BIO carries data from Python into the SSL protocol instance, whereas the *outgoing* BIO carries data in the reverse direction.

These are the methods on offer:

- `context`

- `server_side`

- `server_hostname`

- `session`

- `session_reused`

-

[Subject index](INDEX.md) · [Previous](notes-on-non-blocking-sockets.md) · [Continue](ssl-sslobject-read-to-ssl-sslobject-get-channel-binding.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md)
