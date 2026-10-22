# Python 3.8.0 beta 1 / security / urllib request

[bpo-35907](https://bugs.python.org/issue?@action=redirect&bpo=35907): [**CVE 2019-9948**](https://www.cve.org/CVERecord?id=CVE-2019-9948): Blocks a file-read avenue by rejecting the `local-file://` and `local_file://` URL schemes within `URLopener().open()` plus `URLopener().retrieve()` belonging to [`urllib.request`](https://docs.python.org/3.14/library/urllib.request.html#module-urllib.request).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
