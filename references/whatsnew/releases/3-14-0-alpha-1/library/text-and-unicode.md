# Python 3.14.0 alpha 1 / library / text and unicode

[gh-124969](https://github.com/python/cpython/issues/124969): Corrects `locale.nl_langinfo(locale.ALT_DIGITS)`. The call now hands back a tuple holding up to 100 strings (and an empty tuple under most locales). Earlier it gave back just that tuple's leading entry, or else an empty string.

[gh-90102](https://github.com/python/cpython/issues/90102): During open(), the `isatty` system call is bypassed whenever the file is already known to be something other than a character device. Reading entire files gets a small speed gain from this.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
