# Matching custom objects in mock call assertions

Imagine that a mock is going to receive an object whose equality, by default, rests on object identity — the behavior Python applies to user-defined classes out of the box. Calling [`assert_called_with()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.assert_called_with) would then demand the very same object be handed over. When only a subset of the object's attributes actually concern us, the answer is to build a matcher that inspects exactly those attributes on our behalf.

The example below shows why an ordinary `assert_called_with` call falls short:

```python
>>> class Foo:
...     def __init__(self, a, b):
...         self.a, self.b = a, b
...
>>> mock = Mock(return_value=None)
>>> mock(Foo(1, 2))
>>> mock.assert_called_with(Foo(1, 2))
Traceback (most recent call last):
    ...
AssertionError: expected call not found.
Expected: mock(<__main__.Foo object at 0x...>)
Actual: mock(<__main__.Foo object at 0x...>)

```

Here is roughly how a comparison function for our `Foo` class could be written:

```python
>>> def compare(self, other):
...     if not type(self) == type(other):
...         return False
...     if self.a != other.a:
...         return False
...     if self.b != other.b:
...         return False
...     return True
...

```

And a matcher object that leans on comparison functions of this sort to drive its equality check might be shaped roughly as follows:

```python
>>> class Matcher:
...     def __init__(self, compare, some_obj):
...         self.compare = compare
...         self.some_obj = some_obj
...     def __eq__(self, other):
...         return self.compare(self.some_obj, other)
...

```

Bringing every piece together:

```python
>>> match_foo = Matcher(compare, Foo(1, 2))
>>> mock.assert_called_with(match_foo)

```

We build the `Matcher` by handing it our compare function alongside the `Foo` object that serves as the target for comparison. Inside `assert_called_with`, the equality method of the `Matcher` fires, weighing the object the mock actually received against the one baked into our matcher. A match lets `assert_called_with` succeed; a mismatch instead triggers an [`AssertionError`](https://docs.python.org/3.14/library/exceptions.html#AssertionError):

```python
>>> match_wrong = Matcher(compare, Foo(3, 4))
>>> mock.assert_called_with(match_wrong)
Traceback (most recent call last):
    ...
AssertionError: Expected: ((<Matcher object at 0x...>,), {})
Called with: ((<Foo object at 0x...>,), {})

```

A little adjustment would let the comparison function raise the [`AssertionError`](https://docs.python.org/3.14/library/exceptions.html#AssertionError) itself and hand back a more informative failure message.

Starting with version 1.5, the Python testing library [PyHamcrest](https://pyhamcrest.readthedocs.io/) offers comparable capability that could serve well in this scenario, by way of its equality matcher ([hamcrest.library.integration.match_equality](https://pyhamcrest.readthedocs.io/en/release-1.8/integration/#module-hamcrest.library.integration.match_equality)).

[Subject index](INDEX.md)
