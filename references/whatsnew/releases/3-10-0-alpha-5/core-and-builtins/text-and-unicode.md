# Python 3.10.0 alpha 5 / core and builtins / text and unicode

[bpo-27772](https://bugs.python.org/issue?@action=redirect&bpo=27772): During string formatting, putting `'0'` in front of the *width* field no longer changes the default alignment used for strings.

[bpo-42986](https://bugs.python.org/issue?@action=redirect&bpo=42986): A parser crash that hit when flagging syntax errors in an f-string containing newlines is fixed. Pablo Galindo contributed the patch.

[bpo-40176](https://bugs.python.org/issue?@action=redirect&bpo=40176): For an unterminated string literal, the syntax error now indicates where the string begins rather than naming EOF/EOL.

[bpo-42924](https://bugs.python.org/issue?@action=redirect&bpo=42924): Repair `bytearray` repetition that wrongly pulled data from the buffer's beginning even when the data sat offset inside the buffer (for instance, after a slice at the start of the `bytearray` was reassigned to a shorter byte string).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
