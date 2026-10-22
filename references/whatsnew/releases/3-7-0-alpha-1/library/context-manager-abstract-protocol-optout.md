# Python 3.7.0 alpha 1 / library / assigning enter none or exit none lets contextlib abstractcontextmanager perform

[bpo-30266](https://bugs.python.org/issue?@action=redirect&bpo=30266): Assigning __enter__ = None or __exit__ = None now lets contextlib.AbstractContextManager perform anti-registration, mirroring the approach first seen in [bpo-25958](https://bugs.python.org/issue?@action=redirect&bpo=25958). Jelle Zijlstra wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
