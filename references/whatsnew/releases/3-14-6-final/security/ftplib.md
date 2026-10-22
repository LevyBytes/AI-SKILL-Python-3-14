# Python 3.14.6 final / security / ftplib

[gh-87451](https://github.com/python/cpython/issues/87451): By default, the undocumented `ftpcp` function of the [`ftplib`](https://docs.python.org/3.14/library/ftplib.html#module-ftplib) module will no longer trust the IPv4 address that the source server hands back in reply to the `PASV` command, which rounds out the remedy for CVE-2021-4189. Just like [`ftplib.FTP`](https://docs.python.org/3.14/library/ftplib.html#ftplib.FTP), you can restore the prior behavior by assigning `True` to the `trust_server_pasv_ipv4_address` attribute on the source `ftplib.FTP` instance. Credit for reporting this goes to Qi Deng at Aurascape AI.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
