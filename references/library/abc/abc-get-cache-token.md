# abc: `abc.abstractstaticmethod`, `abc.abstractproperty`, `abc.get_cache_token()`

@abc.abstractstaticmethod

Added in version 3.2.

Deprecated since version 3.3: Since [`staticmethod`](https://docs.python.org/3.14/library/functions.html#staticmethod) can now be paired with `abstractmethod()`, this decorator no longer serves any purpose.

A subclass of the built-in [`staticmethod()`](https://docs.python.org/3.14/library/functions.html#staticmethod) that marks an abstract staticmethod. In every other respect it mirrors `abstractmethod()`.

This special case is on its way out, because the [`staticmethod()`](https://docs.python.org/3.14/library/functions.html#staticmethod) decorator is now properly recognized as abstract once it wraps an abstract method:

```python
class C(ABC):
    @staticmethod
    @abstractmethod
    def my_abstract_staticmethod(arg):
        ...

```

 @abc.abstractproperty

Deprecated since version 3.3: Since [`property`](https://docs.python.org/3.14/library/functions.html#property), [`property.getter()`](https://docs.python.org/3.14/library/functions.html#property.getter), [`property.setter()`](https://docs.python.org/3.14/library/functions.html#property.setter), and [`property.deleter()`](https://docs.python.org/3.14/library/functions.html#property.deleter) can now be paired with `abstractmethod()`, this decorator no longer serves any purpose.

A subclass of the built-in [`property()`](https://docs.python.org/3.14/library/functions.html#property) that marks an abstract property.

This special case is on its way out, because the [`property()`](https://docs.python.org/3.14/library/functions.html#property) decorator is now properly recognized as abstract once it wraps an abstract method:

```python
class C(ABC):
    @property
    @abstractmethod
    def my_abstract_property(self):
        ...

```

That preceding example sets up a read-only property; to get a read-write abstract property instead, flag one or more of the supporting methods as abstract where appropriate:

```python
class C(ABC):
    @property
    def x(self):
        ...

    @x.setter
    @abstractmethod
    def x(self, val):
        ...

```

When just a subset of the components are abstract, a subclass only has to refresh those components to arrive at a concrete property:

```python
class D(C):
    @C.x.setter
    def x(self, val):
        ...

```

The `abc` module additionally gives you these functions:

 abc.get_cache_token()

Hands back the abstract base class cache token in effect right now.

That token is an opaque object (one that permits equality testing) pinpointing the present version of the abstract base class cache used for virtual subclasses. Each `ABCMeta.register()` call on any ABC shifts the token.

Added in version 3.4.

[Subject index](INDEX.md) · [Previous](abc-abstract-base-classes.md) · [Continue](abc-update-abstractmethods.md) · [Owning module, declaration or section: abc](abc-abc-class.md)
