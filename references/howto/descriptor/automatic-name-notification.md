# Automatic name notification

### Automatic name notification

There are occasions when a descriptor benefits from learning the class variable name to which it was bound. As each new class comes into being, the [`type`](https://docs.python.org/3.14/library/functions.html#type) metaclass walks through the dictionary of that new class. Whenever any entry is a descriptor that also defines [`__set_name__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__set_name__), that method gets invoked with a pair of arguments. The *owner* names the class in which the descriptor lives, while the *name* identifies the class variable to which the descriptor was bound.

You can find the implementation in `type_new()` and `set_names()` over in [Objects/typeobject.c](https://github.com/python/cpython/tree/3.14/Objects/typeobject.c).

Because that update logic lives inside `type.__new__()`, the notifications fire solely when the class is created. Should descriptors be attached to the class later on, you will have to invoke [`__set_name__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__set_name__) yourself.

[Subject index](INDEX.md) · [Descriptor invocation logic summary](descriptor-invocation-logic-summary.md) · [Following source context](descriptor-invocation-logic-summary.md) · [Previous source context](descriptor-invocation-logic-summary.md) · [Following source context](orm-example.md)
