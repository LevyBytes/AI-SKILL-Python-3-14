# abc: `abc.abstractmethod`, `abc.abstractclassmethod`

@abc.abstractmethod

A decorator that flags methods as abstract.

For this decorator to work, the class's metaclass must be `ABCMeta` or something derived from it. A class whose metaclass descends from `ABCMeta` cannot be instantiated until every one of its abstract methods and properties has been overridden. Those abstract methods stay callable through any of the usual ‘super’ call mechanisms. `abstractmethod()` is also fit for declaring abstract methods on properties and descriptors.

Tacking abstract methods onto a class on the fly, or trying to change a method's or class's abstraction status after creation, works only via the `update_abstractmethods()` function. `abstractmethod()` reaches only subclasses formed through ordinary inheritance; the “virtual subclasses” enrolled through the ABC's `register()` method go untouched.

Where `abstractmethod()` is combined with other method descriptors, place it as the innermost decorator, as the usage examples below show:

```python
class C(ABC):
    @abstractmethod
    def my_abstract_method(self, arg1):
        ...
    @classmethod
    @abstractmethod
    def my_abstract_classmethod(cls, arg2):
        ...
    @staticmethod
    @abstractmethod
    def my_abstract_staticmethod(arg3):
        ...

    @property
    @abstractmethod
    def my_abstract_property(self):
        ...
    @my_abstract_property.setter
    @abstractmethod
    def my_abstract_property(self, val):
        ...

    @abstractmethod
    def _get_x(self):
        ...
    @abstractmethod
    def _set_x(self, val):
        ...
    x = property(_get_x, _set_x)

```

For a descriptor to cooperate properly with the abstract base class machinery, it has to flag itself abstract through `__isabstractmethod__`. As a rule, that attribute should read `True` whenever any of the methods making up the descriptor are abstract. Python's built-in [`property`](https://docs.python.org/3.14/library/functions.html#property), for one, does the equivalent of:

```python
class Descriptor:
    ...
    @property
    def __isabstractmethod__(self):
        return any(getattr(f, '__isabstractmethod__', False) for
                   f in (self._fget, self._fset, self._fdel))

```

Note

In contrast to Java's abstract methods, these may carry an implementation. The class that overrides such a method can still invoke that implementation through the [`super()`](https://docs.python.org/3.14/library/functions.html#super) mechanism. That can come in handy as the terminating point of a super-call inside a framework built on cooperative multiple-inheritance.

The `abc` module additionally supports these legacy decorators:

 @abc.abstractclassmethod

Added in version 3.2.

Deprecated since version 3.3: Since [`classmethod`](https://docs.python.org/3.14/library/functions.html#classmethod) can now be paired with `abstractmethod()`, this decorator no longer serves any purpose.

A subclass of the built-in [`classmethod()`](https://docs.python.org/3.14/library/functions.html#classmethod) that marks an abstract classmethod. In every other respect it mirrors `abstractmethod()`.

This special case is on its way out, because the [`classmethod()`](https://docs.python.org/3.14/library/functions.html#classmethod) decorator is now properly recognized as abstract once it wraps an abstract method:

```python
class C(ABC):
    @classmethod
    @abstractmethod
    def my_abstract_classmethod(cls, arg):
        ...

```

[Subject index](INDEX.md) · [Previous](abc-abcmeta-class-to-abc-abcmeta-subclasshook.md) · [Continue](abc-get-cache-token.md) · [Owning module, declaration or section: abc](abc-abc-class.md)
