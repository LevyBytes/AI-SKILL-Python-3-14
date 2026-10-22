# functools: `functools.lru_cache()`

@functools.lru_cache(*user_function*)

 @functools.lru_cache(*maxsize=128*, *typed=False*)

A decorator that wraps a function in a memoizing callable retaining up to the *maxsize* most recent invocations. It can be a time-saver whenever a costly or I/O bound function gets called repeatedly with identical arguments.

Because the cache is threadsafe, the wrapped function is safe to invoke across several threads. As a result, the backing data structure stays consistent even while several threads update it at once.

There is a possibility that the wrapped function executes a second time if a different thread issues another call before the first one has finished running and been stored.

Given that a dictionary backs the cached results, both the positional and keyword arguments handed to the function have to be [hashable](https://docs.python.org/3.14/glossary.html#term-hashable).

Different argument arrangements might count as different calls holding separate cache entries. As an illustration, `f(a=1, b=2)` and `f(b=2, a=1)` vary in keyword argument ordering and so could occupy two distinct cache entries.

When *user_function* is given, it has to be a callable. That permits applying the *lru_cache* decorator straight to a user function while leaving *maxsize* at its default of 128:

```python
@lru_cache
def count_vowels(sentence):
    return sum(sentence.count(vowel) for vowel in 'AEIOUaeiou')

```

Setting *maxsize* to `None` turns off the LRU behavior, letting the cache expand without limit.

When *typed* is true, arguments of differing types get cached on their own. When *typed* is false, the implementation typically treats them as the same call and retains only one result. (Certain types, such as *str* and *int*, may end up cached separately even with *typed* set to false.)

Keep in mind that type distinctions apply only to the function's direct arguments, not to whatever those arguments contain. The scalar arguments `Decimal(42)` and `Fraction(42)` register as separate calls yielding separate results. Conversely, the tuple arguments `('answer', Decimal(42))` and `('answer', Fraction(42))` are handled as the same.

The wrapped function gains a `cache_parameters()` function that hands back a fresh [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) reporting the current *maxsize* and *typed* values. It exists purely for information. Altering those values does nothing.

So you can gauge how well the cache performs and adjust the *maxsize* parameter, the wrapped function also carries a `cache_info()` function returning a [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple) that reports *hits*, *misses*, *maxsize* and *currsize*.

The decorator further supplies a `cache_clear()` function to empty or invalidate the cache.

You can reach the original underlying function via the `__wrapped__` attribute. That comes in handy for introspection, for sidestepping the cache, or for rewrapping the function with a different cache.

The cache holds onto references to both the arguments and the return values right up until they age out or the cache gets cleared.

When a method is cached, the `self` instance argument forms part of the cache. Refer to [How do I cache method calls?](https://docs.python.org/3.14/faq/programming.html#faq-cache-method-calls)

An [LRU (least recently used) cache](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_(LRU)) performs best when recent calls reliably forecast the calls to come (for instance, the top stories on a news server typically shift day by day). Capping the cache size guarantees it won't expand without limit on long-running processes such as web servers.

As a rule, reach for the LRU cache only when reusing previously computed values is your aim. For that reason, caching makes no sense for functions with side-effects, functions that must produce fresh mutable objects per call (like generators and async functions), or impure functions such as time() or random().

Example of an LRU cache for static web content:

```python
@lru_cache(maxsize=32)
def get_pep(num):
    'Retrieve text of a Python Enhancement Proposal'
    resource = f'https://peps.python.org/pep-{num:04d}'
    try:
        with urllib.request.urlopen(resource) as s:
            return s.read()
    except urllib.error.HTTPError:
        return 'Not Found'

>>> for n in 8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991:
...     pep = get_pep(n)
...     print(n, len(pep))

>>> get_pep.cache_info()
CacheInfo(hits=3, misses=8, maxsize=32, currsize=8)

```

Example of efficiently computing [Fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_number) using a cache to implement a [dynamic programming](https://en.wikipedia.org/wiki/Dynamic_programming) technique:

```python
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

>>> [fib(n) for n in range(16)]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

>>> fib.cache_info()
CacheInfo(hits=28, misses=16, maxsize=None, currsize=16)

```

Added in version 3.2.

Changed in version 3.3: Added the *typed* option.

Changed in version 3.8: Added the *user_function* option.

Changed in version 3.9: Added the function `cache_parameters()`

[Subject index](INDEX.md) · [Previous](functools-cmp-to-key.md) · [Continue](functools-placeholder.md) · [Owning module, declaration or section: functools](cached-factorial-and-dataset-examples.md)
