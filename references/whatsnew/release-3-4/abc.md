# What's New In Python 3.4 / abc — abc

### Improved Modules

### abc

A new function, [`abc.get_cache_token()`](https://docs.python.org/3.14/library/abc.html#abc.get_cache_token), lets you detect the moment to invalidate caches that depend on shifts in the object graph. (Contributed by ?ukasz Langa in [bpo-16832](https://bugs.python.org/issue?@action=redirect&bpo=16832).)

A new class, [`ABC`](https://docs.python.org/3.14/library/abc.html#abc.ABC), carries [`ABCMeta`](https://docs.python.org/3.14/library/abc.html#abc.ABCMeta) as its metaclass. Subclassing `ABC` yields practically the same outcome as writing `metaclass=abc.ABCMeta`, while being shorter to type and clearer to read. (Contributed by Bruno Dupuis in [bpo-16049](https://bugs.python.org/issue?@action=redirect&bpo=16049).)

[Subject index](INDEX.md) · [Previous source section](tracemalloc.md) · [Next source section](aifc.md) · [Release/subject declaration](release-highlights.md)
