# What's New In Python 3.6 / collections - collections, collections.abc

### collections

A fresh [`Collection`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Collection) abstract base class now represents container classes that are both sized and iterable. (Contributed by Ivan Levkivskyi, with documentation from Neil Girdhar in [bpo-27598](https://bugs.python.org/issue?@action=redirect&bpo=27598).)

A fresh [`Reversible`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Reversible) abstract base class stands for iterable classes that additionally supply the [`__reversed__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__reversed__) method. (Contributed by Ivan Levkivskyi in [bpo-25987](https://bugs.python.org/issue?@action=redirect&bpo=25987).)

A fresh [`AsyncGenerator`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.AsyncGenerator) abstract base class stands for asynchronous generators. (Contributed by Yury Selivanov in [bpo-28720](https://bugs.python.org/issue?@action=redirect&bpo=28720).)

The [`namedtuple()`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple) function has gained an optional keyword argument *module*; supplying it sets the [`__module__`](https://docs.python.org/3.14/reference/datamodel.html#type.__module__) attribute on the named tuple class that comes back. (Contributed by Raymond Hettinger in [bpo-17941](https://bugs.python.org/issue?@action=redirect&bpo=17941).)

The *verbose* together with *rename* parameters of [`namedtuple()`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple) are keyword-only from now on. (Contributed by Raymond Hettinger in [bpo-25628](https://bugs.python.org/issue?@action=redirect&bpo=25628).)

You can now pickle recursive [`collections.deque`](https://docs.python.org/3.14/library/collections.html#collections.deque) instances. (Contributed by Serhiy Storchaka in [bpo-26482](https://bugs.python.org/issue?@action=redirect&bpo=26482).)

[Subject index](INDEX.md) · [Previous source section](cmath.md) · [Next source section](concurrent-futures.md) · [Release/subject declaration](summary-release-highlights.md)
