# unittest.mock - TEST_PREFIX

### TEST_PREFIX

Each of the patchers can act as a class decorator. Used that way, they wrap every test method belonging to the class. The patchers treat methods whose names begin with `'test'` as test methods — the very same convention that [`unittest.TestLoader`](https://docs.python.org/3.14/library/unittest.html#unittest.TestLoader) uses by default to locate test methods.

You may well want a different prefix for your tests. Communicate the alternate prefix to the patchers by setting `patch.TEST_PREFIX`:

```python
>>> patch.TEST_PREFIX = 'foo'
>>> value = 3
>>>
>>> @patch('__main__.value', 'not three')
... class Thing:
...     def foo_one(self):
...         print(value)
...     def foo_two(self):
...         print(value)
...
>>>
>>> Thing().foo_one()
not three
>>> Thing().foo_two()
not three
>>> value
3

```

[Subject index](INDEX.md) · [Previous](patch-builtins.md) · [Continue](nesting-patch-decorators.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md)
