# multiprocessing: Remote shared-object proxy behavior

### Proxy Objects

A proxy is an object that *refers* to a shared object living (presumably) inside a different process. That shared object is termed the *referent* of the proxy. Several proxy objects can share one referent.

A proxy object carries methods that call the matching methods on its referent (though not every method of the referent is guaranteed to be reachable through the proxy). This way, a proxy can stand in for its referent:

```pycon
>>> mp_context = multiprocessing.get_context('spawn')
>>> manager = mp_context.Manager()
>>> l = manager.list([i*i for i in range(10)])
>>> print(l)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> print(repr(l))
<ListProxy object, typeid 'list' at 0x...>
>>> l[4]
16
>>> l[2:5]
[4, 9, 16]

```

Observe that applying [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) to a proxy hands back the referent's representation, whereas applying [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) hands back the proxy's representation.

A notable trait of proxy objects is that they are picklable, so you can pass them between processes. By the same token, a referent is free to hold Proxy Objects. This lets these managed lists, dicts, and other Proxy Objects nest within one another:

```pycon
>>> a = manager.list()
>>> b = manager.list()
>>> a.append(b)         # referent of a now contains referent of b
>>> print(a, b)
[<ListProxy object, typeid 'list' at ...>] []
>>> b.append('hello')
>>> print(a[0], b)
['hello'] ['hello']

```

In the same way, dict and list proxies can be nested one inside another:

```python
>>> l_outer = manager.list([ manager.dict() for i in range(2) ])
>>> d_first_inner = l_outer[0]
>>> d_first_inner['a'] = 1
>>> d_first_inner['b'] = 2
>>> l_outer[1]['c'] = 3
>>> l_outer[1]['z'] = 26
>>> print(l_outer[0])
{'a': 1, 'b': 2}
>>> print(l_outer[1])
{'c': 3, 'z': 26}

```

When ordinary (non-proxy) [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) or [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) objects sit inside a referent, edits to those mutable values will not travel through the manager, since the proxy has no way to tell when the values held within get changed. Storing a value into a container proxy (which fires a `__setitem__` on the proxy object) does, however, travel through the manager, so to edit such an item effectively you can re-assign the changed value back onto the container proxy:

```python
# create a list proxy and append a mutable object (a dictionary)
lproxy = manager.list()
lproxy.append({})
# now mutate the dictionary
d = lproxy[0]
d['a'] = 1
d['b'] = 2
# at this point, the changes to d are not yet synced, but by
# updating the dictionary, the proxy is notified of the change
lproxy[0] = d

```

For most use cases this route is arguably less handy than relying on nested Proxy Objects, yet it also shows off a degree of control over the synchronization.

Note

The proxy types in `multiprocessing` make no effort to support comparisons by value. So, for example, we get:

```pycon
>>> manager.list([1,2,3]) == [1,2,3]
False

```

When making comparisons, you should just work with a copy of the referent instead.

[Subject index](INDEX.md) · [Previous](using-a-remote-manager.md) · [Continue](manager-proxy-contract.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md)
