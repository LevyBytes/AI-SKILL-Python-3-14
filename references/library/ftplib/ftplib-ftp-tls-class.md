# ftplib: `ftplib.FTP_TLS`

### FTP_TLS objects

 *class *ftplib.FTP_TLS(*host=''*, *user=''*, *passwd=''*, *acct=''*, ***, *context=None*, *timeout=None*, *source_address=None*, *encoding='utf-8'*)

A subclass of `FTP` that layers TLS support onto FTP per [**RFC 4217**](https://datatracker.ietf.org/doc/html/rfc4217.html). It reaches port 21, implicitly protecting the FTP control connection prior to authentication.

Note

The user must explicitly secure the data connection by calling the `prot_p()` method.

Parameters:

- **host** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – The name of the host to reach. When supplied, the constructor implicitly invokes `connect(host)`.

- **user** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – The account name used at login (default: `'anonymous'`). When supplied, the constructor implicitly invokes `login(host, passwd, acct)`.

- **passwd** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – The credential supplied at login. When omitted, and where *passwd* equals the empty string or `"-"`, a password gets generated automatically.

- **acct** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – Account details fed to the `ACCT` FTP command. Hardly any systems implement it. Consult [RFC-959](https://datatracker.ietf.org/doc/html/rfc959.html) for further detail.

- **context** ([`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext)) – An SSL context object that lets you gather SSL configuration options, certificates and private keys into one, possibly long-lived, structure. For best practices, please review [Security considerations](https://docs.python.org/3.14/library/ssl.html#ssl-security).

- **timeout** ([*float*](https://docs.python.org/3.14/library/functions.html#float)* | **None*) – How many seconds to allow blocking calls such as `connect()` before timing out (default: the global default timeout setting).

- **source_address** ([*tuple*](https://docs.python.org/3.14/library/stdtypes.html#tuple)* | **None*) – A 2-tuple `(host, port)` that the socket binds to as its own source address ahead of connecting.

- **encoding** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – Which encoding applies to directories and filenames (default: `'utf-8'`).

Added in version 3.2.

Changed in version 3.3: Added the *source_address* parameter.

Changed in version 3.4: Hostname checking via [`ssl.SSLContext.check_hostname`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.check_hostname) plus *Server Name Indication* (see [`ssl.HAS_SNI`](https://docs.python.org/3.14/library/ssl.html#ssl.HAS_SNI)) is now handled by the class.

Changed in version 3.9: Setting the *timeout* parameter to zero now triggers a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError), blocking creation of a non-blocking socket. The *encoding* parameter arrived, and its default shifted away from Latin-1 over to UTF-8 in line with [**RFC 2640**](https://datatracker.ietf.org/doc/html/rfc2640.html).

Changed in version 3.12: Both deprecated parameters, *keyfile* and *certfile*, are now gone.

Below is an example session that exercises the `FTP_TLS` class:

```python
>>> ftps = FTP_TLS('ftp.pureftpd.org')
>>> ftps.login()
'230 Anonymous user logged in'
>>> ftps.prot_p()
'200 Data protection level set to "private"'
>>> ftps.nlst()
['6jack', 'OpenBSD', 'antilink', 'blogbench', 'bsdcam', 'clockspeed', 'djbdns-jedi', 'docs', 'eaccelerator-jedi', 'favicon.ico', 'francotone', 'fugu', 'ignore', 'libpuzzle', 'metalog', 'minidentd', 'misc', 'mysql-udf-global-user-variables', 'php-jenkins-hash', 'php-skein-hash', 'php-webdav', 'phpaudit', 'phpbench', 'pincaster', 'ping', 'posto', 'pub', 'public', 'public_keys', 'pure-ftpd', 'qscan', 'qtc', 'sharedance', 'skycache', 'sound', 'tmp', 'ucarp']

```

`FTP_TLS` class inherits from `FTP`, defining these additional methods and attributes:

[Subject index](INDEX.md) · [Previous](ftplib-ftp-nlst-to-ftplib-ftp-close.md) · [Continue](ftplib-ftp-tls-auth-to-ftplib-ftp-tls-prot-c.md) · [Owning module, declaration or section: ftplib](ftplib-ftp-protocol-client.md)
