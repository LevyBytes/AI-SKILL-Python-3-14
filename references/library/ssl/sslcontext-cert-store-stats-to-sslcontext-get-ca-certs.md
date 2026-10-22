# ssl: `SSLContext.cert_store_stats()`, `SSLContext.load_cert_chain()`, `SSLContext.load_default_certs()`, `SSLContext.load_verify_locations()`, `SSLContext.get_ca_certs()`

Changed in version 3.6: Secure default values now back a newly created context. By default the following options are enabled: `OP_NO_COMPRESSION`, `OP_CIPHER_SERVER_PREFERENCE`, `OP_SINGLE_DH_USE`, `OP_SINGLE_ECDH_USE`, `OP_NO_SSLv2`, and `OP_NO_SSLv3` (the lone exception being `PROTOCOL_SSLv3`). At startup the cipher suite list holds `HIGH` ciphers exclusively, omitting `NULL` ciphers as well as `MD5` ciphers.

Deprecated since version 3.10: Constructing `SSLContext` with no protocol argument is deprecated. Going forward the context class is expected to mandate either the `PROTOCOL_TLS_CLIENT` or the `PROTOCOL_TLS_SERVER` protocol.

Changed in version 3.10: The default cipher suites have been narrowed to secure AES and ChaCha20 ciphers that provide forward secrecy at security level 2. Disallowed now are RSA and DH keys below 2048 bits and ECC keys below 224 bits. A minimum TLS version of TLS 1.2 applies to `PROTOCOL_TLS`, `PROTOCOL_TLS_CLIENT`, and `PROTOCOL_TLS_SERVER`.

Note

Once a connection has made use of an `SSLContext`, only limited changes to it are supported. Loading additional certificates into the internal trust store remains permitted, but altering ciphers, verification settings, or mTLS certificates can produce unexpected results.

Note

Because `SSLContext` is meant to be shared across many connections, it stays thread-safe provided you don't reconfigure it once a connection has begun using it.

`SSLContext` objects have the following methods and attributes:

 SSLContext.cert_store_stats()

Return, as a dictionary, statistics covering how many X.509 certificates are loaded, how many of those X.509 certificates carry the CA flag, and how many certificate revocation lists are present.

Example for a context with one CA cert and one other cert:

```python
>>> context.cert_store_stats()
{'crl': 0, 'x509_ca': 1, 'x509': 2}

```

Added in version 3.4.

 SSLContext.load_cert_chain(*certfile*, *keyfile=None*, *password=None*)

Load a private key together with its matching certificate. The *certfile* string has to be the path of one PEM-format file holding the certificate plus however many CA certificates are required to confirm the certificate's authenticity. If supplied, the *keyfile* string must reference a file holding the private key; otherwise the private key is read out of *certfile* as well. Refer to the discussion of Certificates to learn more about how the certificate sits inside the *certfile*.

You may pass the *password* argument as a function that supplies the password used to decrypt the private key. Such a function runs only when the private key is encrypted and a password is required. It receives no arguments and is expected to hand back a string, bytes, or bytearray. A returned string gets encoded as UTF-8 before it is applied to decrypt the key. As an alternative, you can give a string, bytes, or bytearray straight through as the *password* argument. When the private key isn't encrypted and no password is necessary, the value is disregarded.

When the *password* argument is omitted yet a password is needed, OpenSSL falls back to its own built-in password prompting, which interactively asks the user for a password.

If the private key fails to correspond to the certificate, an `SSLError` is raised.

Changed in version 3.3: New optional argument *password*.

 SSLContext.load_default_certs(*purpose=Purpose.SERVER_AUTH*)

Pull in a collection of default "certification authority" (CA) certificates from standard locations. Under Windows the CA certs are read from the `CA` and `ROOT` system stores. Across every platform it invokes `SSLContext.set_default_verify_paths()`. The method may, at some later point, also gather CA certificates from additional places.

Which kind of CA certificates get loaded is governed by the *purpose* flag. The default value `Purpose.SERVER_AUTH` brings in certificates flagged and trusted for TLS web server authentication (client side sockets), whereas `Purpose.CLIENT_AUTH` brings in CA certificates used for verifying client certificates on the server side.

Added in version 3.4.

 SSLContext.load_verify_locations(*cafile=None*, *capath=None*, *cadata=None*)

Bring in a collection of "certification authority" (CA) certificates that serve to validate the certificates of other peers whenever `verify_mode` differs from `CERT_NONE`. You must supply at least one of *cafile* or *capath*.

This method is also able to load certification revocation lists (CRLs) in either PEM or DER format. To put CRLs to work, you have to set up `SSLContext.verify_flags` correctly.

If given, the *cafile* string names the path of a file holding concatenated CA certificates in PEM format. Consult the discussion of Certificates to see how the certificates ought to be laid out within that file.

If given, the *capath* string names the path of a directory that holds several PEM-format CA certificates arranged according to an [OpenSSL specific layout](https://docs.openssl.org/master/man3/SSL_CTX_load_verify_locations/).

If given, the *cadata* object is one of two things: an ASCII string carrying one or more PEM-encoded certificates, or else a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) holding DER-encoded certificates. As with *capath*, surplus lines surrounding PEM-encoded certificates are skipped, though at least one certificate has to be there.

Changed in version 3.4: New optional argument *cadata*

 SSLContext.get_ca_certs(*binary_form=False*)

Return a list of the "certification authority" (CA) certificates that have been loaded. When the `binary_form` parameter is [`False`](https://docs.python.org/3.14/library/constants.html#False), every list entry is a dict shaped like the result of `SSLSocket.getpeercert()`. Otherwise the method hands back a list of DER-encoded certificates. Certificates from *capath* are left out of the returned list unless some certificate was both requested and loaded during an SSL connection.

Note

A capath directory's certificates stay unloaded until they have been needed at least one time.

Added in version 3.4.

[Subject index](INDEX.md) · [Continue](sslcontext-get-ciphers-to-sslcontext-set-npn-protocols.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md) · [Owning module, declaration or section: ssl.SSLContext](ssl-sslcontext-class.md) · [Owning module, declaration or section: SSL contexts](ssl-sslcontext-class.md) · [Preceding source contract and version conditions](ssl-sslcontext-class.md)
