# operator: `operator.call()`, `operator.__call__()`, `operator.attrgetter()`

`operator.call(*obj*, */*, **args*, ***kwargs*)`

 `operator.__call__(*obj*, */*, **args*, ***kwargs*)`

Return `obj(*args, **kwargs)`.

Added in version 3.11.

Beyond those, the `operator` module supplies helpers for general-purpose attribute and item lookups. They come in handy when you need quick field extractors to pass to [`map()`](https://docs.python.org/3.14/library/functions.html#map), [`sorted()`](https://docs.python.org/3.14/library/functions.html#sorted), [`itertools.groupby()`](https://docs.python.org/3.14/library/itertools.html#itertools.groupby), or anything else that takes a function argument.

 `operator.attrgetter(*attr*)`

 `operator.attrgetter(**attrs*)`

Produce a callable that pulls *attr* out of whatever operand it's given. Ask for several attributes and you get back a tuple of them. Dots are allowed inside the attribute names as well. As an illustration:

- After `f = attrgetter('name')`, the call `f(b)` returns `b.name`.

- After `f = attrgetter('name', 'date')`, the call `f(b)` returns `(b.name, b.date)`.

- After `f = attrgetter('name.first', 'name.last')`, the call `f(b)` returns `(b.name.first, b.name.last)`.

Equivalent to:

```python
def attrgetter(*items):
    if any(not isinstance(item, str) for item in items):
        raise TypeError('attribute name must be a string')
    if len(items) == 1:
        attr = items[0]
        def g(obj):
            return resolve_attr(obj, attr)
    else:
        def g(obj):
            return tuple(resolve_attr(obj, attr) for attr in items)
    return g

def resolve_attr(obj, attr):
    for name in attr.split("."):
        obj = getattr(obj, name)
    return obj

```

[Subject index](INDEX.md) · [Previous](operator-pow-to-operator-length-hint.md) · [Continue](operator-itemgetter-to-operator-methodcaller.md) · [Owning module, declaration or section: operator](operator-lt-to-operator-abs.md)
