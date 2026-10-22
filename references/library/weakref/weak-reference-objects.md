# weakref — Weak Reference Objects

### Weak Reference Objects

A weak reference object exposes no methods and no attributes apart from `ref.__callback__`. You retrieve the referent through a weak reference object, provided it is still around, simply by calling it:

```python
>>> import weakref
>>> class Object:
...     pass
...
>>> o = Object()
>>> r = weakref.ref(o)
>>> o2 = r()
>>> o is o2
True

```

Where the referent is gone, calling the reference object hands back [`None`](https://docs.python.org/3.14/library/constants.html#None):

```python
>>> del o, o2
>>> print(r())
None

```

To check that a weak reference object is still live, use the expression `ref() is not None`. As a rule, application code that has to work with a reference object ought to follow this shape:

```python
# r is a weak reference object
o = r()
if o is None:
    # referent has been garbage collected
    print("Object has been deallocated; can't frobnicate.")
else:
    print("Object is still live!")
    o.do_something_useful()

```

Running a distinct “liveness” check beforehand opens up race conditions in threaded applications; some other thread might invalidate a weak reference in the gap before the weak reference is called. The idiom above stays safe whether the application is threaded or single-threaded.

Tailored variants of `ref` objects can be made by subclassing. The `WeakValueDictionary` implementation uses exactly this to trim the memory cost of each entry in the mapping. It is most often useful for binding extra information onto a reference, though it can equally slip in additional processing whenever the referent is fetched.

The following example shows how a `ref` subclass can stash extra information about an object and shape the value handed back when the referent is accessed:

```python
import weakref

class ExtendedRef(weakref.ref):
    def __init__(self, ob, callback=None, /, **annotations):
        super().__init__(ob, callback)
        self.__counter = 0
        for k, v in annotations.items():
            setattr(self, k, v)

    def __call__(self):
        """Return a pair containing the referent and the number of
        times the reference has been called.
        """
        ob = super().__call__()
        if ob is not None:
            self.__counter += 1
            ob = (ob, self.__counter)
        return ob

```

[Subject index](INDEX.md) · [Previous](weakref-proxytypes.md) · [Continue](example.md) · [Owning module, declaration or section: weakref](weakref-ref-class.md)
