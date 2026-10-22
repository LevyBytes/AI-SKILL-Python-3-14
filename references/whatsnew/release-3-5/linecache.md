# What’s New In Python 3.5 / linecache — linecache

### linecache

To record details about a module that is not backed by a file, so that its lines can be fetched afterward through [`getline()`](https://docs.python.org/3.14/library/linecache.html#linecache.getline), there is a new [`lazycache()`](https://docs.python.org/3.14/library/linecache.html#linecache.lazycache) function. It defers I/O until some line is genuinely required, sparing you from holding the module globals around forever. (Contributed by Robert Collins in [bpo-17911](https://bugs.python.org/issue?@action=redirect&bpo=17911).)

[Subject index](INDEX.md) · [Previous source section](json.md) · [Next source section](locale.md) · [Release/subject declaration](summary-release-highlights.md)
