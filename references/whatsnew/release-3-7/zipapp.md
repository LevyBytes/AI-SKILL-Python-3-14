# What's New In Python 3.7 / zipapp — zipapp

### zipapp

So the caller can choose which files land in the archive, the [`create_archive()`](https://docs.python.org/3.14/library/zipapp.html#zipapp.create_archive) function now takes an optional *filter* argument. (Contributed by Irmen de Jong in [bpo-31072](https://bugs.python.org/issue?@action=redirect&bpo=31072).)

To produce a compressed archive, the [`create_archive()`](https://docs.python.org/3.14/library/zipapp.html#zipapp.create_archive) function now takes an optional *compressed* argument. A `--compress` command line option was likewise introduced to enable compression. (Contributed by Zhiming Wang in [bpo-31638](https://bugs.python.org/issue?@action=redirect&bpo=31638).)

[Subject index](INDEX.md) · [Previous source section](xmlrpc-server.md) · [Next source section](zipfile.md) · [Release/subject declaration](summary-release-highlights.md)
