# ssl: `ssl.SSLContext`

### SSL contexts

Added in version 3.2.

An SSL context retains assorted data that outlives any single SSL connection, such as SSL configuration options, certificate(s) and private key(s). It additionally keeps a cache of SSL sessions for server-side sockets so that repeated connections from the same clients go faster.

 *class *ssl.SSLContext(*protocol=None*)

Build a new SSL context. You may hand in *protocol*, which must be one of the `PROTOCOL_*` constants this module defines. The parameter declares which version of the SSL protocol to use. As a rule, the server settles on a given protocol version, and the client has to fall in line with the server's pick. Most versions cannot interoperate with the others. When left unspecified, the default is `PROTOCOL_TLS`, which gives the broadest compatibility with other versions.

The table below shows which versions in a client (down the side) are able to connect to which versions in a server (along the top):

| *client* / **server** | **SSLv2** | **SSLv3** | **TLS** [3] | **TLSv1** | **TLSv1.1** | **TLSv1.2** |
| --- | --- | --- | --- | --- | --- | --- |
| *SSLv2* | yes | no | no [1] | no | no | no |
| *SSLv3* | no | yes | no [2] | no | no | no |
| *TLS* (*SSLv23*) [3] | no [1] | no [2] | yes | yes | yes | yes |
| *TLSv1* | no | no | yes | yes | no | no |
| *TLSv1.1* | no | no | yes | no | yes | no |
| *TLSv1.2* | no | no | yes | no | no | yes |

Footnotes

See also

`create_default_context()` lets the `ssl` module choose security settings for a given purpose.

[Subject index](INDEX.md) · [Previous](sslsocket-get-channel-binding-to-sslsocket-session-reused.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md) · [Required continuation of the source contract](sslcontext-cert-store-stats-to-sslcontext-get-ca-certs.md)
