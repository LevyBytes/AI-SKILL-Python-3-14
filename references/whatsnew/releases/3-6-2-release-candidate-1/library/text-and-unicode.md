# Python 3.6.2 release candidate 1 / library / text and unicode

[bpo-30003](https://bugs.python.org/issue?@action=redirect&bpo=30003): Correct how escape characters are handled within the HZ codec. Ma Lin's patch was the basis.

[bpo-29800](https://bugs.python.org/issue?@action=redirect&bpo=29800): Repair crashes within partial.__repr__ whenever the keys of partial.keywords are not strings. Michael Seifert wrote the patch.

[bpo-8256](https://bugs.python.org/issue?@action=redirect&bpo=8256): Corrected a possible crash or failure of input() arising when the "encoding" or "errors" attributes of sys.stdin or sys.stdout are unset or are not strings.

[bpo-23894](https://bugs.python.org/issue?@action=redirect&bpo=23894): lib2to3 will now recognize `rb'...'` along with `f'...'` strings.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
