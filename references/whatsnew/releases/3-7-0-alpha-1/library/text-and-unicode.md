# Python 3.7.0 alpha 1 / library / text and unicode

[bpo-27897](https://bugs.python.org/issue?@action=redirect&bpo=27897): Closed a possible crash inside sqlite3.Connection.create_collation() that triggered whenever an invalid string-like object was passed as a name. Xiang Zhang authored the patch.

[bpo-29800](https://bugs.python.org/issue?@action=redirect&bpo=29800): Crashes from partial.__repr__ when the keys in partial.keywords are not strings were corrected. Michael Seifert wrote the patch.

[bpo-8256](https://bugs.python.org/issue?@action=redirect&bpo=8256): A potential failure or crash in input() — happening when the “encoding” or “errors” attributes of sys.stdin or sys.stdout were unset or not strings — was corrected.

[bpo-31170](https://bugs.python.org/issue?@action=redirect&bpo=31170): expat: Bring libexpat up from 2.2.3 to 2.2.4. Repair the copying of partial characters for UTF-8 input (libexpat bug 115): [https://github.com/libexpat/libexpat/issues/115](https://github.com/libexpat/libexpat/issues/115)

[bpo-28114](https://bugs.python.org/issue?@action=redirect&bpo=28114): Closed a crash inside parse_envlist() that occurred when env held byte strings. Eryk Sun authored the patch.

[bpo-30746](https://bugs.python.org/issue?@action=redirect&bpo=30746): Forbid the "=" character within environment variable names in `os.putenv()` and `os.spawn*()`.

[bpo-29193](https://bugs.python.org/issue?@action=redirect&bpo=29193): The format-string argument accepted by string.Formatter.format() became positional-only.

[bpo-1198569](https://bugs.python.org/issue?@action=redirect&bpo=1198569): A `string.Template` subclass may optionally set `braceidpattern` whenever it needs distinct placeholder patterns for inside versus outside the braces. When it is None (the default) the value falls back to `idpattern`.

[bpo-30003](https://bugs.python.org/issue?@action=redirect&bpo=30003): Escape-character handling within the HZ codec was corrected. The work is based on a patch from Ma Lin.

[bpo-23894](https://bugs.python.org/issue?@action=redirect&bpo=23894): The `rb'...'` and `f'...'` string forms are now understood by lib2to3.

[bpo-24744](https://bugs.python.org/issue?@action=redirect&bpo=24744): Should *path* be a string, pkgutil.walk_packages will now raise ValueError. Sanyam Khurana contributed this.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
