# Methods

### Methods

A method is a function invoked through attribute notation. They come in two kinds: [built-in methods](https://docs.python.org/3.14/reference/datamodel.html#builtin-methods) (for example `append()` on lists) and [class instance method](https://docs.python.org/3.14/reference/datamodel.html#instance-methods). Built-in methods are documented alongside whatever types provide them.

Reaching a method (a function declared in a class namespace) by way of an instance hands you a special object: a *bound method* (also termed an [instance method](https://docs.python.org/3.14/reference/datamodel.html#instance-methods)) object. On being called, it prepends the `self` argument to the argument list. A bound method carries two special read-only attributes: [`m.__self__`](https://docs.python.org/3.14/reference/datamodel.html#method.__self__) is the object the method acts upon, while [`m.__func__`](https://docs.python.org/3.14/reference/datamodel.html#method.__func__) is the function that implements the method. The call `m(arg-1, arg-2, ..., arg-n)` is wholly the same as the call `m.__func__(m.__self__, arg-1, arg-2, ..., arg-n)`.

As with [function objects](https://docs.python.org/3.14/reference/datamodel.html#user-defined-funcs), a bound method object lets you read arbitrary attributes. But because method attributes actually reside on the function object underneath ([`method.__func__`](https://docs.python.org/3.14/reference/datamodel.html#method.__func__)), assigning method attributes on bound methods is forbidden. Trying to set an attribute on a method causes an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) to be raised. To assign a method attribute, you have to set it directly on the function object beneath it:

```pycon
>>> class C:
...     def method(self):
...         pass
...
>>> c = C()
>>> c.method.whoami = 'my name is method'  # can't set on the method
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'method' object has no attribute 'whoami'
>>> c.method.__func__.whoami = 'my name is method'
>>> c.method.whoami
'my name is method'

```

For further detail, consult [Instance methods](https://docs.python.org/3.14/reference/datamodel.html#instance-methods).

[Subject index](INDEX.md) · [Previous](functions.md) · [Continue](code-objects.md)
