# unittest.mock: Mock call arguments and argument-history inspection

call_args

This is either `None` (when the mock has not been called) or the arguments that the mock was most recently called with. It comes as a tuple: the first member, also reachable through the `args` property, holds whatever positional arguments the mock was called with (or an empty tuple), while the second member, also reachable through the `kwargs` property, holds whatever keyword arguments there were (or an empty dictionary).

```python
>>> mock = Mock(return_value=None)
>>> print(mock.call_args)
None
>>> mock()
>>> mock.call_args
call()
>>> mock.call_args == ()
True
>>> mock(3, 4)
>>> mock.call_args
call(3, 4)
>>> mock.call_args == ((3, 4),)
True
>>> mock.call_args.args
(3, 4)
>>> mock.call_args.kwargs
{}
>>> mock(3, 4, 5, key='fish', next='w00t!')
>>> mock.call_args
call(3, 4, 5, key='fish', next='w00t!')
>>> mock.call_args.args
(3, 4, 5)
>>> mock.call_args.kwargs
{'key': 'fish', 'next': 'w00t!'}

```

`call_args`, together with the members of the lists `call_args_list`, `method_calls` and `mock_calls`, are `call` objects. Being tuples, they can be unpacked to reach the individual arguments and build more elaborate assertions. See calls as tuples.

Changed in version 3.8: Added `args` and `kwargs` properties.

 call_args_list

This holds, in order, every call made to the mock object (so the list’s length equals the count of times it has been called). Until any calls have happened it stays an empty list. The `call` object serves to neatly assemble lists of calls for comparison against `call_args_list`.

```python
>>> mock = Mock(return_value=None)
>>> mock()
>>> mock(3, 4)
>>> mock(key='fish', next='w00t!')
>>> mock.call_args_list
[call(), call(3, 4), call(key='fish', next='w00t!')]
>>> expected = [(), ((3, 4),), ({'key': 'fish', 'next': 'w00t!'},)]
>>> mock.call_args_list == expected
True

```

The members of `call_args_list` are `call` objects. They can be unpacked as tuples to reach the individual arguments. See calls as tuples.

 method_calls

Beyond keeping tabs on calls to themselves, mocks additionally keep tabs on calls to methods and attributes, and to *their* methods and attributes:

```python
>>> mock = Mock()
>>> mock.method()
<Mock name='mock.method()' id='...'>
>>> mock.property.method.attribute()
<Mock name='mock.property.method.attribute()' id='...'>
>>> mock.method_calls
[call.method(), call.property.method.attribute()]

```

The members of `method_calls` are `call` objects. They can be unpacked as tuples to reach the individual arguments. See calls as tuples.

[Subject index](INDEX.md) · [Previous](mock-side-effects.md) · [Continue](mock-call-history.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md) · [Owning module, declaration or section: unittest.mock.Mock](unittest-mock-mock-class.md) · [Owning module, declaration or section: The Mock Class](unittest-mock-mock-class.md)
