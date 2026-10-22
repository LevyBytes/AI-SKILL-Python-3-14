# What’s New In Python 3.8 / gzip — gzip

> (Contributed by Franz Glasner, ??ric Araujo, and Cheryl Sabella in [bpo-2504](https://bugs.python.org/issue?@action=redirect&bpo=2504).)

### gzip

A *mtime* parameter now exists on [`gzip.compress()`](https://docs.python.org/3.14/library/gzip.html#gzip.compress) so output can be reproducible.
> (Contributed by Guo Ci Teo in [bpo-34898](https://bugs.python.org/issue?@action=redirect&bpo=34898).)

For some kinds of broken or corrupt gzip files, a [`BadGzipFile`](https://docs.python.org/3.14/library/gzip.html#gzip.BadGzipFile) exception now surfaces in place of [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

[Subject index](INDEX.md) · [Previous source section](gettext.md) · [Next source section](idle-and-idlelib.md) · [Release/subject declaration](assignment-expressions.md)
