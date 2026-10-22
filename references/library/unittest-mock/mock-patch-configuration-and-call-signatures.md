# unittest.mock — Mock and patch keyword configuration and callable spec signatures

You can configure the return value and side effect of child mocks the same way, through dotted notation. Since dotted names can't be supplied directly inside a call, build a dictionary first and then unpack it with `**`:

```python
>>> attrs = {'method.return_value': 3, 'other.side_effect': KeyError}
>>> mock = Mock(some_attribute='eggs', **attrs)
>>> mock.some_attribute
'eggs'
>>> mock.method()
3
>>> mock.other()
Traceback (most recent call last):
  ...
KeyError

```

When a callable mock is built with a *spec* (or a *spec_set*), it inspects the signature of the specification object as it matches calls against the mock. As a result, it recognizes the real call's arguments whether they arrived positionally or as keywords:

```python
>>> def f(a, b, c): pass
...
>>> mock = Mock(spec=f)
>>> mock(1, 2, c=3)
<Mock name='mock()' id='140161580456576'>
>>> mock.assert_called_with(1, 2, 3)
>>> mock.assert_called_with(a=1, b=2, c=3)

```

The same holds for `assert_called_with()`, `assert_called_once_with()`, `assert_has_calls()` and `assert_any_call()`. Under Autospeccing, it extends to method calls on the mock object too.

Changed in version 3.4: Signature introspection added for mock objects that are specced and autospecced.

[Subject index](INDEX.md) · [Continue](unittest-mock-propertymock-class.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md) · [Owning module, declaration or section: Mock and patch keyword configuration and callable spec signatures](unittest-mock-mock-class.md) · [Preceding source contract and version conditions](unittest-mock-noncallablemock-class.md)
