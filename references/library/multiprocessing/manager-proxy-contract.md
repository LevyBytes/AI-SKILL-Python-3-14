# multiprocessing / Proxy Objects: `multiprocessing.managers.BaseProxy`, `_callmethod()`, `_getvalue()`, `__repr__()`, `__str__()`

*class *multiprocessing.managers.BaseProxy

Proxy objects are instances of subclasses of `BaseProxy`.

 _callmethod(*methodname*[, *args*[, *kwds*]])

Call a method on the proxy's referent and hand back its result.

When `proxy` is a proxy whose referent is `obj`, the expression

```python
proxy._callmethod(methodname, args, kwds)

```

will evaluate the expression

```python
getattr(obj, methodname)(*args, **kwds)

```

in the manager’s process.

What comes back is either a copy of the call's result or a proxy onto a freshly made shared object – consult the documentation covering the *method_to_typeid* argument of `BaseManager.register()`.

When the call raises an exception, `_callmethod()` re-raises it. When some other exception arises inside the manager's process, it gets turned into a `RemoteError` exception and raised by `_callmethod()`.

Note especially that an exception arises when *methodname* has not been *exposed*.

An example of the usage of `_callmethod()`:

```pycon
>>> l = manager.list(range(10))
>>> l._callmethod('__len__')
10
>>> l._callmethod('__getitem__', (slice(2, 7),)) # equivalent to l[2:7]
[2, 3, 4, 5, 6]
>>> l._callmethod('__getitem__', (20,))          # equivalent to l[20]
Traceback (most recent call last):
...
IndexError: list index out of range

```

 _getvalue()

Hand back a copy of the referent.

Should the referent be unpicklable, this will raise an exception.

 __repr__()

Hand back a representation of the proxy object.

 __str__()

Hand back the referent's representation.

[Subject index](INDEX.md) · [Previous](proxy-objects.md) · [Continue](cleanup.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md) · [Owning module, declaration or section: Proxy Objects](proxy-objects.md)
