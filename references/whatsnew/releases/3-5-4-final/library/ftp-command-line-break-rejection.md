# Python 3.5.4 final / library / ftplib ftp putline raises valueerror any command holding cr or lf

[bpo-30119](https://bugs.python.org/issue?@action=redirect&bpo=30119): ftplib.FTP.putline() now raises ValueError for any command holding a CR or LF. Donghee Na contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
