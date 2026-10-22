# Python 3.7.0 alpha 1 / core and builtins / text and unicode

[bpo-27222](https://bugs.python.org/issue?@action=redirect&bpo=27222): Tidy up the redundant code inside the long_rshift function. Thanks Oren Milman.

- The bundled internal unicode databases were upgraded to Unicode version 9.0.0.

[bpo-30682](https://bugs.python.org/issue?@action=redirect&bpo=30682): An overly strict assertion that broke on certain f-strings, like eval("f'\n'") and eval("f'\r'"), was removed.

[bpo-29104](https://bugs.python.org/issue?@action=redirect&bpo=29104): Backslash parsing within f-strings was fixed.

[bpo-24821](https://bugs.python.org/issue?@action=redirect&bpo=24821): A 25x slowdown when searching for certain unlucky Unicode characters was fixed.

[bpo-29568](https://bugs.python.org/issue?@action=redirect&bpo=29568): An escaped percent "%%" within a classic string formatting format string no longer permits any characters to sit between the two percents.

[bpo-28774](https://bugs.python.org/issue?@action=redirect&bpo=28774): Correct the reported error position for the unicode error produced by the ASCII and Latin1 encoders whenever the string handed back by the error handler holds several non-encodable characters (non-ASCII for the ASCII codec, or characters falling outside the U+0000-U+00FF range for Latin1).

[bpo-28596](https://bugs.python.org/issue?@action=redirect&bpo=28596): On Android the preferred encoding is UTF-8. Chi Hsuan Yen wrote the patch.

[bpo-28739](https://bugs.python.org/issue?@action=redirect&bpo=28739): f-string expressions are no longer treated as docstrings nor accepted by ast.literal_eval(), even when they contain no expressions.

[bpo-31291](https://bugs.python.org/issue?@action=redirect&bpo=31291): On Windows, an assertion failure inside `zipimport.zipimporter.get_data` was fixed for the case where `pathname.replace('/','\\')` produces something other than a string. Oren Milman provided the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
