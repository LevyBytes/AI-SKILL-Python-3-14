# unittest.mock - Autospeccing - Section introduction and initial examples

### Autospeccing

Autospeccing builds on mock's existing `spec` capability. It confines a mock's api to that of an original object (the spec), yet it does so recursively (lazily implemented) so that a mock's attributes match only the api of the spec's matching attributes. On top of that, mocked functions and methods inherit the original's call signature, so calling them wrongly raises a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

Before walking through how auto-speccing operates, let me lay out the reason it exists.

`Mock` is enormously capable and flexible, but it carries a weakness inherent to mocking in general. Refactor your code — rename members and the like — and any tests that exercise the *old api* through mocks rather than the genuine objects keep passing. So your whole suite can stay green even while the code is broken.

Changed in version 3.5: Prior to 3.5, a test containing a typo in the word assert would quietly pass when it ought to have raised. To bring that behaviour back, pass `unsafe=True` to Mock.

This is, incidentally, one more argument for having integration tests alongside unit tests. Exercising each piece in isolation is well and good, but unless you also test how the pieces are “wired together” there remains plenty of room for bugs that those tests could have caught.

A capability for tackling this already ships with `unittest.mock`, called speccing. Use a class or instance as a mock's `spec` and the only attributes you can touch on the mock are the ones present on the real class:

```python
>>> from urllib import request
>>> mock = Mock(spec=request.Request)
>>> mock.assret_called_with  # Intentional typo!
Traceback (most recent call last):
 ...
AttributeError: Mock object has no attribute 'assret_called_with'

```

Since the spec covers only the mock itself, the same trouble persists for any methods sitting on that mock:

```pycon
>>> mock.header_items()
<mock.Mock object at 0x...>
>>> mock.header_items.assret_called_with()  # Intentional typo!

```

Auto-speccing clears this up. You can either hand `autospec=True` to `patch()` / `patch.object()` or call `create_autospec()` to mint a mock with a spec. Pass the `autospec=True` argument to `patch()` and the object being replaced becomes the spec object. Since the speccing happens “lazily” (the spec materializes as attributes get accessed on the mock), it works against very intricate or deeply nested objects (think modules importing modules importing modules) without a heavy performance cost.

Here it is in action:

```python
>>> from urllib import request
>>> patcher = patch('__main__.request', autospec=True)
>>> mock_request = patcher.start()
>>> request is mock_request
True
>>> mock_request.Request
<MagicMock name='request.Request' spec='Request' id='...'>

```

Notice that `request.Request` carries a spec. The `request.Request` constructor accepts two arguments (one of them being *self*). Watch what occurs when we call it the wrong way:

```python
>>> req = request.Request()
Traceback (most recent call last):
 ...
TypeError: <lambda>() takes at least 2 arguments (1 given)

```

That spec carries over to instantiated classes too (that is, the return value of specced mocks):

```python
>>> req = request.Request('foo')
>>> req
<NonCallableMagicMock name='request.Request()' spec='Request' id='...'>

```

Because `Request` objects aren't callable, instantiating our mocked-out `request.Request` yields a non-callable mock. With the spec active, any typos in our asserts surface the right error:

```python
>>> req.add_header('spam', 'eggs')
<MagicMock name='request.Request().add_header()' id='...'>
>>> req.add_header.assret_called_with  # Intentional typo!
Traceback (most recent call last):
 ...
AttributeError: Mock object has no attribute 'assret_called_with'
>>> req.add_header.assert_called_with('spam', 'eggs')

```

For many situations it suffices to tack `autospec=True` onto the `patch()` calls you already have, gaining protection against typos and api drift.

Besides reaching *autospec* through `patch()`, there is `create_autospec()` for minting autospecced mocks on their own:

[Subject index](INDEX.md) · [Previous](unittest-mock-mock-open.md) · [Continue](autospeccing-code-example-from-urllib-import-request.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md)
