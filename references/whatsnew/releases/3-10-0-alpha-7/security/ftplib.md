# Python 3.10.0 alpha 7 / security / ftplib

[bpo-43285](https://bugs.python.org/issue?@action=redirect&bpo=43285): By default, [`ftplib`](https://docs.python.org/3.14/library/ftplib.html#module-ftplib) will no longer trust the IP address that a server returns in reply to the PASV command. This stops a hostile FTP server from leveraging that reply to scan IPv4 address-and-port pairs across the client network.

If the old, vulnerable behavior is needed, code can set a `trust_server_pasv_ipv4_address` attribute to `True` on its [`ftplib.FTP`](https://docs.python.org/3.14/library/ftplib.html#ftplib.FTP) instances to switch it back on.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
