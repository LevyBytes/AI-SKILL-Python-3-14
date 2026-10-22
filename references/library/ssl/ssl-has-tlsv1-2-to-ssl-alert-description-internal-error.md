# ssl: TLS feature detection, OpenSSL versions and alert constants

ssl.HAS_TLSv1_2

Indicates whether the OpenSSL library ships with native support for the TLS 1.2 protocol.

Added in version 3.7.

 ssl.HAS_TLSv1_3

Indicates whether the OpenSSL library ships with native support for the TLS 1.3 protocol.

Added in version 3.7.

 ssl.HAS_PSK

Indicates whether the OpenSSL library ships with native support for TLS-PSK.

Added in version 3.13.

 ssl.HAS_PHA

Indicates whether the OpenSSL library ships with native support for TLS-PHA.

Added in version 3.14.

 ssl.CHANNEL_BINDING_TYPES

List of the TLS channel binding types that are supported. The strings in this list may be passed as arguments to `SSLSocket.get_channel_binding()`.

Added in version 3.3.

 ssl.OPENSSL_VERSION

The OpenSSL library's version string as loaded by the interpreter:

```python
>>> ssl.OPENSSL_VERSION
'OpenSSL 1.0.2k  26 Jan 2017'

```

Added in version 3.2.

 ssl.OPENSSL_VERSION_INFO

A five-integer tuple that conveys version details about the OpenSSL library:

```python
>>> ssl.OPENSSL_VERSION_INFO
(1, 0, 2, 11, 15)

```

Added in version 3.2.

 ssl.OPENSSL_VERSION_NUMBER

The OpenSSL library's raw version number, expressed as one integer:

```python
>>> ssl.OPENSSL_VERSION_NUMBER
268443839
>>> hex(ssl.OPENSSL_VERSION_NUMBER)
'0x100020bf'

```

Added in version 3.2.

 ssl.ALERT_DESCRIPTION_HANDSHAKE_FAILURE

 ssl.ALERT_DESCRIPTION_INTERNAL_ERROR

 ALERT_DESCRIPTION_*

Alert Descriptions taken from [**RFC 5246**](https://datatracker.ietf.org/doc/html/rfc5246.html) and elsewhere. The [IANA TLS Alert Registry](https://www.iana.org/assignments/tls-parameters/tls-parameters.xml#tls-parameters-6) holds this list along with references to the RFCs that define what they mean.

Used as the value returned by the callback function in `SSLContext.set_servername_callback()`.

Added in version 3.4.

[Subject index](INDEX.md) · [Previous](ssl-op-no-ticket-to-ssl-has-tlsv1-1.md) · [Continue](ssl-alertdescription-class-to-purpose-client-auth.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md) · [Owning module, declaration or section: Constants](ssl-cert-none-to-ssl-cert-required.md)
