# collections: `collections.OrderedDict`

### `OrderedDict` objects

Ordered dictionaries behave much like ordinary dictionaries, but they carry a few additional powers tied to ordering operations. They matter less these days, given that the built-in [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) class picked up the ability to recall insertion order (a behavior that became guaranteed starting in Python 3.7).

A handful of distinctions from [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) persist:

- The ordinary [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) was built to excel at mapping operations. Keeping track of insertion order came second.

- The `OrderedDict` was built to excel at reordering operations. Space efficiency, iteration speed, and the speed of update operations came second.

- The `OrderedDict` algorithm copes with heavy reordering operations more gracefully than [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict). The recipes further down show why this makes it a good fit for building assorted kinds of LRU caches.

- For `OrderedDict`, the equality operation tests that the order matches too.

On a plain [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict), the order sensitive equality test is reproduced through `p == q and all(k1 == k2 for k1, k2 in zip(p, q))`.

- `OrderedDict`’s `popitem()` method carries a different signature. It takes an optional argument that selects which item gets popped.

On a plain [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict), OrderedDict’s `od.popitem(last=True)` is reproduced by `d.popitem()`, which reliably pops the rightmost (last) item.

On a plain [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict), OrderedDict’s `od.popitem(last=False)` is reproduced by `(k := next(iter(d)), d.pop(k))`, which returns and deletes the leftmost (first) item when one is present.

- `OrderedDict` provides a `move_to_end()` method that efficiently shifts an element to one of the endpoints.

On a plain [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict), OrderedDict’s `od.move_to_end(k, last=True)` is reproduced by `d[k] = d.pop(k)`, which relocates the key together with its value to the rightmost (last) position.

A plain [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) offers no efficient counterpart to OrderedDict’s `od.move_to_end(k, last=False)`, which shifts the key together with its value into the leftmost (first) position.

- Right up to Python 3.8, [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) had no [`__reversed__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__reversed__) method.

 *class *collections.OrderedDict(***kwargs*)

 *class *collections.OrderedDict(*mapping*, */*, ***kwargs*)

 *class *collections.OrderedDict(*iterable*, */*, ***kwargs*)

Hand back an instance of a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) subclass whose methods are tailored for shuffling dictionary order around.

Added in version 3.1.

[Subject index](INDEX.md) · [Previous](somenamedtuple-field-defaults.md) · [Continue](ordereddict-popitem-and-move-to-end.md) · [Owning module, declaration or section: collections](collections-container-datatypes.md)
