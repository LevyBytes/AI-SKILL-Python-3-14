# ssl: `ssl.cert_time_to_seconds()`, `ssl.get_server_certificate()`, `ssl.DER_cert_to_PEM_cert()`, `ssl.PEM_cert_to_DER_cert()`, `ssl.get_default_verify_paths()`

### Certificate handling

 ssl.cert_time_to_seconds(*cert_time*)

Hand back the seconds elapsed since the epoch for the supplied `cert_time` string, which holds a certificate's “notBefore” or “notAfter” date written in `"%b %d %H:%M:%S %Y %Z"` strptime format (C locale).

For illustration:

```pycon
>>> import ssl
>>> import datetime as dt
>>> timestamp = ssl.cert_time_to_seconds("Jan  5 09:34:43 2018 GMT")
>>> timestamp
1515144883
>>> print(dt.datetime.fromtimestamp(timestamp, dt.UTC))
2018-01-05 09:34:43+00:00

```

Per [**RFC 5280**](https://datatracker.ietf.org/doc/html/rfc5280.html), the “notBefore” and “notAfter” dates have to be expressed in GMT.

Changed in version 3.5: Read the supplied time as UTC, following the ‘GMT’ timezone marker in the input string; earlier releases assumed the local timezone instead. Hand back an integer (the input format holds no sub-second fractions).

 ssl.get_server_certificate(*addr*, *ssl_version=PROTOCOL_TLS_CLIENT*, *ca_certs=None*[, *timeout*])

For a server that speaks SSL at address `addr`, given as a (*hostname*, *port-number*) pair, retrieve that server's certificate and hand it back as a PEM-encoded string. Supplying `ssl_version` tells it which version of the SSL protocol to use when reaching the server. Supplying *ca_certs* — a file holding a list of root certificates in the very format the *cafile* parameter of `SSLContext.load_verify_locations()` expects — causes the call to check the server certificate against that collection of root certificates, failing if that check does not pass. The `timeout` parameter lets you set a timeout.

Changed in version 3.3: IPv6 support was added to this function.

Changed in version 3.5: To stay maximally compatible with present-day servers, the default *ssl_version* moved from `PROTOCOL_SSLv3` over to `PROTOCOL_TLS`.

Changed in version 3.10: A *timeout* parameter became available.

 ssl.DER_cert_to_PEM_cert(*der_cert_bytes*)

Take a certificate supplied as a DER-encoded blob of bytes and hand back a PEM-encoded string form of that same certificate.

 ssl.PEM_cert_to_DER_cert(*pem_cert_string*)

Take a certificate supplied as an ASCII PEM string and hand back a DER-encoded byte sequence for that same certificate.

 ssl.get_default_verify_paths()

Hand back a named tuple holding paths to OpenSSL's default cafile and capath. These match the paths that `SSLContext.set_default_verify_paths()` relies on. What comes back is a [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple) `DefaultVerifyPaths`:

- `cafile` - resolved path to cafile or `None` if the file doesn’t exist,

- `capath` - resolved path to capath or `None` if the directory doesn’t exist,

- `openssl_cafile_env` - OpenSSL’s environment key that points to a cafile,

- `openssl_cafile` - hard coded path to a cafile,

- `openssl_capath_env` - OpenSSL’s environment key that points to a capath,

- `openssl_capath` - hard coded path to a capath directory

Added in version 3.4.

[Subject index](INDEX.md) · [Previous](ssl-rand-bytes-to-ssl-rand-add.md) · [Continue](ssl-enum-certificates-to-ssl-enum-crls.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md)
