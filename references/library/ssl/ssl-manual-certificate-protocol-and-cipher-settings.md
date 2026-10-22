# ssl manual certificate, protocol and cipher settings

### Manual settings

#### Verifying certificates

Invoke the `SSLContext` constructor on its own and the default you get is `CERT_NONE`. Because that mode performs no authentication of the opposite peer, it can leave you exposed — particularly in client mode, where you generally want assurance that the server on the far end is genuine. Hence the strong recommendation to choose `CERT_REQUIRED` whenever you are acting as a client. That alone, though, does not finish the job; you must additionally confirm that the server's certificate — retrievable via a `SSLSocket.getpeercert()` call — corresponds to the service you intended to reach. Across many protocols and applications the service is recognizable by its hostname, and turning on `SSLContext.check_hostname` makes this routine verification happen for you automatically.

Changed in version 3.7: OpenSSL now carries out hostname matching. `match_hostname()` is no longer relied upon by Python.

Operating in server mode, should you wish to authenticate the connecting clients through the SSL layer itself (instead of relying on some higher-level authentication scheme), you must again set `CERT_REQUIRED` and inspect the client's certificate in the same way.

#### Protocol versions

Both SSL version 2 and version 3 are regarded as insecure, which makes relying on them hazardous. To maximize interoperability across clients and servers, the suggested protocol version to pick is either `PROTOCOL_TLS_CLIENT` or `PROTOCOL_TLS_SERVER`. By default SSLv2 and SSLv3 come disabled.

```python
>>> client_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
>>> client_context.minimum_version = ssl.TLSVersion.TLSv1_2
>>> client_context.maximum_version = ssl.TLSVersion.TLSv1_3

```

The SSL client context built just above permits only TLSv1.2 and TLSv1.3 (where your system provides support) when connecting to a server. By default `PROTOCOL_TLS_CLIENT` brings certificate validation along with hostname checks. It remains up to you to load certificates into the context.

#### Cipher selection

Where your security needs are more demanding, the `SSLContext.set_ciphers()` method lets you fine-tune which ciphers are available during the negotiation of an SSL session. As of Python 3.2.3 the ssl module switches off a set of weak ciphers by default, though you might still wish to narrow the selection further. Make a point of consulting OpenSSL's documentation covering the [cipher list format](https://docs.openssl.org/1.1.1/man1/ciphers/#cipher-list-format). To see which ciphers a particular cipher list activates, turn to `SSLContext.get_ciphers()` or run the `openssl ciphers` command on your machine.

[Subject index](INDEX.md) · [Continue](ssl-multiprocessing-tls-1-3-and-platform-limitations.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md)
