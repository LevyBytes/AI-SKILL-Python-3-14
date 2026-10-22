# ssl — Exceptions

### Exceptions

 *exception *ssl.SSLError

Thrown to flag a failure coming from the underlying SSL implementation (today that is the OpenSSL library). It points to trouble in the encryption-and-authentication layer that rides above the underlying network connection. The exception is a subtype of [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError). For each `SSLError` instance, the OpenSSL library supplies the message and the error code.

Changed in version 3.3: Previously `SSLError` had been a subtype of [`socket.error`](https://docs.python.org/3.14/library/socket.html#socket.error).

 library

A short string identifying which OpenSSL submodule produced the error — for instance `SSL`, `PEM` or `X509`. Which values can appear is tied to the OpenSSL version.

Added in version 3.3.

 reason

A short string identifying why the error came up, say `CERTIFICATE_VERIFY_FAILED`. Which values can appear is tied to the OpenSSL version.

Added in version 3.3.

 *exception *ssl.SSLZeroReturnError

A subclass of `SSLError` thrown when a read or write is attempted after the SSL connection has already been shut down cleanly. Be aware this says nothing about whether the underlying transport (that is, TCP) has closed.

Added in version 3.3.

 *exception *ssl.SSLWantReadError

A subclass of `SSLError` thrown by a non-blocking SSL socket when a read or write is attempted but additional data must first arrive over the underlying TCP transport before the request can complete.

Added in version 3.3.

 *exception *ssl.SSLWantWriteError

A subclass of `SSLError` thrown by a non-blocking SSL socket when a read or write is attempted but additional data must first be transmitted over the underlying TCP transport before the request can complete.

Added in version 3.3.

 *exception *ssl.SSLSyscallError

A subclass of `SSLError` thrown when a system error crops up during an operation on a SSL socket. Regrettably, the underlying errno number cannot easily be examined.

Added in version 3.3.

 *exception *ssl.SSLEOFError

A subclass of `SSLError` thrown once the SSL connection has ended abruptly. As a rule, don't attempt to keep using the underlying transport after hitting this error.

Added in version 3.3.

 *exception *ssl.SSLCertVerificationError

A subclass of `SSLError` thrown once certificate validation comes back as failed.

Added in version 3.7.

 verify_code

A numeric error number that denotes the verification error.

 verify_message

A human readable string of the verification error.

 *exception *ssl.CertificateError

An alias for `SSLCertVerificationError`.

Changed in version 3.7: The exception is now an alias for `SSLCertVerificationError`.

[Subject index](INDEX.md) · [Previous](ssl-create-default-context.md) · [Continue](ssl-rand-bytes-to-ssl-rand-add.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md)
