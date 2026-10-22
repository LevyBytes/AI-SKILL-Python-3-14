# Python 3.10.0 alpha 7 / security / pydoc

[bpo-42988](https://bugs.python.org/issue?@action=redirect&bpo=42988): [**CVE 2021-3426**](https://www.cve.org/CVERecord?id=CVE-2021-3426): The `getfile` feature of the [`pydoc`](https://docs.python.org/3.14/library/pydoc.html#module-pydoc) module was removed because it could be misused to read arbitrary files off disk (a directory traversal vulnerability). On top of that, even the source of Python modules may hold sensitive data such as passwords. David Schwörer reported the vulnerability.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
