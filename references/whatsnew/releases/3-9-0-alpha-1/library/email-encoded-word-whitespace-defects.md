# Python 3.9.0 alpha 1 / library / email headers contain rfc2047 encoded words parse even whitespace

[bpo-21315](https://bugs.python.org/issue?@action=redirect&bpo=21315): Email headers that contain RFC2047 encoded words now parse even with the whitespace missing, and a defect gets recorded. Likewise, absent trailing whitespace following encoded words is now logged as a defect.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
