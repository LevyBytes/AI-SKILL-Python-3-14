# Python 3.12.0 alpha 4 / windows / winreg

[bpo-43984](https://bugs.python.org/issue?@action=redirect&bpo=43984): On a conversion error, [`winreg.SetValueEx()`](https://docs.python.org/3.14/library/winreg.html#winreg.SetValueEx) now leaves the existing value alone. Formerly such an error would write `-1` instead.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
