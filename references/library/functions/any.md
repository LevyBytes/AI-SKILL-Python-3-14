# any

any(*iterable*, */*)

Hand back `True` whenever at least one element of the *iterable* is truthy. Should the iterable hold nothing, give back `False`. The equivalent logic is:

```python
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

```

[Builtin task index](INDEX.md).
