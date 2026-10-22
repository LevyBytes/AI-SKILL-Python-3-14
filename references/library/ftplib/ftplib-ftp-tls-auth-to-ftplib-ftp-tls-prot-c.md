# ftplib.FTP_TLS: `auth()`, `ccc()`, `prot_p()`, `prot_c()`

ssl_version

The SSL version to use (defaults to [`ssl.PROTOCOL_SSLv23`](https://docs.python.org/3.14/library/ssl.html#ssl.PROTOCOL_SSLv23)).

 auth()

Establish a secure control connection through TLS or SSL, according to whatever the `ssl_version` attribute names.

Changed in version 3.4: Hostname checking via [`ssl.SSLContext.check_hostname`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.check_hostname) plus *Server Name Indication* (see [`ssl.HAS_SNI`](https://docs.python.org/3.14/library/ssl.html#ssl.HAS_SNI)) is now handled by the method.

 ccc()

Switch the control channel back to plaintext. This comes in handy for exploiting firewalls that can manage NAT with non-secure FTP without needing to open fixed ports.

Added in version 3.3.

 prot_p()

Set up secure data connection.

 prot_c()

Set up clear text data connection.

[Subject index](INDEX.md) · [Previous](ftplib-ftp-tls-class.md) · [Continue](ftplib-error-reply-to-ftplib-all-errors.md) · [Owning module, declaration or section: ftplib](ftplib-ftp-protocol-client.md) · [Owning module, declaration or section: ftplib.FTP_TLS](ftplib-ftp-tls-class.md) · [Owning module, declaration or section: FTP_TLS objects](ftplib-ftp-tls-class.md)
