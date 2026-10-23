# weakref - Finalizer Objects

### Finalizer Objects

The chief upside of reaching for `finalize` is that enrolling a callback becomes easy, with no obligation to hang onto the finalizer object that comes back. For instance

```python
>>> import weakref
>>> class Object:
...     pass
...
>>> kenny = Object()
>>> weakref.finalize(kenny, print, "You killed Kenny!")
<finalize object at ...; for 'Object' at ...>
>>> del kenny
You killed Kenny!

```

You can also invoke the finalizer outright. Even so, the finalizer fires the callback no more than a single time.

```python
>>> def callback(x, y, z):
...     print("CALLBACK")
...     return x + y + z
...
>>> obj = Object()
>>> f = weakref.finalize(obj, callback, 1, 2, z=3)
>>> assert f.alive
>>> assert f() == 6
CALLBACK
>>> assert not f.alive
>>> f()                     # callback not called because finalizer dead
>>> del obj                 # callback not called because finalizer dead

```

To unregister a finalizer, call its `detach()` method. Doing so kills the finalizer and hands back the arguments that were passed to the constructor at creation time.

```python
>>> obj = Object()
>>> f = weakref.finalize(obj, callback, 1, 2, z=3)
>>> f.detach()
(<...Object object ...>, <function callback ...>, (1, 2), {'z': 3})
>>> newobj, func, args, kwargs = _
>>> assert not f.alive
>>> assert newobj is obj
>>> assert func(*args, **kwargs) == 6
CALLBACK

```

So long as you have not set the `atexit` attribute to [`False`](https://docs.python.org/3.14/library/constants.html#False), a still-alive finalizer fires as the program exits. For instance

```pycon
>>> obj = Object()
>>> weakref.finalize(obj, print, "obj dead or exiting")
<finalize object at ...; for 'Object' at ...>
>>> exit()
obj dead or exiting

```

[Subject index](INDEX.md) · [Previous](example.md) · [Continue](comparing-finalizers-with-del-methods.md) · [Owning module, declaration or section: weakref](weakref-ref-class.md)
