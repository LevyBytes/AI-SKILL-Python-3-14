# Python 3.14.0 alpha 1 / library / urllib request

[gh-122909](https://github.com/python/cpython/issues/122909): Inside urllib.request, whenever a URLError gets raised while an ftp URL is opened, that exception's argument is now reliably a string. Prior releases handed URLError either a string or else an ftplib exception object as its argument.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
