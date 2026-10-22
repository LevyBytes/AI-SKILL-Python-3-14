# What's New In Python 3.4 / sunau

### sunau

The `getparams()` method now hands back a namedtuple in place of an ordinary plain tuple. (Contributed by Claudiu Popa in [bpo-18901](https://bugs.python.org/issue?@action=redirect&bpo=18901).)

`sunau.open()` now honours the context management protocol: within a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) block, the returned object's `close` method gets invoked on its own once the block ends. (Contributed by Serhiy Storchaka in [bpo-18878](https://bugs.python.org/issue?@action=redirect&bpo=18878).)

`AU_write.setsampwidth()` now copes with 24 bit samples, which lets the module write 24 sample. (Contributed by Serhiy Storchaka in [bpo-19261](https://bugs.python.org/issue?@action=redirect&bpo=19261).)

The `writeframesraw()` and `writeframes()` methods now take any [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object). (Contributed by Serhiy Storchaka in [bpo-8311](https://bugs.python.org/issue?@action=redirect&bpo=8311).)

[Subject index](INDEX.md) · [Previous source section](subprocess.md) · [Next source section](sys.md) · [Release/subject declaration](release-highlights.md)
