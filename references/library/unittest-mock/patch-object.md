# unittest.mock — patch.object

### patch.object

 patch.object(*target*, *attribute*, *new=DEFAULT*, *spec=None*, *create=False*, *spec_set=None*, *autospec=None*, *new_callable=None*, ***kwargs*)

On an object (*target*), replace the named member (*attribute*) with a mock object.

You may apply `patch.object()` as a decorator, a class decorator, or a context manager. The arguments *new*, *spec*, *create*, *spec_set*, *autospec* and *new_callable* carry the same significance they have for `patch()`. As with `patch()`, `patch.object()` accepts arbitrary keyword arguments to configure the mock object it builds.

Acting as a class decorator, `patch.object()` respects `patch.TEST_PREFIX` when deciding which methods get wrapped.

`patch.object()` accepts either three arguments or two. In the three-argument form you supply the object being patched, the name of the attribute, and the object that should replace that attribute.

In the two-argument form you leave off the replacement object; a mock is then built for you and handed to the decorated function as one more argument:

```python
>>> @patch.object(SomeClass, 'class_method')
... def test(mock_method):
...     SomeClass.class_method(3)
...     mock_method.assert_called_with(3)
...
>>> test()

```

The arguments *spec*, *create*, and the rest passed to `patch.object()` mean exactly what they mean for `patch()`.

[Subject index](INDEX.md) · [Previous](patch.md) · [Continue](patch-dict.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md)
