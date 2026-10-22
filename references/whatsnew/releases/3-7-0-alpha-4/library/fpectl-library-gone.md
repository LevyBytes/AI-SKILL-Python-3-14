# Python 3.7.0 alpha 4 / library / fpectl library gone

[bpo-29137](https://bugs.python.org/issue?@action=redirect&bpo=29137): The `fpectl` library is gone. It was never on by default, never functioned right on x86-64, and altered the Python ABI in ways that triggered unexpected breakage of C extensions.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
