# What's New In Python 3.3 / abc — abc

### Improved Modules

### abc

Better handling now exists for abstract base classes that hold descriptors built together with abstract methods. Declaring abstract descriptors is now best done by supplying `__isabstractmethod__` as a property that updates dynamically. The built-in descriptors were revised to match.

- Now that [`abc.abstractproperty`](https://docs.python.org/3.14/library/abc.html#abc.abstractproperty) is deprecated, reach instead for [`property`](https://docs.python.org/3.14/library/functions.html#property) paired with [`abc.abstractmethod()`](https://docs.python.org/3.14/library/abc.html#abc.abstractmethod).

- Since [`abc.abstractclassmethod`](https://docs.python.org/3.14/library/abc.html#abc.abstractclassmethod) is deprecated, prefer [`classmethod`](https://docs.python.org/3.14/library/functions.html#classmethod) combined with [`abc.abstractmethod()`](https://docs.python.org/3.14/library/abc.html#abc.abstractmethod) instead.

- With [`abc.abstractstaticmethod`](https://docs.python.org/3.14/library/abc.html#abc.abstractstaticmethod) now deprecated, opt for [`staticmethod`](https://docs.python.org/3.14/library/functions.html#staticmethod) together with [`abc.abstractmethod()`](https://docs.python.org/3.14/library/abc.html#abc.abstractmethod) in its place.

(Contributed by Darren Dale in [bpo-11610](https://bugs.python.org/issue?@action=redirect&bpo=11610).)

Because [`abc.ABCMeta.register()`](https://docs.python.org/3.14/library/abc.html#abc.ABCMeta.register) hands back the subclass it registered, you are now able to apply it as a class decorator ([bpo-10868](https://bugs.python.org/issue?@action=redirect&bpo=10868)).

[Subject index](INDEX.md) · [Previous source section](lzma.md) · [Next source section](array.md) · [Release/subject declaration](summary-release-highlights.md)
