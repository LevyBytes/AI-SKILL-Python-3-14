# What's New In Python 3.7 / Notable changes in Python 3.7.11 - ftplib, urllib.parse

### Notable changes in Python 3.7.11

A security fix changes how [`ftplib.FTP`](https://docs.python.org/3.14/library/ftplib.html#ftplib.FTP) behaves so it stops trusting the IPv4 address that the remote server sends while establishing a passive data channel. We fall back on the ftp server IP address in its place. For uncommon code that needs the former behavior, place a `trust_server_pasv_ipv4_address` attribute set to `True` onto your FTP instance. (See [gh-87451](https://github.com/python/cpython/issues/87451))

When newline or tab characters appear inside portions of a URL, certain styles of attack become possible. In keeping with the WHATWG specification that supersedes RFC 3986, the ASCII newline `\n`, `\r` and tab `\t` characters get stripped out of the URL by the [`urllib.parse()`](https://docs.python.org/3.14/library/urllib.parse.html#module-urllib.parse) parser, heading off such attacks. Which characters get removed is governed by a fresh module-level variable `urllib.parse._UNSAFE_URL_BYTES_TO_REMOVE`. (See [gh-88048](https://github.com/python/cpython/issues/88048))

### Notable security feature in 3.7.14

[Subject index](INDEX.md) · [Previous source section](notable-changes-in-python-3-7-10.md) · [Release/subject declaration](summary-release-highlights.md) · [Following release/subject continuation](notable-security-feature-in-3-7-14.md)
