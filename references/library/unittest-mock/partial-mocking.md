# unittest.mock - Partial mocking

### Partial mocking

In certain tests you might wish to mock out a call to [`datetime.date.today()`](https://docs.python.org/3.14/library/datetime.html#datetime.date.today) so it yields a fixed date, yet avoid stopping the code under test from making fresh date objects. Sadly [`datetime.date`](https://docs.python.org/3.14/library/datetime.html#datetime.date) is implemented in C, so you can't simply monkey-patch away the static `datetime.date.today()` method.

Instead, you can essentially wrap the date class in a mock while letting calls to the constructor pass through to the genuine class (and return genuine instances).

The [`patch decorator`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.patch) is applied here to mock out the `date` class within the module under test. The [`side_effect`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.side_effect) attribute on the mock date class then gets set to a lambda that returns a real date. Whenever the mock date class is called, `side_effect` will build and return a real date.

```python
>>> import datetime as dt
>>> with patch('mymodule.date') as mock_date:
...     mock_date.today.return_value = dt.date(2010, 10, 8)
...     mock_date.side_effect = lambda *args, **kw: dt.date(*args, **kw)
...
...     assert mymodule.date.today() == dt.date(2010, 10, 8)
...     assert mymodule.date(2009, 6, 8) == dt.date(2009, 6, 8)

```

Notice we don't patch [`datetime.date`](https://docs.python.org/3.14/library/datetime.html#datetime.date) globally; we patch `date` inside the module that *uses* it. See [where to patch](https://docs.python.org/3.14/library/unittest.mock.html#where-to-patch).

Calling `date.today()` yields a known date, while calls to the `date(...)` constructor still produce ordinary dates. Lacking this, you can end up forced to compute an expected result with precisely the same algorithm the code under test uses, which is a textbook testing anti-pattern.

The `mock_date` attributes (`call_count` and friends) record calls to the date constructor, which may likewise be handy for your tests.

[Subject index](INDEX.md) · [Previous](mocking-chained-calls.md) · [Owning module, declaration or section: unittest.mock](mock-patching-methods.md) · [Required continuation of the source contract](mocking-a-generator-method.md)
