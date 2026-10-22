# all

all(*iterable*, */*)

Hand back `True` when every element of the *iterable* is truthy (and also when the iterable contains nothing). The equivalent logic is:

```python
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

```

[Builtin task index](INDEX.md).
