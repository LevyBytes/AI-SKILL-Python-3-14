# Python 3.11.0 alpha 7 / core and builtins / text and unicode

[bpo-47182](https://bugs.python.org/issue?@action=redirect&bpo=47182): Resolve a crash that struck when a named unicode character such as `"\N{digit nine}"` was used once the main interpreter had been brought up for a second time.

[bpo-47129](https://bugs.python.org/issue?@action=redirect&bpo=47129): Sharpen the wording of f-string syntax errors that involve empty expressions.

[bpo-47117](https://bugs.python.org/issue?@action=redirect&bpo=47117): Address a crash arising when character decoding fails in interactive mode while the tokenizer buffers remain uninitialized. Pablo Galindo wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
