# Python 3.14.4 final / security / wsgiref

[gh-144370](https://github.com/python/cpython/issues/144370): Forbid control characters in the status value within [`wsgiref.handlers`](https://docs.python.org/3.14/library/wsgiref.html#module-wsgiref.handlers), heading off HTTP header injections. Benedikt Johannes wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
