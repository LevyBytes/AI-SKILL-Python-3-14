# unittest.mock - call

### call

 unittest.mock.call(**args*, ***kwargs*)

To write more concise assertions, reach for the `call()` helper, which lines up against `call_args`, `call_args_list`, `mock_calls` and `method_calls`. The `assert_has_calls()` method also accepts `call()`.

```python
>>> m = MagicMock(return_value=None)
>>> m(1, 2, a='foo', b='bar')
>>> m()
>>> m.call_args_list == [call(1, 2, a='foo', b='bar'), call()]
True

```

 call.call_list()

When a call object stands for a series of calls, `call_list()` hands back a list containing each of the intermediate calls plus the closing one.

Where `call_list` really shines is asserting against “chained calls.” One line of code that strings several calls together is a chained call, and it deposits several entries into a mock's `mock_calls`. Building that call sequence by hand gets tiresome.

From the very same chained call, `call_list()` is able to assemble the call sequence:

```python
>>> m = MagicMock()
>>> m(1).method(arg='foo').other('bar')(2.0)
<MagicMock name='mock().method().other()()' id='...'>
>>> kall = call(1).method(arg='foo').other('bar')(2.0)
>>> kall.call_list()
[call(1),
 call().method(arg='foo'),
 call().method().other('bar'),
 call().method().other()(2.0)]
>>> m.mock_calls == kall.call_list()
True

```

Depending on the way it was built, a `call` object is a tuple of either (positional args, keyword args) or (name, positional args, keyword args). Building one by hand offers little of interest, yet the `call` objects sitting in the `Mock.call_args`, `Mock.call_args_list` and `Mock.mock_calls` attributes can be examined to reach the separate arguments they hold.

Inside `Mock.call_args` and `Mock.call_args_list`, the `call` objects are two-tuples of (positional args, keyword args), while the `call` objects found in `Mock.mock_calls` — and any you build yourself — are three-tuples of (name, positional args, keyword args).

Their “tupleness” lets you extract the separate arguments for richer introspection and assertions. Positional arguments come back as a tuple (empty when none are present) and keyword arguments come back as a dictionary:

```python
>>> m = MagicMock(return_value=None)
>>> m(1, 2, 3, arg='one', arg2='two')
>>> kall = m.call_args
>>> kall.args
(1, 2, 3)
>>> kall.kwargs
{'arg': 'one', 'arg2': 'two'}
>>> kall.args is kall[0]
True
>>> kall.kwargs is kall[1]
True

```

```python
>>> m = MagicMock()
>>> m.foo(4, 5, 6, arg='two', arg2='three')
<MagicMock name='mock.foo()' id='...'>
>>> kall = m.mock_calls[0]
>>> name, args, kwargs = kall
>>> name
'foo'
>>> args
(4, 5, 6)
>>> kwargs
{'arg': 'two', 'arg2': 'three'}
>>> name is m.mock_calls[0][0]
True

```

[Subject index](INDEX.md) · [Previous](unittest-mock-default.md) · [Continue](unittest-mock-create-autospec.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md)
