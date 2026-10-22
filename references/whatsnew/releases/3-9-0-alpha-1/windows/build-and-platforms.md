# Python 3.9.0 alpha 1 / windows / build and platforms

[bpo-10945](https://bugs.python.org/issue?@action=redirect&bpo=10945): Officially drop support for creating bdist_wininst installers on non-Windows systems.

[bpo-37380](https://bugs.python.org/issue?@action=redirect&bpo=37380): On Windows, unfinished processes are no longer gathered via `subprocess._active` for later cleanup. Ruslan Kuprieiev wrote the patch.

[bpo-37351](https://bugs.python.org/issue?@action=redirect&bpo=37351): Removes libpython38.a from standard Windows distribution.

[bpo-35360](https://bugs.python.org/issue?@action=redirect&bpo=35360): Update Windows builds to use SQLite 3.28.0.

[bpo-36779](https://bugs.python.org/issue?@action=redirect&bpo=36779): Keep `time.tzname` accurate under Windows whenever the active code page happens to be CP_UTF7 or CP_UTF8.

[bpo-38589](https://bugs.python.org/issue?@action=redirect&bpo=38589): Corrects the HTML Help shortcut for cases where Windows lives somewhere other than the C drive

[bpo-37283](https://bugs.python.org/issue?@action=redirect&bpo=37283): In the Windows installer, make a command-line or unattend.xml setting take precedence over states already detected.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
