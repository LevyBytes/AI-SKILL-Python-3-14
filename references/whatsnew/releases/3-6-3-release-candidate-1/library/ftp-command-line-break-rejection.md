# Python 3.6.3 release candidate 1 / library / ftplib ftp putline will raise valueerror whenever command holds cr or

[bpo-30119](https://bugs.python.org/issue?@action=redirect&bpo=30119): ftplib.FTP.putline() will now raise ValueError whenever a command holds CR or LF. Donghee Na wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
