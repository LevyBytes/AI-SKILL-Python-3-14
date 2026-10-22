# Python 3.8.0 alpha 1 / library / site

[bpo-10496](https://bugs.python.org/issue?@action=redirect&bpo=10496): `posixpath.expanduser()` now leaves the supplied *path* untouched whenever the `HOME` environment variable is missing and the active user lacks a home directory (that is, when the current user identifier is absent from the password database). The change repairs the [`site`](https://docs.python.org/3.14/library/site.html#module-site) module for cases where the active user is missing from the password database (where the user owns no home directory).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
