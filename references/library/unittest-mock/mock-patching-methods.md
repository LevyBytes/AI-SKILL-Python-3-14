# unittest.mock - Mock patching methods

<a id="unittestmock--unittestmock--getting-started"></a>

getting started: Added in version 3.3.

### Using Mock

### Mock patching methods

Typical scenarios where [`Mock`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock) objects help include:

- Patching methods

- Recording method calls on objects

Suppose you'd like to swap out a method on an object so you can confirm that some other part of the system invokes it with the right arguments:

```python
>>> real = SomeClass()
>>> real.method = MagicMock(name='method')
>>> real.method(3, 4, 5, key='value')
<MagicMock name='method()' id='...'>

```

After our mock has been exercised (`real.method` here) it exposes methods and attributes that let you assert how it was used.

Note

Across most of these snippets the [`Mock`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock) and [`MagicMock`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.MagicMock) classes can stand in for one another. Because `MagicMock` is the richer of the two, it serves well as the default choice.

After the mock gets called, its [`called`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.called) attribute becomes `True`. More to the point, the [`assert_called_with()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.assert_called_with) or [`assert_called_once_with()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.assert_called_once_with) method lets us verify it received the arguments we expected.

Here is a test confirming that invoking `ProductionClass().method` triggers a call to the `something` method:

```python
>>> class ProductionClass:
...     def method(self):
...         self.something(1, 2, 3)
...     def something(self, a, b, c):
...         pass
...
>>> real = ProductionClass()
>>> real.something = MagicMock()
>>> real.method()
>>> real.something.assert_called_once_with(1, 2, 3)

```

[Subject index](INDEX.md) · [Continue](mock-for-method-calls-on-an-object.md)
