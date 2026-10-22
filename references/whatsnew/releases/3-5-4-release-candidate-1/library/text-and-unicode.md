# Python 3.5.4 release candidate 1 / library / text and unicode

[bpo-29800](https://bugs.python.org/issue?@action=redirect&bpo=29800): Repair crashes in partial.__repr__ whenever the keys of partial.keywords are not strings. Michael Seifert contributed the patch.

[bpo-8256](https://bugs.python.org/issue?@action=redirect&bpo=8256): Repaired the possible failure or crash of input() when the "encoding" or "errors" attributes of sys.stdin or sys.stdout are unset or are not strings.

[bpo-30003](https://bugs.python.org/issue?@action=redirect&bpo=30003): Repair the handling of escape characters within the HZ codec. Built on a patch from Ma Lin.

[bpo-30746](https://bugs.python.org/issue?@action=redirect&bpo=30746): Disallowed the "=" character within environment variable names passed to `os.putenv()` and `os.spawn*()`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
