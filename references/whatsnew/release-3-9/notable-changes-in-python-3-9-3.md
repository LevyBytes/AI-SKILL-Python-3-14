# What's New In Python 3.9 / Notable changes in Python 3.9.3 - ftplib

### Notable changes in Python 3.9.3

A security fix changes how [`ftplib.FTP`](https://docs.python.org/3.14/library/ftplib.html#ftplib.FTP) behaves so that it stops trusting the IPv4 address the remote server hands over while opening a passive data channel; the ftp server’s own IP address is reused in its place. For the odd bit of code that depends on the former behavior, flip a `trust_server_pasv_ipv4_address` attribute on your FTP instance to `True`. (See [gh-87451](https://github.com/python/cpython/issues/87451))

[Subject index](INDEX.md) · [Previous source section](urllib-parse.md) · [Next source section](urllib-parse.md) · [Release/subject declaration](summary-release-highlights.md)
