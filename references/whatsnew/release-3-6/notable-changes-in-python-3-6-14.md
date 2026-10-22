# What's New In Python 3.6 / Notable changes in Python 3.6.14 — ftplib, urllib.parse

### Notable changes in Python 3.6.14

A security patch changes how [`ftplib.FTP`](https://docs.python.org/3.14/library/ftplib.html#ftplib.FTP) behaves so that it stops trusting the IPv4 address handed back by the remote server while establishing a passive data channel. In its place we fall back on the ftp server's own IP address. Should you have atypical code that depends on the former conduct, give your FTP instance a `trust_server_pasv_ipv4_address` attribute set to `True`. (See [gh-87451](https://github.com/python/cpython/issues/87451))

When newline or tab characters turn up inside portions of a URL, they open the door to certain attack vectors. In keeping with the WHATWG specification that revises RFC 3986, the parser [`urllib.parse()`](https://docs.python.org/3.14/library/urllib.parse.html#module-urllib.parse) now strips the ASCII newline `\n`, `\r`, and tab `\t` characters out of the URL, thwarting those attacks. Which characters get pulled is governed by a fresh module-level variable, `urllib.parse._UNSAFE_URL_BYTES_TO_REMOVE`. (See [gh-88048](https://github.com/python/cpython/issues/88048))

[Subject index](INDEX.md) · [Previous source section](notable-changes-in-python-3-6-13.md) · [Release/subject declaration](summary-release-highlights.md)
