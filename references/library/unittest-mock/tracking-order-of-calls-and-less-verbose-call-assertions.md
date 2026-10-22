# unittest.mock — Tracking order of calls and less verbose call assertions

### Tracking order of calls and less verbose call assertions

Through its [`method_calls`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.method_calls) attribute, the [`Mock`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock) class lets you follow the *order* of method calls made on your mock objects. That attribute won't follow the ordering of calls spread across distinct mock objects, but [`mock_calls`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.mock_calls) gives us a way to reach the same result.

Since mocks log calls to their child mocks under `mock_calls`, and reaching for any attribute on a mock spawns a child mock, we can carve our separate mocks out of a single parent. Every call to those child mocks then lands, in sequence, within the parent's `mock_calls`:

```python
>>> manager = Mock()
>>> mock_foo = manager.foo
>>> mock_bar = manager.bar

```

```python
>>> mock_foo.something()
<Mock name='mock.foo.something()' id='...'>
>>> mock_bar.other.thing()
<Mock name='mock.bar.other.thing()' id='...'>

```

```python
>>> manager.mock_calls
[call.foo.something(), call.bar.other.thing()]

```

From there we can assert about the calls — order included — by matching against the `mock_calls` attribute on the manager mock:

```python
>>> expected_calls = [call.foo.something(), call.bar.other.thing()]
>>> manager.mock_calls == expected_calls
True

```

When `patch` is the one building your mocks and slotting them into place, you can bind them onto a manager mock via the [`attach_mock()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.attach_mock) method. Once attached, the calls land in the manager's `mock_calls`.

```python
>>> manager = MagicMock()
>>> with patch('mymodule.Class1') as MockClass1:
...     with patch('mymodule.Class2') as MockClass2:
...         manager.attach_mock(MockClass1, 'MockClass1')
...         manager.attach_mock(MockClass2, 'MockClass2')
...         MockClass1().foo()
...         MockClass2().bar()
<MagicMock name='mock.MockClass1().foo()' id='...'>
<MagicMock name='mock.MockClass2().bar()' id='...'>
>>> manager.mock_calls
[call.MockClass1(),
call.MockClass1().foo(),
call.MockClass2(),
call.MockClass2().bar()]

```

Should a great many calls have occurred while you only care about one specific run of them, another route is the [`assert_has_calls()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.assert_has_calls) method. It accepts a list of calls (assembled with the [`call`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.call) object). Provided that run of calls appears within [`mock_calls`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.mock_calls), the assert passes.

```python
>>> m = MagicMock()
>>> m().foo().bar().baz()
<MagicMock name='mock().foo().bar().baz()' id='...'>
>>> m.one().two().three()
<MagicMock name='mock.one().two().three()' id='...'>
>>> calls = call.one().two().three().call_list()
>>> m.assert_has_calls(calls)

```

Despite the chained call `m.one().two().three()` not being the sole calls made against the mock, the assert nonetheless passes.

There are occasions where a mock has received several calls and you only want to assert about *some* of them. The order might not even matter to you. For that, hand `any_order=True` to `assert_has_calls`:

```python
>>> m = MagicMock()
>>> m(1), m.two(2, 3), m.seven(7), m.fifty('50')
(...)
>>> calls = [call.fifty('50'), call(1), call.seven(7)]
>>> m.assert_has_calls(calls, any_order=True)

```

[Subject index](INDEX.md) · [Previous](mocking-imports-with-patch-dict.md) · [Continue](more-complex-argument-matching.md) · [Owning module, declaration or section: unittest.mock](mock-patching-methods.md)
