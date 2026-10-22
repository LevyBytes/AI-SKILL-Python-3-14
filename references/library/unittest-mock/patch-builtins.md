# unittest.mock — patch builtins

### patch builtins

Any builtins inside a module are patchable. This example patches the builtin [`ord()`](https://docs.python.org/3.14/library/functions.html#ord):

```python
>>> @patch('__main__.ord')
... def test(mock_ord):
...     mock_ord.return_value = 101
...     print(ord('c'))
...
>>> test()
101

```

[Subject index](INDEX.md) · [Previous](patch-stopall.md) · [Continue](test-prefix.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md)
