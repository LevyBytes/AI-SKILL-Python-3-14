# Positional-only names shared with keyword dictionaries

As a last case, look at this definition, where the positional argument `name` could clash with a `**kwds` that includes `name` among its keys:

```python
def foo(name, **kwds):
    return 'name' in kwds

```

No call whatsoever can coax it into returning `True`, since the keyword `'name'` invariably attaches itself to the leading parameter. Take this instance:

```python
>>> foo(1, **{'name': 2})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: foo() got multiple values for argument 'name'
>>>

```

Yet with `/` (positional only arguments) in play it becomes feasible, because that permits `name` to serve as a positional argument while `'name'` lives as a key among the keyword arguments:

```python
>>> def foo(name, /, **kwds):
...     return 'name' in kwds
...
>>> foo(1, **{'name': 2})
True

```

Put differently, you may reuse the labels of positional-only parameters inside `**kwds` and run no risk of ambiguity.

[Subject index](INDEX.md) · [Previous source section](positional-only-and-keyword-only-definitions-and-calls.md) · [Following source section](recap.md) · [Related tutorial example and explanation](positional-only-and-keyword-only-definitions-and-calls.md)
