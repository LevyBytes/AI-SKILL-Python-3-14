# Python 3.8.0 alpha 1 / library / text and unicode

[bpo-11874](https://bugs.python.org/issue?@action=redirect&bpo=11874): Used a stronger regex while splitting usage into wrappable pieces. This avoids spurious assertion errors arising from custom metavar strings.

[bpo-30877](https://bugs.python.org/issue?@action=redirect&bpo=30877): Corrected a bug in the Python implementation of the JSON decoder that kept the cache of parsed strings from clearing once decoding completed. Based on patch by c-fos.

[bpo-33497](https://bugs.python.org/issue?@action=redirect&bpo=33497): Introduce an errors param on cgi.parse_multipart and have a FieldStorage encoding apply the supplied errors (required by Twisted). Patch by Amber Brown.

[bpo-33134](https://bugs.python.org/issue?@action=redirect&bpo=33134): While computing a dataclass's __hash__, employ the lookup table to hold the function yielding the __hash__ value. That beats looking up a string and then testing said string to decide the action.

[bpo-33663](https://bugs.python.org/issue?@action=redirect&bpo=33663): Cast content length to a string ahead of placing it into the header.

[bpo-33422](https://bugs.python.org/issue?@action=redirect&bpo=33422): Stop trailing quotation marks from being stripped during byte/string literal lookups in pydoc. Patch by Andrés Delfino.

[bpo-34604](https://bugs.python.org/issue?@action=redirect&bpo=34604): Corrected possible mojibake in the error message from `pwd.getpwnam` and `grp.getgrnam` that used the string representation, caused by invisible characters or trailing whitespaces. William Grzybowski wrote the patch.

[bpo-32922](https://bugs.python.org/issue?@action=redirect&bpo=32922): dbm.open() now encodes the filename via the filesystem encoding instead of the default encoding.

[bpo-33266](https://bugs.python.org/issue?@action=redirect&bpo=33266): lib2to3 now recognizes `rf'...'` strings.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
