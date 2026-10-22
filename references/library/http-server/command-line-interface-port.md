# http.server: HTTP server CLI port and serving options

port

By default the server listens on port 8000. Override that default by supplying the wanted port number as an argument:

```bash
python -m http.server 9000

```

 -b, --bind &lt;address&gt;

Names a particular address for it to bind to. IPv4 as well as IPv6 addresses work. By default the server binds across all interfaces. As an example, the command below makes the server bind to localhost alone:

```bash
python -m http.server --bind 127.0.0.1

```

Added in version 3.4.

Changed in version 3.8: Support IPv6 in the `--bind` option.

 -d, --directory &lt;dir&gt;

Names a directory from which it should serve the files. By default the server relies on the current directory. As an example, the command below points at a particular directory:

```bash
python -m http.server --directory /tmp/

```

Added in version 3.7.

 -p, --protocol &lt;version&gt;

Names the HTTP version the server conforms to. By default the server conforms to HTTP/1.0. As an example, the command below starts an HTTP/1.1 conformant server:

```bash
python -m http.server --protocol HTTP/1.1

```

Added in version 3.11.

 --cgi

`CGIHTTPRequestHandler` can be turned on at the command line by supplying the `--cgi` option:

```python
python -m http.server --cgi

```

Deprecated since version 3.13, will be removed in version 3.15: Because `CGIHTTPRequestHandler` is going away, the `--cgi` command line support in `http.server` is being dropped too.

Warning

`CGIHTTPRequestHandler` and the `--cgi` command-line option are not meant for use with untrusted clients and could be open to exploitation. Always run them inside a secure environment.

 --tls-cert

Names a TLS certificate chain for HTTPS connections:

```bash
python -m http.server --tls-cert fullchain.pem

```

Added in version 3.14.

 --tls-key

Names a private key file for HTTPS connections.

Using this option demands that `--tls-cert` also be given.

Added in version 3.14.

 --tls-password-file

Names the password file for password-protected private keys:

```bash
python -m http.server \
       --tls-cert cert.pem \
       --tls-key key.pem \
       --tls-password-file password.txt

```

Using this option demands that `--tls-cert` also be given.

Added in version 3.14.

[Subject index](INDEX.md) · [Previous](command-line-file-server.md) · [Continue](security-considerations.md) · [Owning module, declaration or section: http.server](http-server-httpserver-class.md) · [Owning module, declaration or section: Command-line interface](command-line-file-server.md)
