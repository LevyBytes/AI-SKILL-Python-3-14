# Python 3.7.0 release candidate 1 / idle / text

[bpo-33656](https://bugs.python.org/issue?@action=redirect&bpo=33656): For Windows, invoke an API declaring that tk handles DPI scaling. Running Windows 8.1+ or 10, leaving the Python executable's DPI compatibility settings as-is, and using a display above 96 DPI, text and lines ought to render crisper. Elsewhere there should be no change.

[bpo-33763](https://bugs.python.org/issue?@action=redirect&bpo=33763): IDLE: Swap the label widget out for a `read-only text widget` driving code context.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
