# Descriptor protocol

### Descriptor protocol

`descr.__get__(self, obj, type=None)`

`descr.__set__(self, obj, value)`

`descr.__delete__(self, obj)`

That really is the whole of it. Implement any one of these methods and the object becomes a descriptor, able to supersede default behavior when it is looked up as an attribute.

When an object implements [`__set__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__set__) or [`__delete__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__delete__), it counts as a data descriptor. A descriptor implementing only [`__get__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__get__) is termed a non-data descriptor (frequently used for methods, though other applications exist).

The distinction between data and non-data descriptors lies in how their overrides interact with entries in an instance’s dictionary. When an instance’s dictionary contains an entry sharing a name with a data descriptor, the data descriptor wins. When an instance’s dictionary contains an entry sharing a name with a non-data descriptor, the dictionary entry wins.

For a read-only data descriptor, supply both [`__get__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__get__) and [`__set__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__set__), having `__set__()` raise an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) whenever it is called. Providing the `__set__()` method as an exception-raising stub suffices to qualify it as a data descriptor.

[Subject index](INDEX.md) · [Previous source context](definition-and-introduction.md) · [Following source context](overview-of-descriptor-invocation.md)
