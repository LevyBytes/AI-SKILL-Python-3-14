# expressions: Generator expression syntax and iteration

### 6.2.9. Generator expressions

*Generator expressions* share the same syntax as list comprehensions, the difference being that parentheses surround them rather than brackets. For instance:

```python
>>> iterator = (x ** 2 for x in range(10))
>>> iterator
<generator object <genexpr> at ...>

```

When run, a generator expression evaluates to a [generator iterator](https://docs.python.org/3.14/glossary.html#term-generator-iterator) that yields the very same values the matching list comprehension would:

```python
>>> list(iterator)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

```

So the example just above is broadly the same as writing and invoking the generator function below:

```python
def make_generator_of_squares(iterator):
    for x in iterator:
        yield x ** 2

make_generator_of_squares(iter(range(10)))

```

You can leave off the surrounding parentheses in a call whenever the generator expression is the sole positional argument and no keyword arguments are present. The Calls section spells out the details. For instance:

```python
# The parentheses after `sum` are part of the call syntax:
>>> sum(x ** 2 for x in range(10))
285

# The generator needs its own parentheses if it's not the only argument:
>>> sum((x ** 2 for x in range(10)), start=1000)
1285

```

Evaluation of the iterable expression in the leftmost `for` clause happens right away, so an error this expression raises surfaces at the spot where the generator expression is defined, instead of at the spot where the first value gets pulled out:

```python
>>> (x ** 2 for x in nonexistent_iterable)
Traceback (most recent call last):
  ...
NameError: name 'nonexistent_iterable' is not defined

```

Once that expression has been evaluated, an iterator is built from the result, just as though [`iter()`](https://docs.python.org/3.14/library/functions.html#iter) had been invoked on it. Should creating the iterator raise any error, it too surfaces straight away:

```python
>>> (x ** 2 for x in None)
Traceback (most recent call last):
  ...
TypeError: 'NoneType' object is not iterable

```

Every other expression is evaluated lazily, the same way ordinary generators handle it (namely, once the iterator is prompted to yield a value):

```python
>>> iterator = (nonexistent_value for x in range(10))
>>> iterator
<generator object <genexpr> at ...>
>>> list(iterator)
Traceback (most recent call last):
  ...
NameError: name 'nonexistent_value' is not defined

```

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Owning language section](atoms.md) · [Previous source section](dictionary-displays.md) · [Following source section](generator-expression-errors-and-yield-restrictions.md)
