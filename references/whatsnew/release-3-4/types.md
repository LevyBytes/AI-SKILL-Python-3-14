# What's New In Python 3.4 / types - enum, types

### types

A new [`DynamicClassAttribute()`](https://docs.python.org/3.14/library/types.html#types.DynamicClassAttribute) descriptor offers a means to declare an attribute that behaves normally on lookup via an instance object, yet gets diverted to the *class* `__getattr__` on lookup via the class. That permits keeping properties live on a class while also exposing virtual attributes carrying the same name on the class (consult [`enum`](https://docs.python.org/3.14/library/enum.html#module-enum) for an illustration). (Contributed by Ethan Furman in [bpo-19030](https://bugs.python.org/issue?@action=redirect&bpo=19030).)

[Subject index](INDEX.md) · [Previous source section](traceback.md) · [Next source section](urllib.md) · [Release/subject declaration](release-highlights.md)
