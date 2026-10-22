# What’s New In Python 3.5 / difflib — difflib

### difflib

The charset on HTML documents that [`HtmlDiff.make_file()`](https://docs.python.org/3.14/library/difflib.html#difflib.HtmlDiff.make_file) produces can henceforth be tailored through a fresh *charset* keyword-only argument. The default charset for an HTML document shifted from `"ISO-8859-1"` over to `"utf-8"`. (Contributed by Berker Peksag in [bpo-2052](https://bugs.python.org/issue?@action=redirect&bpo=2052).)

The [`diff_bytes()`](https://docs.python.org/3.14/library/difflib.html#difflib.diff_bytes) function henceforth compares lists made of byte strings. This repairs a regression carried over from Python 2. (Contributed by Terry J. Reedy and Greg Ward in [bpo-17445](https://bugs.python.org/issue?@action=redirect&bpo=17445).)

[Subject index](INDEX.md) · [Previous source section](dbm.md) · [Next source section](distutils.md) · [Release/subject declaration](summary-release-highlights.md)
