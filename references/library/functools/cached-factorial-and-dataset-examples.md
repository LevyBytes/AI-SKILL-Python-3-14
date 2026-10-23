# functools: `functools.cache()`, `functools.cached_property()`

### `functools` - Higher-order functions and operations on callable objects

**Source code:** [Lib/functools.py](https://github.com/python/cpython/tree/3.14/Lib/functools.py)

---

Higher-order functions — those that take other functions as input or hand them back as output — are what the `functools` module provides. For this module's purposes, treat any callable object as if it were a function.

These are the functions exported by the `functools` module:

 @functools.cache(*user_function*)

A minimal, lightweight unbounded cache for function results. The technique is sometimes referred to as ["memoize"](https://en.wikipedia.org/wiki/Memoization).

The return value matches `lru_cache(maxsize=None)`, wrapping a dictionary lookup keyed on the function's arguments in a thin layer. Since stale entries are never discarded, it stays leaner and quicker than a bounded `lru_cache()`.

For example:

```python
@cache
def factorial(n):
    return n * factorial(n-1) if n else 1

>>> factorial(10)   # no previously cached result, makes 11 recursive calls
3628800
>>> factorial(5)    # no new calls, just returns the cached result
120
>>> factorial(12)   # two new recursive calls, factorial(10) is cached
479001600

```

Because the cache is threadsafe, the wrapped function is safe to invoke across several threads. As a result, the backing data structure stays consistent even while several threads update it at once.

There is a possibility that the wrapped function executes a second time if a different thread issues another call before the first one has finished running and been stored.

Added in version 3.9.

 @functools.cached_property(*func*)

Convert a class method into a property whose value is calculated a single time, then stored as an ordinary attribute that persists for the instance's lifetime. It resembles [`property()`](https://docs.python.org/3.14/library/functions.html#property), but adds caching on top. Handy for costly computed properties on instances that are otherwise effectively immutable.

Example:

```python
class DataSet:

    def __init__(self, sequence_of_numbers):
        self._data = tuple(sequence_of_numbers)

    @cached_property
    def stdev(self):
        return statistics.stdev(self._data)

```

How `cached_property()` operates differs in some respects from [`property()`](https://docs.python.org/3.14/library/functions.html#property). An ordinary property refuses attribute writes when no setter has been defined. A *cached_property*, by contrast, permits writes.

A *cached_property* decorator activates solely during lookups, and only when no attribute of that name is already present. Once it activates, the *cached_property* stores a value under that same attribute name. From then on, reading or writing that attribute overrides the *cached_property* method, behaving like an ordinary attribute.

Deleting the attribute clears the stored value. After that, the *cached_property* method is free to execute once more.

A *cached_property* offers no protection against a possible race condition under multi-threaded use. The getter could fire more than one time against a single instance, and whichever run finishes last establishes the cached value. Provided the cached property is idempotent — or at least harmless when executed repeatedly on one instance — that's acceptable. When you do require synchronization, add the appropriate locking either within the decorated getter or surrounding access to the cached property.

Be aware that this decorator disrupts how [**PEP 412**](https://peps.python.org/pep-0412/) key-sharing dictionaries function. Consequently, the per-instance dictionaries may consume more memory than they otherwise would.

This decorator further depends on every instance's `__dict__` attribute being a mutable mapping. As such, certain types won't work with it — metaclasses, for instance (since, on type instances, the `__dict__` attribute is a read-only proxy onto the class namespace), along with classes that declare `__slots__` but omit `__dict__` from their slot list (since those classes expose no `__dict__` attribute whatsoever).

When no mutable mapping exists, or when you'd rather have space-efficient key sharing, you can approximate `cached_property()` by layering [`property()`](https://docs.python.org/3.14/library/functions.html#property) over `lru_cache()`. Consult [How do I cache method calls?](https://docs.python.org/3.14/faq/programming.html#faq-cache-method-calls) to learn how that approach diverges from `cached_property()`.

Added in version 3.8.

Changed in version 3.12: Before Python 3.12, `cached_property` carried an undocumented lock that guaranteed, in multi-threaded use, the getter ran a single time per instance. That lock, however, was scoped per-property rather than per-instance, which could produce unacceptably high lock contention. From Python 3.12 onward, this locking has been dropped.

[Subject index](INDEX.md) · [Continue](functools-cmp-to-key.md)
