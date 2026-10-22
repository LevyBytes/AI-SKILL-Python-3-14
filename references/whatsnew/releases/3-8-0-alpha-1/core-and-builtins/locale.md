# Python 3.8.0 alpha 1 / core and builtins / locale

[bpo-34485](https://bugs.python.org/issue?@action=redirect&bpo=34485): On Windows, LC_CTYPE is now configured to the user's preferred locale during startup. Formerly the LC_CTYPE locale began as ?C? and only shifted once setlocale(LC_CTYPE, ??) or setlocale(LC_ALL, ??) was invoked.

[bpo-34485](https://bugs.python.org/issue?@action=redirect&bpo=34485): Standard streams such as sys.stdout now adopt the ?surrogateescape? error handler in place of ?strict? whenever the POSIX locale applies (that is, when the C locale stays uncoerced and UTF-8 Mode remains off).

[bpo-34527](https://bugs.python.org/issue?@action=redirect&bpo=34527): On FreeBSD, Py_DecodeLocale() and Py_EncodeLocale() now apply the ASCII encoding whenever the LC_CTYPE locale equals ?POSIX? as well, no longer doing so only when the LC_CTYPE locale equals ?C?.

[bpo-34527](https://bugs.python.org/issue?@action=redirect&bpo=34527): UTF-8 Mode is now switched on by the ?POSIX? locale as well, not just by the ?C? locale.

[bpo-34403](https://bugs.python.org/issue?@action=redirect&bpo=34403): On HP-UX under the C or POSIX locale, sys.getfilesystemencoding() now yields ?ascii? in place of ?roman8? (provided UTF-8 Mode stays off and the C locale remains uncoerced).

[bpo-35336](https://bugs.python.org/issue?@action=redirect&bpo=35336): Repair the PYTHONCOERCECLOCALE=1 environment variable: coerce the C locale only when the LC_CTYPE locale equals "C".

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
