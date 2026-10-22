# ssl: `ssl.AlertDescription`, `Purpose.SERVER_AUTH`, `Purpose.CLIENT_AUTH`

*class *ssl.AlertDescription

[`enum.IntEnum`](https://docs.python.org/3.14/library/enum.html#enum.IntEnum) collection of ALERT_DESCRIPTION_* constants.

Added in version 3.6.

 Purpose.SERVER_AUTH

Option for `create_default_context()` and `SSLContext.load_default_certs()`. This value signals that the context is allowed to authenticate web servers (and so it will serve to create client-side sockets).

Added in version 3.4.

 Purpose.CLIENT_AUTH

Option for `create_default_context()` and `SSLContext.load_default_certs()`. This value signals that the context is allowed to authenticate web clients (and so it will serve to create server-side sockets).

Added in version 3.4.

[Subject index](INDEX.md) · [Previous](ssl-has-tlsv1-2-to-ssl-alert-description-internal-error.md) · [Continue](ssl-sslerrornumber-class.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md) · [Owning module, declaration or section: Constants](ssl-cert-none-to-ssl-cert-required.md)
