# When can I rely on identity tests with the *is* operator?

### When can I rely on identity tests with the *is* operator?

The `is` operator checks for object identity. The expression `a is b` corresponds to `id(a) == id(b)`.

An identity test’s key feature is that any object is always identical to itself, so `a is a` always evaluates to `True`. Such tests tend to run faster than equality checks. And in contrast to equality checks, identity tests are promised to hand back a boolean `True` or `False`.

That said, identity tests are *only* a valid stand-in for equality tests when object identity is certain. As a rule, identity is certain in three situations:

1.

Assignment makes new names without altering object identity. Once you run `new = old`, `new is old` is guaranteed to hold.

2.

Placing an object into a container that holds object references leaves object identity untouched. Once the list assignment `s[0] = x` runs, `s[0] is x` is guaranteed.

3.

When an object is a singleton, only a single instance of it is allowed to exist. Once you run `a = None` and `b = None`, `a is b` is guaranteed because `None` is a singleton.

For nearly every other case, identity tests are unwise and equality tests are the better choice. Specifically, you shouldn’t lean on identity tests to compare against constants like [`int`](https://docs.python.org/3.14/library/functions.html#int) and [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), which carry no guarantee of being singletons:

```python
>>> a = 10_000_000
>>> b = 5_000_000
>>> c = b + 5_000_000
>>> a is c
False

>>> a = 'Python'
>>> b = 'Py'
>>> c = b + 'thon'
>>> a is c
False

```

In the same way, freshly built mutable containers are never identical:

```python
>>> a = []
>>> b = []
>>> a is b
False

```

Throughout the standard library code, a few recurring patterns show identity tests used the right way:

1.

Per the advice in [**PEP 8**](https://peps.python.org/pep-0008/), an identity test is the favored means of checking for `None`. It reads almost like ordinary English in the source and steers clear of mix-ups with other objects whose boolean value evaluates as false.

2.

Spotting optional arguments gets tricky once `None` counts as a legitimate input value. For such cases, you can build a singleton sentinel object that is certain to differ from every other object. As an example, here’s one way to write a method that acts like [`dict.pop()`](https://docs.python.org/3.14/library/stdtypes.html#dict.pop):

```python
_sentinel = object()

def pop(self, key, default=_sentinel):
    if key in self:
        value = self[key]
        del self[key]
        return value
    if default is _sentinel:
        raise KeyError(key)
    return default

```

3.

Container implementations occasionally have to back up equality tests with identity tests. Doing so keeps the code from getting tripped up by objects like `float('NaN')`, which are not equal to themselves.

To illustrate, here’s how `collections.abc.Sequence.__contains__()` is implemented:

```python
def __contains__(self, value):
    for v in self:
        if v is value or v == value:
            return True
    return False

```

[Subject index](INDEX.md)
