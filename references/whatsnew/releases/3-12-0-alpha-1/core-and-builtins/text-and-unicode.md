# Python 3.12.0 alpha 1 / core and builtins / text and unicode

[gh-96611](https://github.com/python/cpython/issues/96611): A file holding invalid UTF-8 inside a multi-line string now yields a correct SyntaxError when loaded.

[gh-96268](https://github.com/python/cpython/issues/96268): Loading a file holding invalid UTF-8 now flags the broken character at its proper location.

[gh-93418](https://github.com/python/cpython/issues/93418): Fixed an assert triggered when an f-string carries an equal sign "=" after an expression yet lacks a closing brace. As an example, `f'{i='`.

[gh-93283](https://github.com/python/cpython/issues/93283): Sharpens the error message when an f-string expression has an invalid conversion character syntax.

[gh-98354](https://github.com/python/cpython/issues/98354): A unicode check was added for the `name` attribute of the `spec` argument handed to the `_imp.create_builtin()` function.

[gh-94360](https://github.com/python/cpython/issues/94360): Resolved a tokenizer crash that hit when encoded files containing syntax errors were read from `stdin` using non utf-8 encoded text. Pablo Galindo wrote the patch

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
