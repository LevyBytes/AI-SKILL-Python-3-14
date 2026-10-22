# --with-ssl-default-suites=[python/openssl/STRING]

--with-ssl-default-suites=[python|openssl|STRING]

Replace the default OpenSSL cipher-suites string:

- `python` (default): adopt Python's preferred picks;

- `openssl`: keep OpenSSL's own defaults as they are;

- *STRING*: supply a custom string

Refer to the [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) module.

Added in version 3.7.

Changed in version 3.10: Choosing `python` or *STRING* additionally pins TLS 1.2 as the lowest allowed protocol version.

[Subject index](INDEX.md) · [Previous source section](builtin-hash-algorithm-selection.md) · [Following source section](disable-safety.md)
