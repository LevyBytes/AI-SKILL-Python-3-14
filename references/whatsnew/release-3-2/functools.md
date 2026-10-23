# What's New In Python 3.2 / functools - functools

### functools

- A fresh decorator for caching function calls has been added to the [`functools`](https://docs.python.org/3.14/library/functools.html#module-functools) module. [`functools.lru_cache()`](https://docs.python.org/3.14/library/functools.html#functools.lru_cache) can spare you repeated trips to an external resource any time the answers are expected to stay identical.

As an illustration, attaching a caching decorator onto a database query function can spare database hits for frequently requested searches:

```python
>>> import functools
>>> @functools.lru_cache(maxsize=300)
... def get_phone_number(name):
...     c = conn.cursor()
...     c.execute('SELECT phonenumber FROM phonelist WHERE name=?', (name,))
...     return c.fetchone()[0]

```

```python
>>> for name in user_requests:
...     get_phone_number(name)        # cached lookup

```

So that picking a workable cache size is easier, the wrapped function carries instrumentation for tracking cache statistics:

```python
>>> get_phone_number.cache_info()
CacheInfo(hits=4805, misses=980, maxsize=300, currsize=300)

```

Should the phonelist table be updated, the stale cache contents can be flushed with:

```python
>>> get_phone_number.cache_clear()

```

(Built by Raymond Hettinger, who folded in design ideas drawn from Jim Baker, plus Miki Tebeka and also Nick Coghlan; see [recipe 498245](https://code.activestate.com/recipes/498245-lru-and-lfu-cache-decorators/), [recipe 577479](https://code.activestate.com/recipes/577479-simple-caching-decorator/), [bpo-10586](https://bugs.python.org/issue?@action=redirect&bpo=10586), and [bpo-10593](https://bugs.python.org/issue?@action=redirect&bpo=10593).)

- The [`functools.wraps()`](https://docs.python.org/3.14/library/functools.html#functools.wraps) decorator now attaches a `__wrapped__` attribute that points at the original callable function. That lets wrapped functions be introspected. It additionally copies [`__annotations__`](https://docs.python.org/3.14/reference/datamodel.html#function.__annotations__) when those are present. And it now also steps gracefully past absent attributes like [`__doc__`](https://docs.python.org/3.14/reference/datamodel.html#function.__doc__), which the wrapped callable might lack.

For the example above, you can drop the cache by getting back the original function:

```python
>>> get_phone_number = get_phone_number.__wrapped__    # uncached function

```

(By Nick Coghlan and Terrence Cole; [bpo-9567](https://bugs.python.org/issue?@action=redirect&bpo=9567), [bpo-3445](https://bugs.python.org/issue?@action=redirect&bpo=3445), and [bpo-8814](https://bugs.python.org/issue?@action=redirect&bpo=8814).)

- As an aid to writing classes that carry rich comparison methods, a fresh decorator [`functools.total_ordering()`](https://docs.python.org/3.14/library/functools.html#functools.total_ordering) leans on the equality and inequality methods you already have to supply the rest.

As an example, providing *__eq__* alongside *__lt__* lets [`total_ordering()`](https://docs.python.org/3.14/library/functools.html#functools.total_ordering) supply *__le__*, *__gt__* and *__ge__*:

```python
@total_ordering
class Student:
    def __eq__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))

    def __lt__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))

```

When the *total_ordering* decorator is applied, the leftover comparison methods get supplied for you automatically.

(Contributed by Raymond Hettinger.)

- As a help when porting programs across from Python 2, the [`functools.cmp_to_key()`](https://docs.python.org/3.14/library/functools.html#functools.cmp_to_key) function turns a legacy-style comparison function into a modern [key function](https://docs.python.org/3.14/glossary.html#term-key-function):

```python
>>> # locale-aware sort order
>>> sorted(iterable, key=cmp_to_key(locale.strcoll))

```

To see sorting examples plus a short sorting walkthrough, refer to the [Sorting HowTo](https://wiki.python.org/moin/HowTo/Sorting/) tutorial.

(Contributed by Raymond Hettinger.)

[Subject index](INDEX.md) · [Previous source section](elementtree.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md) · [Next source section](itertools.md)
