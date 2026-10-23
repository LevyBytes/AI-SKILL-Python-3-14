# unittest.mock - Mocking a generator method

For a different take on mocking dates and similar builtin classes, see the techniques laid out in [this blog entry](https://williambert.online/2011/07/how-to-unit-testing-in-django-with-mocking-and-patching/).

### Mocking a generator method

In Python, a generator is a function or method that relies on the [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) statement to hand back a sequence of values as it is iterated [1].

Calling such a function or method produces the generator object, and that object is what gets iterated. Since [`__iter__()`](https://docs.python.org/3.14/library/stdtypes.html#container.__iter__) is the protocol method driving iteration, we can stand in for it with a [`MagicMock`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.MagicMock).

Below is a sample class whose "iter" method is written as a generator:

```python
>>> class Foo:
...     def iter(self):
...         for i in [1, 2, 3]:
...             yield i
...
>>> foo = Foo()
>>> list(foo.iter())
[1, 2, 3]

```

So how do we go about mocking this class, and especially its "iter" method?

Setting the values that the iteration yields (which the call to [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) triggers implicitly) means configuring whatever the `foo.iter()` call hands back.

```python
>>> mock_foo = MagicMock()
>>> mock_foo.iter.return_value = iter([1, 2, 3])
>>> list(mock_foo.iter())
[1, 2, 3]

```

[Subject index](INDEX.md) · [Continue](applying-the-same-patch-to-every-test-method.md) · [Owning module, declaration or section: unittest.mock](mock-patching-methods.md) · [Owning module, declaration or section: Partial mocking](partial-mocking.md)
