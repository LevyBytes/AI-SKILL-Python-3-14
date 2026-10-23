# What's New In Python 3.3 / collections - collections, collections.abc

### collections

A new [`ChainMap`](https://docs.python.org/3.14/library/collections.html#collections.ChainMap) class was added so several mappings can be handled together as one. (Written by Raymond Hettinger for [bpo-11089](https://bugs.python.org/issue?@action=redirect&bpo=11089), made public in [bpo-11297](https://bugs.python.org/issue?@action=redirect&bpo=11297).)

To draw a sharper line between the abstract collection classes and the concrete ones, the abstract base classes were relocated into a new [`collections.abc`](https://docs.python.org/3.14/library/collections.abc.html#module-collections.abc) module. So existing imports keep working, the [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) module still carries aliases for those ABCs. ([bpo-11085](https://bugs.python.org/issue?@action=redirect&bpo=11085))

Backing for the unary `+` and `-` operators, plus the in-place operators `+=`, `-=`, `|=`, and `&=`, has arrived in the [`Counter`](https://docs.python.org/3.14/library/collections.html#collections.Counter) class. (Contributed by Raymond Hettinger in [bpo-13121](https://bugs.python.org/issue?@action=redirect&bpo=13121).)

[Subject index](INDEX.md) · [Previous source section](codecs.md) · [Next source section](contextlib.md) · [Release/subject declaration](summary-release-highlights.md)
