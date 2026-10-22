# Python 3.6.2 release candidate 1 / library / assigning enter none or exit none contextlib abstractcontextmanager permits anti registration

[bpo-30266](https://bugs.python.org/issue?@action=redirect&bpo=30266): By assigning __enter__ = None or __exit__ = None, contextlib.AbstractContextManager now permits anti-registration, mirroring the approach first added in [bpo-25958](https://bugs.python.org/issue?@action=redirect&bpo=25958). Jelle Zijlstra wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
