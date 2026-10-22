# What’s New In Python 3.8 / Notable changes in Python 3.8.9 — ftplib

### Notable changes in Python 3.8.9

As part of a security patch, [`ftplib.FTP`](https://docs.python.org/3.14/library/ftplib.html#ftplib.FTP) was changed so that it stops trusting the IPv4 address the remote server hands back while opening a passive data channel. In its place the ftp server's own IP address is reused. Should some unusual code depend on the former conduct, give your FTP object a `trust_server_pasv_ipv4_address` attribute set to `True`. (See [gh-87451](https://github.com/python/cpython/issues/87451))

[Subject index](INDEX.md) · [Previous source section](notable-changes-in-python-3-8-8.md) · [Next source section](macos-11-0-and-apple-silicon-mac-support.md) · [Release/subject declaration](assignment-expressions.md)
