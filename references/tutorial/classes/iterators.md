# 9.8. Iterators

### 9.8. Iterators

You’ve likely seen by this point that a [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) statement can iterate over the bulk of container objects:

```python
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')

```

This way of reaching elements is plain, compact, and handy. Iterators run all through Python and tie it together. Out of sight, the [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) statement invokes [`iter()`](https://docs.python.org/3.14/library/functions.html#iter) on the container object. What it gets back is an iterator object carrying a [`__next__()`](https://docs.python.org/3.14/library/stdtypes.html#iterator.__next__) method that yields the container’s elements one by one. Once nothing remains, `__next__()` throws a [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) exception, signaling the `for` loop to stop. The `__next__()` method can be driven by hand through the [`next()`](https://docs.python.org/3.14/library/functions.html#next) built-in function; the example below lays out the whole mechanism:

```python
>>> s = 'abc'
>>> it = iter(s)
>>> it
<str_iterator object at 0x10c90e650>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
StopIteration

```

With the workings of the iterator protocol now in view, giving your own classes iterator behavior is straightforward. Write an [`__iter__()`](https://docs.python.org/3.14/library/stdtypes.html#container.__iter__) method that hands back an object owning a [`__next__()`](https://docs.python.org/3.14/library/stdtypes.html#iterator.__next__) method. When the class already supplies `__next__()`, then `__iter__()` need only return `self`:

```python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

```

```python
>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x00A1DB50>
>>> for char in rev:
...     print(char)
...
m
a
p
s

```

[Subject index](INDEX.md) · [Previous source section](odds-and-ends.md) · [Following source section](generators.md)
