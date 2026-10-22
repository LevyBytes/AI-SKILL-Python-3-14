# What's New In Python 3.4 / aifc

### aifc

The `getparams()` method hands back a namedtuple now instead of an ordinary tuple. (Contributed by Claudiu Popa in [bpo-17818](https://bugs.python.org/issue?@action=redirect&bpo=17818).)

`aifc.open()` has gained support for the context management protocol: inside a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) block, the returned object's `close()` method fires on its own once the block ends. (Contributed by Serhiy Storchacha in [bpo-16486](https://bugs.python.org/issue?@action=redirect&bpo=16486).)

The `writeframesraw()` and `writeframes()` methods will now take any [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object). (Contributed by Serhiy Storchaka in [bpo-8311](https://bugs.python.org/issue?@action=redirect&bpo=8311).)

[Subject index](INDEX.md) · [Previous source section](abc.md) · [Next source section](argparse.md) · [Release/subject declaration](release-highlights.md)
