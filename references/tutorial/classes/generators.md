# 9.9. Generators

### 9.9. Generators

[Generators](https://docs.python.org/3.14/glossary.html#term-generator) give you a straightforward yet potent way to build iterators. You author them just like ordinary functions, except they reach for the [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) statement each time they want to emit data. On every [`next()`](https://docs.python.org/3.14/library/functions.html#next) call, the generator picks up exactly where it stopped (it retains all its data values plus the statement it ran last). The following example demonstrates how trivially generators can be put together:

```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

```

```python
>>> for char in reverse('golf'):
...     print(char)
...
f
l
o
g

```

Whatever you can accomplish with generators is equally achievable through the class-based iterators covered in the prior section. The reason generators stay so terse is that their [`__iter__()`](https://docs.python.org/3.14/library/stdtypes.html#iterator.__iter__) and [`__next__()`](https://docs.python.org/3.14/reference/expressions.html#generator.__next__) methods come into being for free.

A second crucial trait is that local variables and execution state are preserved on their own from one call to the next. That made the function simpler to write and far clearer than leaning on instance variables such as `self.index` and `self.data`.

Beyond automatic method creation and the saving of program state, generators raise [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) by themselves when they finish. Taken together, these traits let you build iterators with no more work than writing an ordinary function.

[Subject index](INDEX.md) · [Previous source section](iterators.md) · [Following source section](generator-expressions.md)
