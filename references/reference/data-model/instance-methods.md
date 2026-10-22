# 3.2.8.2. Instance methods

#### 3.2.8.2. Instance methods

An instance method object brings together a class, a class instance, and any callable object (ordinarily a user-defined function).

Special read-only attributes:

| method.__self__ | Points to the class instance object the method is bound to |
| --- | --- |
| method.__func__ | Points to the function object it was built from |
| method.__doc__ | The documentation of the method (identical to `method.__func__.__doc__`). A `string` when the originating function carried a docstring, otherwise `None`. |
| method.__name__ | The method’s name (identical to `method.__func__.__name__`) |
| method.__module__ | The name of whatever module the method was defined in, or `None` when there is none. |

In the same way, methods let you read — but not assign — the arbitrary function attributes held on the function object beneath.

A user-defined method object can spring into existence as a class attribute is fetched (perhaps through an instance of that class), as long as the attribute is a user-defined function object or a [`classmethod`](https://docs.python.org/3.14/library/functions.html#classmethod) object.

If an instance method object comes from looking up a user-defined function object on a class through one of that class's instances, then its `__self__` attribute holds the instance and the method is described as *bound*. That new method exposes the original function object through its `__func__` attribute.

If an instance method object comes from looking up a [`classmethod`](https://docs.python.org/3.14/library/functions.html#classmethod) object on a class or one of its instances, then its `__self__` attribute holds the class itself, while its `__func__` attribute holds the function object that backs the class method.

Invoking an instance method object triggers a call to the wrapped function (`__func__`), with the class instance (`__self__`) prepended to the argument list. As an example, if `C` is a class that defines a function `f()`, and `x` names an instance of `C`, then the call `x.f(1)` behaves identically to the call `C.f(x, 1)`.

If an instance method object originates from a [`classmethod`](https://docs.python.org/3.14/library/functions.html#classmethod) object, the "class instance" held in `__self__` is in fact the class itself, meaning that either `x.f(1)` or `C.f(1)` behaves the same as the call `f(C,1)`, in which `f` is the wrapped function.

Note carefully that user-defined functions stored as attributes of a class instance do not become bound methods; the conversion *only* takes place when the function lives as an attribute of the class.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](callable-types.md) · [Previous source section](special-writable-attributes.md) · [Following source section](generator-functions.md)
