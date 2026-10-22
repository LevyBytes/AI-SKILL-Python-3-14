# Why does a_tuple[i] += [‘item’] raise an exception when the addition works?

### Why does a_tuple[i] += [‘item’] raise an exception when the addition works?

The cause lies in two things coming together: the fact that augmented assignment operators are *assignment* operators, and the distinction between mutable and immutable objects in Python.

The point holds broadly whenever augmented assignment operators are applied to elements of a tuple that reference mutable objects, but we’ll take a `list` and `+=` as our example.

Suppose you wrote:

```python
>>> a_tuple = (1, 2)
>>> a_tuple[0] += 1
Traceback (most recent call last):
   ...
TypeError: 'tuple' object does not support item assignment

```

Why the exception arises should be plain at once: `1` is added to the object that `a_tuple[0]` references (`1`), yielding the result object, `2`, but when we go to assign that computed result, `2`, to element `0` of the tuple, an error appears because we can’t alter what a tuple element references.

Beneath the surface, what this augmented assignment statement carries out is roughly this:

```python
>>> result = a_tuple[0] + 1
>>> a_tuple[0] = result
Traceback (most recent call last):
  ...
TypeError: 'tuple' object does not support item assignment

```


The error comes from the assignment half of the operation, because a tuple cannot be changed.

Consider code such as this:

```python
>>> a_tuple = (['foo'], 'bar')
>>> a_tuple[0] += ['item']
Traceback (most recent call last):
  ...
TypeError: 'tuple' object does not support item assignment

```

What makes this puzzling is that, despite the raised error, the append still went through:

```python
>>> a_tuple[0]
['foo', 'item']

```

Understanding this rests on two facts: (a) when an object defines an [`__iadd__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__iadd__) magic method, that method runs whenever the `+=` augmented assignment fires, and whatever it returns is then placed into the assignment target; and (b) on a list, `__iadd__()` amounts to invoking [`extend()`](https://docs.python.org/3.14/library/stdtypes.html#sequence.extend) on that list and handing the list back. This is the reason we describe `+=` on lists as a “shorthand” for [`list.extend()`](https://docs.python.org/3.14/library/stdtypes.html#list.extend):

```python
>>> a_list = []
>>> a_list += [1]
>>> a_list
[1]

```

This is equivalent to:

```python
>>> result = a_list.__iadd__([1])
>>> a_list = result

```

Whatever a_list referred to has now been mutated, and the reference to that mutated object is stored back into `a_list`. Storing it back accomplishes nothing visible, because the reference already names the very object that `a_list` previously held, yet the assignment is still performed.

So, applying that to the tuple case, the behaviour matches this:

```python
>>> result = a_tuple[0].__iadd__(['item'])
>>> a_tuple[0] = result
Traceback (most recent call last):
  ...
TypeError: 'tuple' object does not support item assignment

```

The call to `__iadd__()` works and the list grows as a result, yet although `result` names the identical object that `a_tuple[0]` already names, writing that value back fails, because you cannot modify a tuple.

[Subject index](INDEX.md)
