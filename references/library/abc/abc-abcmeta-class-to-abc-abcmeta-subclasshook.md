# abc / Abstract Base Classes: `abc.ABCMeta`, `register()`, `__subclasshook__()`

*class *abc.ABCMeta

The metaclass used to declare Abstract Base Classes (ABCs).

Reach for this metaclass to fashion an ABC. You can subclass an ABC straight away, at which point it behaves as a mix-in class. You may additionally register unrelated concrete classes (built-in ones included) and unrelated ABCs as “virtual subclasses” – from then on the built-in [`issubclass()`](https://docs.python.org/3.14/library/functions.html#issubclass) function treats them and their descendants as subclasses of the registering ABC, yet that ABC never appears in their MRO (Method Resolution Order), and the method implementations the registering ABC defines are not callable (not even through [`super()`](https://docs.python.org/3.14/library/functions.html#super)). [1]

A class built with `ABCMeta` as its metaclass carries the following method:

 register(*subclass*)

Enroll *subclass* as a “virtual subclass” of this ABC. For example:

```python
from abc import ABC

class MyABC(ABC):
    pass

MyABC.register(tuple)

assert issubclass(tuple, MyABC)
assert isinstance((), MyABC)

```

Changed in version 3.3: Hands back the registered subclass, so it can serve as a class decorator.

Changed in version 3.4: To notice when `register()` is called, lean on the `get_cache_token()` function.

You are also free to override this method inside an abstract base class:

 __subclasshook__(*subclass*)

(It has to be declared as a class method.)

Determine whether *subclass* counts as a subclass of this ABC. This lets you shape [`issubclass()`](https://docs.python.org/3.14/library/functions.html#issubclass)'s behavior beyond the defaults without having to call `register()` on every single class you wish to treat as a subclass of the ABC. (The ABC's [`__subclasscheck__()`](https://docs.python.org/3.14/reference/datamodel.html#type.__subclasscheck__) method is what calls this class method.)

It ought to hand back `True`, `False`, or [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented). A `True` result means *subclass* is taken as a subclass of this ABC. A `False` result means *subclass* is not taken as a subclass of this ABC, even where it ordinarily would be. A `NotImplemented` result lets the subclass check fall back to the standard machinery.

To see these ideas in action, study this sample ABC definition:

```python
class Foo:
    def __getitem__(self, index):
        ...
    def __len__(self):
        ...
    def get_iterator(self):
        return iter(self)

class MyIterable(ABC):

    @abstractmethod
    def __iter__(self):
        while False:
            yield None

    def get_iterator(self):
        return self.__iter__()

    @classmethod
    def __subclasshook__(cls, C):
        if cls is MyIterable:
            if any("__iter__" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented

MyIterable.register(Foo)

```

The `MyIterable` ABC lays out the customary iterable method, [`__iter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__iter__), marking it abstract. Even so, the implementation shown here remains callable from subclasses. The `get_iterator()` method belongs to the `MyIterable` abstract base class as well, though non-abstract derived classes need not override it.

The `__subclasshook__()` class method written here declares that any class carrying an [`__iter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__iter__) method within its [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__) (or within that of one of its base classes, reached through the [`__mro__`](https://docs.python.org/3.14/reference/datamodel.html#type.__mro__) list) counts as a `MyIterable` too.

At last, the closing line turns `Foo` into a virtual subclass of `MyIterable`, despite `Foo` declaring no [`__iter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__iter__) method (it relies on the old-style iterable protocol, spelled out via [`__len__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__len__) and [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__)). Keep in mind this does not give `Foo` a `get_iterator` method, which is why that one is supplied on its own.

The `abc` module additionally hands you this decorator:

[Subject index](INDEX.md) · [Previous](abc-abc-class.md) · [Continue](abc-abstract-base-classes.md) · [Owning module, declaration or section: abc](abc-abc-class.md)
