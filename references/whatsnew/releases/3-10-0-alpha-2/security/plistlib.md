# Python 3.10.0 alpha 2 / security / plistlib

[bpo-42051](https://bugs.python.org/issue?@action=redirect&bpo=42051): To sidestep XML vulnerabilities, the [`plistlib`](https://docs.python.org/3.14/library/plistlib.html#module-plistlib) module will no longer permit entity declarations inside XML plist files. Users should be unaffected, since ordinary plist files do not employ entity declarations.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
