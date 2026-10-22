# Python 3.9.0 alpha 6 / core and builtins / text and unicode

[bpo-39939](https://bugs.python.org/issue?@action=redirect&bpo=39939): The str.removeprefix and str.removesuffix methods were added, together with matching bytes, bytearray, and collections.UserString methods that strip affixes from a string when they appear. Consult [**PEP 616**](https://peps.python.org/pep-0616/) for the complete account. Dennis Sweeney supplied the patch.

[bpo-40267](https://bugs.python.org/issue?@action=redirect&bpo=40267): Adjust the tokenizer so it shows the right error message whenever a `SyntaxError` lands on the final input character with no trailing newline. The message used to read `unexpected EOF while parsing`, whereas the correct one is `invalid syntax`.

[bpo-39522](https://bugs.python.org/issue?@action=redirect&bpo=39522): Unparse the explicit `u` string prefix correctly once postponed evaluation of annotations is turned on. Batuhan Taskaya supplied the patch.

[bpo-40246](https://bugs.python.org/issue?@action=redirect&bpo=40246): Emit a tailored error message, `invalid string prefix`, whenever the tokenizer meets a string carrying an invalid prefix.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
