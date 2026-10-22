# unittest.mock.Mock: `reset_mock()`, `mock_add_spec()`, `attach_mock()`

reset_mock(***, *return_value=False*, *side_effect=False*)

Calling the reset_mock method clears every call attribute on a mock object:

```pycon
>>> mock = Mock(return_value=None)
>>> mock('hello')
>>> mock.called
True
>>> mock.reset_mock()
>>> mock.called
False

```

This comes in handy whenever you intend to run a sequence of assertions that reuse one and the same object.

When the *return_value* parameter is set to `True`, it clears `return_value`:

```pycon
>>> mock = Mock(return_value=5)
>>> mock('hello')
5
>>> mock.reset_mock(return_value=True)
>>> mock('hello')
<Mock name='mock()' id='...'>

```

When the *side_effect* parameter is set to `True`, it clears `side_effect`:

```pycon
>>> mock = Mock(side_effect=ValueError)
>>> mock('hello')
Traceback (most recent call last):
  ...
ValueError
>>> mock.reset_mock(side_effect=True)
>>> mock('hello')
<Mock name='mock()' id='...'>

```

Bear in mind that, by default, `reset_mock()` *doesn’t* wipe out the `return_value`, `side_effect`, or any child attributes you assigned through ordinary assignment.

Child mocks get reset too.

Changed in version 3.6: Added two keyword-only arguments to the reset_mock function.

 mock_add_spec(*spec*, *spec_set=False*)

Attach a spec onto a mock. The *spec* argument is permitted to be an object or else a list of strings. From the mock you may retrieve, as attributes, only those attributes present on the *spec*.

Where *spec_set* holds true, only the spec’s attributes are assignable.

 attach_mock(*mock*, *attribute*)

Bind a mock onto this one as an attribute, overriding its name as well as its parent. Whenever the attached mock is called, that gets logged within this one’s `method_calls` and `mock_calls` attributes.

[Subject index](INDEX.md) · [Previous](mock-call-sequence-and-absence-assertions.md) · [Continue](mock-configuration-and-child-creation.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md) · [Owning module, declaration or section: unittest.mock.Mock](unittest-mock-mock-class.md) · [Owning module, declaration or section: The Mock Class](unittest-mock-mock-class.md)
