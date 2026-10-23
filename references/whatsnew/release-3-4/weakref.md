# What's New In Python 3.4 / weakref - weakref

### weakref

A new [`WeakMethod`](https://docs.python.org/3.14/library/weakref.html#weakref.WeakMethod) class emulates weak references aimed at bound methods. (Contributed by Antoine Pitrou in [bpo-14631](https://bugs.python.org/issue?@action=redirect&bpo=14631).)

A new [`finalize`](https://docs.python.org/3.14/library/weakref.html#weakref.finalize) class lets you register a callback that fires once an object gets garbage collected, sparing you from hand-managing the lifecycle of the underlying weak reference. (Contributed by Richard Oudkerk in [bpo-15528](https://bugs.python.org/issue?@action=redirect&bpo=15528).)

Any callback tied to a [`ref`](https://docs.python.org/3.14/library/weakref.html#weakref.ref) is from now on reachable through the [`__callback__`](https://docs.python.org/3.14/library/weakref.html#weakref.ref.__callback__) attribute. (Contributed by Mark Dickinson in [bpo-17643](https://bugs.python.org/issue?@action=redirect&bpo=17643).)

[Subject index](INDEX.md) · [Previous source section](wave.md) · [Next source section](xml-etree.md) · [Release/subject declaration](release-highlights.md)
