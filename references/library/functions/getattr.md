# getattr

getattr(*object*, *name*, */*)

 getattr(*object*, *name*, *default*, */*)

Return the value of the named attribute of *object*. *name* has to be a string. When the string names one of the object's attributes, the result is that attribute's value. As an example, `getattr(x, 'foobar')` matches `x.foobar`. When the named attribute is absent, *default* comes back if it was supplied, and otherwise [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) is raised. *name* does not have to be a Python identifier (see `setattr()`).

Note

Because [private name mangling](https://docs.python.org/3.14/reference/expressions.html#private-name-mangling) takes place at compilation time, you have to mangle a private attribute's name (attributes carrying two leading underscores) by hand so that `getattr()` can fetch it.

[Builtin task index](INDEX.md).
