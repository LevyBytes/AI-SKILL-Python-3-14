# Why are default values shared between objects?

### Why are default values shared between objects?

This kind of bug frequently trips up beginning programmers. Take this function:

```python
def foo(mydict={}):  # Danger: shared reference to one dict for all calls
    ... compute something ...
    mydict[key] = value
    return mydict

```

On the first call to this function, `mydict` holds a single item. On the second call, `mydict` holds two items, because at the moment `foo()` starts running, `mydict` already begins with an item in it.

People often assume a function call produces new objects for its default values. That isn't the case. Default values come into being precisely once, at the time the function is defined. Should that object be mutated, as the dictionary in this example is, later calls to the function will point at this same altered object.

By their nature, immutable objects such as numbers, strings, tuples, and `None`, can't change. Mutating mutable objects like dictionaries, lists, and class instances can produce confusion.

Given this behavior, it's good programming practice to avoid mutable objects as default values. Instead, set the default to `None`, and within the function check whether the parameter is `None` and build a fresh list/dictionary/whatever when it is. For instance, rather than writing:

```python
def foo(mydict={}):
    ...

```

but:

```python
def foo(mydict=None):
    if mydict is None:
        mydict = {}  # create a new dict for local namespace

```

This behavior can come in handy. With a function that takes a long time to compute, one common approach is to cache each call's parameters along with its resulting value and hand back the cached value whenever the same value is asked for again. This goes by the name "memoizing", and you can implement it this way:

```python
# Callers can only provide two parameters and optionally pass _cache by keyword
def expensive(arg1, arg2, *, _cache={}):
    if (arg1, arg2) in _cache:
        return _cache[(arg1, arg2)]

    # Calculate the value
    result = ... expensive computation ...
    _cache[(arg1, arg2)] = result           # Store result in the cache
    return result

```

In place of the default value you could keep a global variable holding a dictionary; which one you pick is a question of taste.

[Subject index](INDEX.md)
