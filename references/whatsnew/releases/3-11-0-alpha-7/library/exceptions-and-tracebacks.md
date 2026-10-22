# Python 3.11.0 alpha 7 / library / exceptions and tracebacks

[bpo-47099](https://bugs.python.org/issue?@action=redirect&bpo=47099): Each `URLError` exception message thrown by `urllib.request.URLopener` now puts a colon between `ftp error` and what follows. Earlier, `open_ftp()` skipped that colon. Oleg Iarygin supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
