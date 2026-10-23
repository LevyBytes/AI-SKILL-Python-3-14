# What’s New in Python 2.6 / Improved SSL Support - socket, ssl

### Improved SSL Support

Bill Janssen overhauled Python 2.6's handling of the Secure Sockets Layer in a big way by contributing a fresh module, [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl), layered over the [OpenSSL](https://www.openssl.org/) library. This module hands you finer control of the protocol that gets negotiated and the X.509 certificates in play, and it makes writing SSL servers in Python (rather than just clients) much easier. The older SSL functionality in the [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) module remains in place and keeps working, though Python 3.0 will drop it.

To put the new module to work, open a TCP connection in the customary fashion first, then feed it to the `ssl.wrap_socket()` function. You can dictate whether a certificate is mandatory and fetch certificate details through the `getpeercert()` method.

See also

The documentation for the [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) module.

[Subject index](INDEX.md) · [Previous source section](ctypes-enhancements.md) · [Next source section](deprecations-and-removals.md) · [Release/subject declaration](python-3-0.md)
