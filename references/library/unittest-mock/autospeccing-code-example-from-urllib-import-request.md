# unittest.mock — Autospeccing — Code example: >>> from urllib import request

```python
>>> from urllib import request
>>> mock_request = create_autospec(request)
>>> mock_request.Request('foo', 'bar')
<NonCallableMagicMock name='mock.Request()' spec='Request' id='...'>

```

This does come with caveats and limits, which is exactly why it isn't switched on by default. To learn which attributes the spec object exposes, autospec must introspect it (access its attributes). Walking attributes on the mock triggers a matching walk over the original object behind the scenes. If any of your specced objects own properties or descriptors that can run code, autospec may be off the table. Conversely, it is far wiser to build your objects so that introspection stays safe [4].

A thornier issue: instance attributes are frequently created inside the [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) method and never appear on the class itself. *autospec* has no way to learn about attributes created on the fly, so it limits the api to attributes it can see.

```python
>>> class Something:
...   def __init__(self):
...     self.a = 33
...
>>> with patch('__main__.Something', autospec=True):
...   thing = Something()
...   thing.a
...
Traceback (most recent call last):
  ...
AttributeError: Mock object has no attribute 'a'

```

A handful of approaches can untangle this. The simplest — though not necessarily the least irritating — is just to assign the needed attributes to the mock after you create it. The fact that *autospec* blocks reading attributes missing from the spec doesn't stop you from setting them:

```python
>>> with patch('__main__.Something', autospec=True):
...   thing = Something()
...   thing.a = 33
...

```

Both *spec* and *autospec* offer a stricter variant that *does* block setting attributes that don't exist. That helps when you also want to guarantee your code only *sets* legitimate attributes, though plainly it rules out this very scenario:

```python
>>> with patch('__main__.Something', autospec=True, spec_set=True):
...   thing = Something()
...   thing.a = 33
...
Traceback (most recent call last):
 ...
AttributeError: Mock object has no attribute 'a'

```

The best fix is probably to declare class attributes as the default values for instance members that get initialised in [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__). Note, too, that if `__init__()` only ever assigns default attributes, supplying them as class attributes (shared across instances, of course) runs faster. e.g.

```python
class Something:
    a = 33

```

That raises yet another point. Quite commonly a member that will later hold an object of some other type is given a default of `None`. As a spec, `None` would be worthless, since it grants access to *no* attributes or methods at all. Because `None` is *never* going to make a useful spec — and likely flags a member meant to hold some other type — autospec skips speccing members set to `None`. They simply become ordinary mocks (well — MagicMocks):

```python
>>> class Something:
...     member = None
...
>>> mock = create_autospec(Something)
>>> mock.member.foo.bar.baz()
<MagicMock name='mock.member.foo.bar.baz()' id='...'>

```

If reworking your production classes to add defaults doesn't appeal, further options remain. One is simply to use an instance, rather than the class, as the spec. Another is to subclass the production class and put the defaults on that subclass, leaving the production class untouched. Each of these calls for a different object to act as the spec. Helpfully, `patch()` accommodates that — you just supply the substitute object as the *autospec* argument:

[Subject index](INDEX.md) · [Previous](autospeccing-section-introduction-and-initial-examples.md) · [Continue](autospeccing-code-example-class-something.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md) · [Owning module, declaration or section: Autospeccing](autospeccing-section-introduction-and-initial-examples.md)
