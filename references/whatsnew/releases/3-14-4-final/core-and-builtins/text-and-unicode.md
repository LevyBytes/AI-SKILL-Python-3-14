# Python 3.14.4 final / core and builtins / text and unicode

[gh-145234](https://github.com/python/cpython/issues/145234): Resolved a `SystemError` inside the parser that fired whenever an encoding cookie (UTF-7, say) decodes into carriage returns (`\r`). The string tokenizer now normalizes newlines once decoding finishes.

Pablo Galindo wrote the patch.

[gh-140594](https://github.com/python/cpython/issues/140594): Corrects an out of bounds read happening when one lone NUL character is read off the standard input. Shamil Abdulaev supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
