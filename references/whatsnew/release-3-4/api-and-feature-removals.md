# What's New In Python 3.4 / API and Feature Removals — difflib, http.client, importlib, inspect, marshal, urllib.request

### API and Feature Removals

These outdated, formerly obsolete APIs and capabilities are now gone:

- The neglected `Misc/TextMate` and `Misc/vim` directories are gone (consult the [devguide](https://devguide.python.org) for recommendations on replacements).

- The `SO` makefile macro is gone (the `SHLIB_SUFFIX` and `EXT_SUFFIX` macros took its place) ([bpo-16754](https://bugs.python.org/issue?@action=redirect&bpo=16754)).

- The `PyThreadState.tick_counter` field is gone; ever since Python 3.2 brought the "new GIL", its value had carried no meaning ([bpo-19199](https://bugs.python.org/issue?@action=redirect&bpo=19199)).

- [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib) no longer carries `PyLoader` and `PyPycLoader`. (Contributed by Taras Lyapun in [bpo-15641](https://bugs.python.org/issue?@action=redirect&bpo=15641).)

- The *strict* parameter on [`HTTPConnection`](https://docs.python.org/3.14/library/http.client.html#http.client.HTTPConnection) and [`HTTPSConnection`](https://docs.python.org/3.14/library/http.client.html#http.client.HTTPSConnection) is gone. HTTP 0.9-style "Simple Responses" are no longer handled.

- The obsolete [`urllib.request.Request`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.Request) accessor and mutator methods `add_data`, `has_data`, `get_data`, `get_type`, `get_host`, `get_selector`, `set_proxy`, `get_origin_req_host`, and `is_unverifiable` are gone (reach for direct attribute access instead).

- [`marshal`](https://docs.python.org/3.14/library/marshal.html#module-marshal) no longer supports loading the obsolete `TYPE_INT64`. (Contributed by Dan Riti in [bpo-15480](https://bugs.python.org/issue?@action=redirect&bpo=15480).)

- [`inspect.Signature`](https://docs.python.org/3.14/library/inspect.html#inspect.Signature): a valid name is now mandatory for positional-only parameters.

- [`object.__format__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__format__) rejects non-empty format strings outright, raising a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) where it once did not. Passing a non-empty string has been obsolete ever since Python 3.2. The motive for the change is to head off a scenario in which formerly functioning (yet wrong) code would begin to break once an object acquired a __format__ method; the upshot is that your code may now throw a `TypeError` whenever an `'s'` format code is paired with objects lacking a __format__ method able to process it. Consult [bpo-7994](https://bugs.python.org/issue?@action=redirect&bpo=7994) for the rationale.

- `difflib.SequenceMatcher.isbjunk()` and `difflib.SequenceMatcher.isbpopular()`, obsolete since 3.2, are now gone: write `x in sm.bjunk` and `x in sm.bpopular`, with *sm* being a [`SequenceMatcher`](https://docs.python.org/3.14/library/difflib.html#difflib.SequenceMatcher) object ([bpo-13248](https://bugs.python.org/issue?@action=redirect&bpo=13248)).

[Subject index](INDEX.md) · [Previous source section](operating-systems-no-longer-supported.md) · [Next source section](code-cleanups.md) · [Release/subject declaration](release-highlights.md)
