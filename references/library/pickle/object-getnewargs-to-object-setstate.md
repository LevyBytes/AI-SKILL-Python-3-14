# pickle: `object.__getnewargs__()`, `object.__getstate__()`, `object.__setstate__()`

Starting with protocol 2, a class that defines the `__getnewargs_ex__()` method can govern the values handed to the [`__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__) method during unpickling. That method has to give back a pair `(args, kwargs)`; here *args* holds a tuple of positional arguments while *kwargs* holds a dictionary of named arguments used in building the object. Both get forwarded to the `__new__()` method when the object is unpickled.

Define this method whenever your class's [`__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__) method needs keyword-only arguments. If that is not the case, defining `__getnewargs__()` is the recommended path for compatibility.

Changed in version 3.6: Protocols 2 and 3 now call `__getnewargs_ex__()`.

 object.__getnewargs__()

This method fulfills a role much like `__getnewargs_ex__()`, but it handles positional arguments only. It has to return a tuple of arguments `args` that will be forwarded to the [`__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__) method during unpickling.

`__getnewargs__()` will not be called if `__getnewargs_ex__()` is defined.

Changed in version 3.6: Prior to Python 3.6, protocols 2 and 3 called `__getnewargs__()` rather than `__getnewargs_ex__()`.

 object.__getstate__()

A class can exert further control over the pickling of its instances by overriding the `__getstate__()` method. It gets called, and whatever object it returns is pickled as the instance's contents in place of a default state. Several situations arise:

- When a class carries neither an instance [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__) nor [`__slots__`](https://docs.python.org/3.14/reference/datamodel.html#object.__slots__), `None` is the default state.

- When a class carries an instance [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__) but no [`__slots__`](https://docs.python.org/3.14/reference/datamodel.html#object.__slots__), `self.__dict__` is the default state.

- For a class with both an instance [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__) and [`__slots__`](https://docs.python.org/3.14/reference/datamodel.html#object.__slots__), the default state is a two-dictionary tuple: `self.__dict__`, together with a dictionary that maps slot names to their slot values. Only the slots that actually hold a value go into that second dictionary.

- For a class that has [`__slots__`](https://docs.python.org/3.14/reference/datamodel.html#object.__slots__) but no instance [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__), the default state is a tuple whose first element is `None` and whose second element is the slot-name-to-slot-value dictionary described in the bullet above.

Changed in version 3.11: A default implementation of the `__getstate__()` method was added to the [`object`](https://docs.python.org/3.14/library/functions.html#object) class.

 object.__setstate__(*state*)

During unpickling, when the class provides `__setstate__()`, it is invoked with the unpickled state. In that situation the state object is not required to be a dictionary. Otherwise the pickled state has to be a dictionary, whose items get assigned to the new instance's dictionary.

Note

When `__reduce__()` yields a state whose value is `None` at pickling time, `__setstate__()` is skipped during unpickling.

See the Handling Stateful Objects section for further detail on putting the `__getstate__()` and `__setstate__()` methods to use.

Note

While an instance is being unpickled, certain methods such as [`__getattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__), [`__getattribute__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattribute__), or [`__setattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__setattr__) may run against it. If those methods depend on some internal invariant holding, the type should set that invariant up in [`__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__), since [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) is not run when an instance is unpickled.

As we will see, pickle does not call the methods above directly. They are in fact part of the copy protocol, which is implemented by the `__reduce__()` special method. The copy protocol offers one consistent interface for fetching the data required to pickle and copy objects. [4]

Implementing `__reduce__()` directly within your classes is powerful but error prone. Because of that, class authors should favor the high-level interface (that is, `__getnewargs_ex__()`, `__getstate__()` and `__setstate__()`) wherever they can. We will, however, illustrate situations in which `__reduce__()` is either the sole choice or yields more efficient pickling, or both.

[Subject index](INDEX.md) · [Continue](object-reduce-to-object-reduce-ex.md) · [Owning module, declaration or section: pickle](pickle-python-object-serialization.md) · [Owning module, declaration or section: Pickling Class Instances](object-getnewargs-ex.md) · [Owning module, declaration or section: object.__getnewargs_ex__](object-getnewargs-ex.md) · [Preceding source contract and version conditions](object-getnewargs-ex.md)
