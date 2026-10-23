# unittest.mock - ANY

### ANY

 unittest.mock.ANY

There are times when you want to assert against *some* of the arguments passed in a call to a mock, while not caring about the rest — or while extracting them one at a time from `call_args` for richer assertions of your own.

To skip over particular arguments, hand in objects that test equal to *anything*. Then `assert_called_with()` and `assert_called_once_with()` will pass regardless of the actual values supplied.

```python
>>> mock = Mock(return_value=None)
>>> mock('foo', bar=object())
>>> mock.assert_called_once_with('foo', bar=ANY)

```

You may likewise apply `ANY` when comparing against call lists such as `mock_calls`:

```python
>>> m = MagicMock(return_value=None)
>>> m(1)
>>> m(1, 2)
>>> m(object())
>>> m.mock_calls == [call(1), call(1, 2), ANY]
True

```

Comparisons with call objects aren't the only home for `ANY`; it fits within test assertions too:

```python
class TestStringMethods(unittest.TestCase):

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', ANY])

```

[Subject index](INDEX.md) · [Previous](unittest-mock-create-autospec.md) · [Continue](unittest-mock-filter-dir.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md)
