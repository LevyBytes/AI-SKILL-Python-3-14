# unittest.mock — Mocking unbound methods

### Mocking unbound methods

Now and then a test has to patch an *unbound method* — that is, patch the method at the class level rather than at the instance level. To verify which objects invoked that specific method, you have to supply `self` as the leading argument. The catch is that a plain mock won't do here: swapping an unbound method for a mock means it never converts into a bound method when retrieved off the instance, so `self` is never handed in. The way around it is to swap the unbound method for an actual function. Because the [`patch()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.patch) decorator makes patching methods with a mock so effortless, being forced to write a real function feels like a chore.

Hand `autospec=True` to patch and the patching is performed with a *real* function object instead. That function object mirrors the signature of whatever it replaces, yet routes everything to a mock beneath the surface. Your mock is still auto-created precisely as it was before. The upshot is this: when such a patch targets a class-level unbound method, the function standing in for it becomes a bound method once retrieved from an instance. At that point `self` arrives as the first argument — exactly the behavior that was required:

```python
>>> class Foo:
...   def foo(self):
...     pass
...
>>> with patch.object(Foo, 'foo', autospec=True) as mock_foo:
...   mock_foo.return_value = 'foo'
...   foo = Foo()
...   foo.foo()
...
'foo'
>>> mock_foo.assert_called_once_with(foo)

```

Omit `autospec=True` and the unbound method gets replaced by a Mock instance, which never receives `self`.

[Subject index](INDEX.md) · [Previous](applying-the-same-patch-to-every-test-method.md) · [Continue](checking-multiple-calls-with-mock.md) · [Owning module, declaration or section: unittest.mock](mock-patching-methods.md)
