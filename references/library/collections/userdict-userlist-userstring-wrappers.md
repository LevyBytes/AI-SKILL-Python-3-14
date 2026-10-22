# UserDict, UserList and UserString wrapper classes

`*class *collections.UserDict(*iterable*, */*, ***kwargs*)`

A class that mimics the behavior of a dictionary. Whatever the instance holds lives inside an ordinary dictionary, which you reach through the `data` attribute on any `UserDict` instance. Any arguments you pass go toward initializing `data`, just as they would for a plain dictionary.

Beyond offering the usual mapping methods and operations, every `UserDict` instance also exposes this attribute:

 data

An actual dictionary that holds whatever the `UserDict` class is keeping.

### `UserList` objects

This one serves as a wrapper sitting around list objects. It makes a handy base from which to derive your own list-like classes, letting them inherit and then either replace the inherited methods or tack on fresh ones. That is how you give lists additional behaviors.

Much of the reason for this class has faded now that you can subclass [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) outright; even so, it can prove simpler to deal with, since the list it wraps is reachable as an attribute.

 `*class *collections.UserList([*list*])`

A class that mimics a list. Its instance contents live in an ordinary list, reachable through the `data` attribute on `UserList` instances. At the start, that content is a copy of *list*, which defaults to the empty list `[]`. The value of *list* may be any iterable — for instance an actual Python list or another `UserList` object.

On top of the standard mutable-sequence methods and operations, each `UserList` instance also offers this attribute:

 data

An honest [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) object that keeps whatever the `UserList` class is holding.

**Subclassing requirements:** Any subclass of `UserList` ought to provide a constructor that accepts being called with no argument or with exactly one. Whenever a list operation yields a new sequence, it tries to build an instance of the concrete implementation class. In doing that, it presumes the constructor will accept a lone parameter — namely a sequence object serving as the data source.

Should a derived class prefer not to follow this convention, it must override every one of the special methods this class supports; in that situation, consult the source code to learn which methods you need to supply.

### `UserString` objects

The `UserString` class wraps itself around string objects. As with the others, the case for it has weakened now that subclassing [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) directly is possible; it can still be the gentler option to work with, because the wrapped string is exposed as an attribute.

 `*class *collections.UserString(*seq*)`

A class that mimics a string object. The content of each instance resides in an ordinary string object, reachable through the `data` attribute on `UserString` instances. That content begins life as a copy of *seq*. You may give *seq* any object at all, provided it can be turned into a string by the built-in [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) function.

Alongside the ordinary string methods and operations, every `UserString` instance further provides this attribute:

 data

A genuine [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) object that holds whatever the `UserString` class is keeping.

Changed in version 3.5: New methods `__getnewargs__`, `__rmod__`, `casefold`, `format_map`, `isprintable`, and `maketrans`.

[Subject index](INDEX.md)
