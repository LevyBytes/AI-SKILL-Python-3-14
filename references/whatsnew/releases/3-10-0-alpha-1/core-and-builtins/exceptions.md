# Python 3.10.0 alpha 1 / core and builtins / exceptions

[bpo-40985](https://bugs.python.org/issue?@action=redirect&bpo=40985): Corrects a defect that left the [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) text blank whenever a file finishes on a line ending in a line continuation character (that is, a backslash). That error text ought to hold the contents of the closing line.

[bpo-41084](https://bugs.python.org/issue?@action=redirect&bpo=41084): Puts a `f-string: ` prefix on the error message whenever an f-string expression being parsed raises a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError).

[bpo-40679](https://bugs.python.org/issue?@action=redirect&bpo=40679): Several [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) messages reporting missing or surplus arguments now carry the function's [qualified name](https://docs.python.org/3.14/glossary.html#term-qualified-name). Dennis Sweeney authored the patch.

[bpo-41654](https://bugs.python.org/issue?@action=redirect&bpo=41654): Closes a crash that struck while tearing down subclasses of [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError). Pablo Galindo contributed the patch.

[bpo-40847](https://bugs.python.org/issue?@action=redirect&bpo=40847): At the tokenizer level, a line holding nothing but a line continuation character was wrongly treated as non-blank; this corrects that. Under the old behavior, the tokenizer emitted more than one `NEWLINE` token for such cases. The legacy parser sidestepped the problem, yet the replacement parser raised a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) on otherwise valid source because of it. To illustrate, a blank line placed right after a line continuation character ended up flagged as a `SyntaxError`.

[bpo-40870](https://bugs.python.org/issue?@action=redirect&bpo=40870): A [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is now raised when validating custom AST’s in which the constants `True`, `False` and `None` appear inside a [`ast.Name`](https://docs.python.org/3.14/library/ast.html#ast.Name) node.

[bpo-38964](https://bugs.python.org/issue?@action=redirect&bpo=38964): If the expression portion of an fstring contains a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError), the filename attribute on that `SyntaxError` is now set properly to the file in which the fstring lives.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
