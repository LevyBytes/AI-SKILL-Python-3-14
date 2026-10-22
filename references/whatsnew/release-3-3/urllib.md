# What's New In Python 3.3 / urllib — urllib.request

### urllib

The [`Request`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.Request) class henceforth takes a *method* argument, which [`get_method()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.Request.get_method) consults to pick the HTTP method to apply. As an illustration, the following issues a `'HEAD'` request:

```python
>>> urlopen(Request('https://www.python.org', method='HEAD'))

```

([bpo-1673007](https://bugs.python.org/issue?@action=redirect&bpo=1673007))

[Subject index](INDEX.md) · [Previous source section](unittest.md) · [Next source section](webbrowser.md) · [Release/subject declaration](summary-release-highlights.md)
