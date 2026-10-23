# unittest.mock - FILTER_DIR

### FILTER_DIR

 unittest.mock.FILTER_DIR

A module-level variable, `FILTER_DIR`, governs how mock objects answer [`dir()`](https://docs.python.org/3.14/library/functions.html#dir). Its default of `True` applies the filtering covered below so that only the useful members surface. To turn this off — say, because you dislike it or need it gone for diagnostics — assign `mock.FILTER_DIR = False`.

While filtering is active, `dir(some_mock)` surfaces only the worthwhile attributes, including any dynamically added ones that normally stay hidden. When the mock came from a *spec* (or, naturally, an *autospec*), every attribute of the original appears even before it has been touched:

```pycon
>>> dir(Mock())
['assert_any_call',
 'assert_called',
 'assert_called_once',
 'assert_called_once_with',
 'assert_called_with',
 'assert_has_calls',
 'assert_not_called',
 'attach_mock',
 ...
>>> from urllib import request
>>> dir(Mock(spec=request))
['AbstractBasicAuthHandler',
 'AbstractDigestAuthHandler',
 'AbstractHTTPHandler',
 'BaseHandler',
 ...

```

A great many low-value attributes with leading underscores or double underscores — ones private to `Mock` rather than belonging to the thing under test — are stripped from what [`dir()`](https://docs.python.org/3.14/library/functions.html#dir) reports for a `Mock`. To disable that behaviour, flip the module-level switch `FILTER_DIR`:

```pycon
>>> from unittest import mock
>>> mock.FILTER_DIR = False
>>> dir(mock.Mock())
['_NonCallableMock__get_return_value',
 '_NonCallableMock__get_side_effect',
 '_NonCallableMock__return_value_doc',
 '_NonCallableMock__set_return_value',
 '_NonCallableMock__set_side_effect',
 '__call__',
 '__class__',
 ...

```

Otherwise, combining `vars(my_mock)` (instance members) with `dir(type(my_mock))` (type members) sidesteps the filtering no matter how `FILTER_DIR` is set.

[Subject index](INDEX.md) · [Previous](unittest-mock-any.md) · [Continue](unittest-mock-mock-open.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md)
