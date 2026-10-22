# Python 3.5.0 alpha 4 / core and builtins / build and platforms

[bpo-22980](https://bugs.python.org/issue?@action=redirect&bpo=22980): On Linux, GNU/KFreeBSD plus the Hurd, the architecture triplet is now embedded inside the extension name for C extensions, simplifying tests of builds that target distinct ABIs from one working tree. On OS X the extension name now carries [**PEP 3149**](https://peps.python.org/pep-3149/)-style data.

[bpo-22977](https://bugs.python.org/issue?@action=redirect&bpo=22977): Corrected the formatting of Windows error messages under Wine. Martin Panter wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
