# ssl: `ssl.TLSVersion`, `TLSVersion.MINIMUM_SUPPORTED`, `TLSVersion.MAXIMUM_SUPPORTED`, `TLSVersion.SSLv3`, `TLSVersion.TLSv1`, `TLSVersion.TLSv1_1`, `TLSVersion.TLSv1_2`, `TLSVersion.TLSv1_3`

*class *ssl.TLSVersion

[`enum.IntEnum`](https://docs.python.org/3.14/library/enum.html#enum.IntEnum) collection of SSL and TLS versions for `SSLContext.maximum_version` and `SSLContext.minimum_version`.

Added in version 3.7.

 TLSVersion.MINIMUM_SUPPORTED

 TLSVersion.MAXIMUM_SUPPORTED

The lowest or highest SSL or TLS version that is supported. These are magic constants. The values they hold do not correspond to the actual lowest and highest TLS/SSL versions available.

 TLSVersion.SSLv3

 TLSVersion.TLSv1

 TLSVersion.TLSv1_1

 TLSVersion.TLSv1_2

 TLSVersion.TLSv1_3

SSL 3.0 to TLS 1.3.

Deprecated since version 3.10: Every `TLSVersion` member apart from `TLSVersion.TLSv1_2` and `TLSVersion.TLSv1_3` is deprecated.

[Subject index](INDEX.md) · [Previous](ssl-sslerrornumber-class.md) · [Continue](ssl-sslsocket-class-to-shutdown.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md) · [Owning module, declaration or section: Constants](ssl-cert-none-to-ssl-cert-required.md)
