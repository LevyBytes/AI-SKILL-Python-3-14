# Python 3.5.0 alpha 1 / library / shutting io bytesio still exported buffer refused guarding against corrupting

[bpo-23099](https://bugs.python.org/issue?@action=redirect&bpo=23099): Shutting an io.BytesIO that still has an exported buffer is now refused, guarding against corrupting that exported buffer.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
