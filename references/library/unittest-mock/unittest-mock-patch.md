# unittest.mock — patch — Signature and initial contract

unittest.mock.patch(*target*, *new=DEFAULT*, *spec=None*, *create=False*, *spec_set=None*, *autospec=None*, *new_callable=None*, ***kwargs*)

`patch()` serves as a function decorator, a class decorator, or a context manager. Within the body of the function or the with statement, the *target* gets replaced by a *new* object. Once the function or with statement finishes, the patch is reverted.

When *new* is left out, the target is swapped for an `AsyncMock` if the patched object is an async function, otherwise for a `MagicMock`. If `patch()` is applied as a decorator and *new* is left out, the generated mock is handed to the decorated function as an extra argument. If `patch()` is applied as a context manager, the generated mock is what the context manager yields.

*target* must be a string shaped like `'package.module.ClassName'`. The *target* gets imported and the named object is swapped for the *new* object, so the *target* has to be importable from wherever you invoke `patch()`. The target is imported at the moment the decorated function runs, not when the decoration happens.

The *spec* and *spec_set* keyword arguments get forwarded to the `MagicMock` when patch builds one on your behalf.

On top of that you may supply `spec=True` or `spec_set=True`, which makes patch hand in the object being mocked as the spec/spec_set object.

*new_callable* lets you nominate a different class, or callable object, to be invoked when creating the *new* object. By default `AsyncMock` serves for async functions and `MagicMock` for everything else.

A stronger variant of *spec* is *autospec*. Setting `autospec=True` builds the mock with a spec drawn from the object being swapped out. Every attribute of the mock likewise carries the spec of the matching attribute on the object being swapped out. Mocked methods and functions get their arguments validated and raise a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) when invoked with a mismatched signature. For mocks that stand in for a class, their return value (the ‘instance’) carries the same spec as the class. See the `create_autospec()` function along with Autospeccing.

Rather than `autospec=True` you may supply `autospec=some_object` to adopt an arbitrary object as the spec in place of the one being swapped out.

By default `patch()` won't replace attributes that aren't there. Supplying `create=True` makes patch create a missing attribute for you when the patched function runs and remove it again once the patched function has finished. This helps when writing tests against attributes your production code generates at runtime. It's off by default since it can be hazardous. Turning it on lets you write passing tests against APIs that don't truly exist!

Note

Changed in version 3.5: When you patch builtins inside a module, passing `create=True` is unnecessary; it gets added by default.

Patch can serve as a [`TestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase) class decorator. It operates by decorating every test method within the class. This trims the boilerplate when your test methods rely on a shared set of patchings. `patch()` locates tests by scanning for method names beginning with `patch.TEST_PREFIX`. That defaults to `'test'`, matching how [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) locates tests. A different prefix can be chosen by assigning to `patch.TEST_PREFIX`.

Patch can serve as a context manager via the with statement. Here the patch covers the indented block that follows the with statement. Using “as” binds the patched object to the name placed after the “as”; quite handy when `patch()` is producing a mock object for you.

`patch()` accepts arbitrary keyword arguments. They get forwarded to `AsyncMock` when the patched object is asynchronous, to `MagicMock` otherwise, or to *new_callable* when one is given.

`patch.dict(...)`, `patch.multiple(...)` and `patch.object(...)` exist for alternate use-cases.

`patch()` as a function decorator, building the mock for you and feeding it into the decorated function:

```python
>>> @patch('__main__.SomeClass')
... def function(normal_argument, mock_class):
...     print(mock_class is SomeClass)
...
>>> function(None)
True

```

Patching a class swaps the class for a `MagicMock` *instance*. When the class is instantiated in the code being tested, what gets used is the `return_value` of the mock.

When the class is instantiated several times you might use `side_effect` to hand back a fresh mock on each occasion. Or you can set the *return_value* to whatever you like.

To set return values on methods of *instances* belonging to the patched class, you have to do it on the `return_value`. For instance:

```python
>>> class Class:
...     def method(self):
...         pass
...
>>> with patch('__main__.Class') as MockClass:
...     instance = MockClass.return_value
...     instance.method.return_value = 'foo'
...     assert Class() is instance
...     assert Class().method() == 'foo'
...

```

When you use *spec* or *spec_set* and `patch()` is standing in for a *class*, then the return value of the created mock carries the same spec.

```python
>>> Original = Class
>>> patcher = patch('__main__.Class', spec=True)
>>> MockClass = patcher.start()
>>> instance = MockClass()
>>> assert isinstance(instance, Original)
>>> patcher.stop()

```

The *new_callable* argument helps when you'd like a class other than the default `MagicMock` for the created mock. As an example, if you wanted a `NonCallableMock` instead:

[Subject index](INDEX.md) · [Previous](patch.md) · [Continue](patch-code-example-thing-object.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md) · [Owning module, declaration or section: patch](patch.md)
