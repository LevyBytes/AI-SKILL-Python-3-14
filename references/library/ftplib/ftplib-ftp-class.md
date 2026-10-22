# ftplib: `ftplib.FTP`

### Reference

### FTP objects

 *class *ftplib.FTP(*host=''*, *user=''*, *passwd=''*, *acct=''*, *timeout=None*, *source_address=None*, ***, *encoding='utf-8'*)

Return a new instance of the `FTP` class.

Parameters:

- **host** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – The name of the host to reach. When supplied, the constructor implicitly invokes `connect(host)`.

- **user** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – The account name used at login (default: `'anonymous'`). When supplied, the constructor implicitly invokes `login(host, passwd, acct)`.

- **passwd** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – The credential supplied at login. When omitted, and where *passwd* equals the empty string or `"-"`, a password gets generated automatically.

- **acct** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – Account details fed to the `ACCT` FTP command. Hardly any systems implement it. Consult [RFC-959](https://datatracker.ietf.org/doc/html/rfc959.html) for further detail.

- **timeout** ([*float*](https://docs.python.org/3.14/library/functions.html#float)* | **None*) – How many seconds to allow blocking calls such as `connect()` before timing out (default: the global default timeout setting).

- **source_address** ([*tuple*](https://docs.python.org/3.14/library/stdtypes.html#tuple)* | **None*) – A 2-tuple `(host, port)` that the socket binds to as its own source address ahead of connecting.

- **encoding** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – Which encoding applies to directories and filenames (default: `'utf-8'`).

The [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement is supported by the `FTP` class, for instance:

```python
>>> from ftplib import FTP
>>> with FTP("ftp1.at.proftpd.org") as ftp:
...     ftp.login()
...     ftp.dir()
...
'230 Anonymous login ok, restrictions apply.'
dr-xr-xr-x   9 ftp      ftp           154 May  6 10:43 .
dr-xr-xr-x   9 ftp      ftp           154 May  6 10:43 ..
dr-xr-xr-x   5 ftp      ftp          4096 May  6 10:43 CentOS
dr-xr-xr-x   3 ftp      ftp            18 Jul 10  2008 Fedora
>>>

```

Changed in version 3.2: Support for the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement was added.

Changed in version 3.3: *source_address* parameter was added.

Changed in version 3.9: Setting the *timeout* parameter to zero now triggers a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError), blocking creation of a non-blocking socket. The *encoding* parameter arrived, and its default shifted away from Latin-1 over to UTF-8 in line with [**RFC 2640**](https://datatracker.ietf.org/doc/html/rfc2640.html).

A number of `FTP` methods come in two variants: one geared to text files and the other to binary files. Each method takes its name from the command it issues, with `lines` appended for the text variant or `binary` for the binary one.

These methods belong to `FTP` instances:

[Subject index](INDEX.md) · [Continue](ftplib-ftp-set-debuglevel-to-ftplib-ftp-voidcmd.md) · [Owning module, declaration or section: ftplib](ftplib-ftp-protocol-client.md)
