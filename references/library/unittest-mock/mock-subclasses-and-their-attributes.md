# unittest.mock — Mock subclasses and their attributes

### Mock subclasses and their attributes

Subclassing [`Mock`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock) can be motivated by a handful of reasons. Tacking on helper methods is one such motive. Here is a trivial illustration:

```python
>>> class MyMock(MagicMock):
...     def has_been_called(self):
...         return self.called
...
>>> mymock = MyMock(return_value=None)
>>> mymock
<MyMock id='...'>
>>> mymock.has_been_called()
False
>>> mymock()
>>> mymock.has_been_called()
True

```

By default, `Mock` instances make their attributes and return value mocks share the same type as the mock from which they are accessed. That guarantees `Mock` attributes come out as `Mocks` and `MagicMock` attributes come out as `MagicMocks` [2]. Consequently, if your subclass exists to add helper methods, those helpers turn up on the attributes and return value mock of your subclass's instances as well.

```python
>>> mymock.foo
<MyMock name='mock.foo' id='...'>
>>> mymock.foo.has_been_called()
False
>>> mymock.foo()
<MyMock name='mock.foo()' id='...'>
>>> mymock.foo.has_been_called()
True

```

In some cases that proves awkward. As an example, [one user](https://code.google.com/archive/p/mock/issues/105) subclasses mock to build a [Twisted adaptor](https://twisted.org/documents/11.0.0/api/twisted.python.components.html). Propagating it onto the attributes as well genuinely triggers errors.

Across all of its variants, `Mock` leans on a method named `_get_child_mock` to spin up these "sub-mocks" for attributes and return values. To keep your subclass from being applied to attributes, override that method. Its signature accepts arbitrary keyword arguments (`**kwargs`), which it then forwards into the mock constructor:

```python
>>> class Subclass(MagicMock):
...     def _get_child_mock(self, /, **kwargs):
...         return MagicMock(**kwargs)
...
>>> mymock = Subclass()
>>> mymock.foo
<MagicMock name='mock.foo' id='...'>
>>> assert isinstance(mymock, Subclass)
>>> assert not isinstance(mymock.foo, Subclass)
>>> assert not isinstance(mymock(), Subclass)

```

[Subject index](INDEX.md) · [Previous](mocking-a-dictionary-with-magicmock.md) · [Continue](mocking-imports-with-patch-dict.md) · [Owning module, declaration or section: unittest.mock](mock-patching-methods.md)
