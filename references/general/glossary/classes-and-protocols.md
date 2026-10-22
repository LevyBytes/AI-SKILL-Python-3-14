# Classes and protocols

Open when checking Python definitions for classes and protocols.

## class

A blueprint from which user-defined objects are made. The bodies of class definitions usually hold method definitions that act on instances of the class.

## class variable

A variable declared inside a class that is meant to be changed only at the class level (that is, not within an instance of the class).

## method

A function declared within a class body. When invoked as an attribute on an instance of that class, the method receives the instance object as its first argument (conventionally named `self`). See function and nested scope.

## abstract base class

Abstract base classes round out duck-typing by offering a mechanism for declaring interfaces in situations where approaches such as [`hasattr()`](https://docs.python.org/3.14/library/functions.html#hasattr) would feel awkward or be quietly incorrect (consider [magic methods](https://docs.python.org/3.14/reference/datamodel.html#special-lookup), for instance). ABCs bring in virtual subclasses, which are types that do not derive from a class yet are nonetheless treated as members by [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) and [`issubclass()`](https://docs.python.org/3.14/library/functions.html#issubclass); consult the [`abc`](https://docs.python.org/3.14/library/abc.html#module-abc) module documentation. A wide range of built-in ABCs ships with Python: for data structures (within the [`collections.abc`](https://docs.python.org/3.14/library/collections.abc.html#module-collections.abc) module), for numbers (within the [`numbers`](https://docs.python.org/3.14/library/numbers.html#module-numbers) module), for streams (within the [`io`](https://docs.python.org/3.14/library/io.html#module-io) module), and for import finders and loaders (within the [`importlib.abc`](https://docs.python.org/3.14/library/importlib.html#module-importlib.abc) module). The `abc` module also lets you define ABCs of your own.

## duck-typing

A coding approach that ignores an object's type when deciding whether its interface fits; rather, the relevant attribute or method is just used or invoked ("Should something look like a duck and quack like one, then a duck it must be.") Putting interfaces ahead of concrete types lets well-built code gain flexibility through polymorphic substitution. Tests relying on [`type()`](https://docs.python.org/3.14/library/functions.html#type) or [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) are avoided by duck-typing. (Be aware, though, that abstract base classes can supplement duck-typing.) In their place it generally leans on [`hasattr()`](https://docs.python.org/3.14/library/functions.html#hasattr) checks or EAFP-style programming.

## descriptor

Any object that provides the methods [`__get__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__get__), [`__set__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__set__), or [`__delete__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__delete__). Whenever a class attribute is a descriptor, its distinctive binding behavior fires during attribute lookup. Ordinarily, writing *a.b* to read, assign, or remove an attribute searches for the object called *b* within the class dictionary belonging to *a*, but when *b* is a descriptor the matching descriptor method is invoked instead. Grasping descriptors is central to a thorough grasp of Python, since they underpin numerous features, among them functions, methods, properties, class methods, static methods, and references to super classes.

To learn more about the methods of descriptors, see [Implementing Descriptors](https://docs.python.org/3.14/reference/datamodel.html#descriptors) or the [Descriptor How To Guide](https://docs.python.org/3.14/howto/descriptor.html#descriptorhowto).

## metaclass

The class to which a class belongs. A class definition produces a class name, a class dictionary, and a list of base classes. Turning those three inputs into the class is the metaclass's job. A default implementation comes with most object oriented programming languages. Python's distinction is that custom metaclasses can be built. The bulk of users will never reach for this tool, yet when it is needed metaclasses can deliver powerful, elegant solutions. People have applied them to log attribute access, add thread-safety, track object creation, implement singletons, and handle many other jobs.

Further details are available in [Metaclasses](https://docs.python.org/3.14/reference/datamodel.html#metaclasses).

## method resolution order

Method Resolution Order denotes the sequence in which base classes get searched for a member while a lookup runs. Consult [The Python 2.3 Method Resolution Order](https://docs.python.org/3.14/howto/mro.html#python-2-3-mro) for specifics of the algorithm the Python interpreter has used ever since the 2.3 release.

## MRO

See method resolution order.

## new-style class

A bygone label for the kind of classes that every class object now uses. In older Python releases, only new-style classes had access to Python's newer, more flexible features such as [`__slots__`](https://docs.python.org/3.14/reference/datamodel.html#object.__slots__), descriptors, properties, [`__getattribute__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattribute__), class methods, and static methods.

## special method

A method Python invokes implicitly to carry out some operation on a type, addition being one example. The names of such methods open and close with a pair of underscores. Special methods are documented in [Special method names](https://docs.python.org/3.14/reference/datamodel.html#specialnames).

## magic method

A casual synonym for special method.

## dunder

A casual abbreviation standing for "double underscore", invoked when discussing a special method. To illustrate, `__init__` is frequently spoken aloud as "dunder init".

## __slots__

A declaration placed within a class that conserves memory by reserving room for instance attributes ahead of time and doing away with instance dictionaries. For all its popularity, the technique is rather fiddly to apply correctly and is best kept for the uncommon situations where a memory-critical application holds enormous counts of instances.

[Glossary context index](INDEX.md).
