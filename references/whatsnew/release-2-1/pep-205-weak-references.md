# What’s New in Python 2.1 / PEP 205: Weak References — weakref

### PEP 205: Weak References

Weak references, reachable through the [`weakref`](https://docs.python.org/3.14/library/weakref.html#module-weakref) module, are a small yet handy new data type joining the Python programmer’s toolbox.

Holding a reference to an object (in a dictionary or a list, say) carries the side effect of keeping that object alive indefinitely. In a handful of particular situations this behavior is unwanted — object caches are the most frequent case, and circular references inside data structures like trees are another.

Consider, for example, a memoizing function that caches the outcomes of another function `f(x)` by saving the function’s argument together with its result in a dictionary:

```python
_cache = {}
def memoize(x):
    if _cache.has_key(x):
        return _cache[x]

    retval = f(x)

    # Cache the returned object
    _cache[x] = retval

    return retval

```

This implementation handles simple values such as integers, but it brings a side effect along; because the `_cache` dictionary retains a reference to the returned values, they stay un-deallocated right up until the Python process exits and tidies up. With integers that’s barely noticeable, but when `f()` yields an object, or a data structure consuming plenty of memory, it can become a problem.

Weak references give you a way to build a cache that won’t prolong an object’s lifetime past its due. Once an object is reachable solely via weak references, the object gets deallocated and the weak references will then report that the object they pointed at is gone. You make a weak reference to an object *obj* by calling `wr = weakref.ref(obj)`. To get the referenced object back, you call the weak reference as though it were a function: `wr()`. That hands back the referenced object, or `None` when the object has ceased to exist.

This lets you write a `memoize()` function whose cache refrains from keeping objects alive, by holding weak references in the cache instead.

```python
_cache = {}
def memoize(x):
    if _cache.has_key(x):
        obj = _cache[x]()
        # If weak reference object still exists,
        # return it
        if obj is not None: return obj

    retval = f(x)

    # Cache a weak reference
    _cache[x] = weakref.ref(retval)

    return retval

```

The [`weakref`](https://docs.python.org/3.14/library/weakref.html#module-weakref) module further supports creating proxy objects that act like weak references — an object held only by proxy objects gets deallocated — except that, rather than needing an explicit call to fetch the object, the proxy quietly relays every operation through to the object while that object endures. Should the object be deallocated, trying to use a proxy triggers a `weakref.ReferenceError` exception.

```python
proxy = weakref.proxy(obj)
proxy.attr   # Equivalent to obj.attr
proxy.meth() # Equivalent to obj.meth()
del obj
proxy.attr   # raises weakref.ReferenceError

```

See also

[**PEP 205**](https://peps.python.org/pep-0205/) - Weak References

Written and implemented by Fred L. Drake, Jr.

[Subject index](INDEX.md) · [Previous source section](pep-229-new-build-system.md) · [Next source section](pep-232-function-attributes.md) · [Release/subject declaration](introduction.md)
