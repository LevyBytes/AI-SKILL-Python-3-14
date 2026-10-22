# Handling Exceptions

### Handling Exceptions

Whenever *urlopen* can't deal with a response it throws [`URLError`](https://docs.python.org/3.14/library/urllib.error.html#urllib.error.URLError) (although, as is typical of Python APIs, built-in exceptions like [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) or [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) and others can surface too).

When the URL in question is an HTTP one, the exception you'll see is [`HTTPError`](https://docs.python.org/3.14/library/urllib.error.html#urllib.error.HTTPError), which derives from [`URLError`](https://docs.python.org/3.14/library/urllib.error.html#urllib.error.URLError).

Both of those exception classes are made available from the [`urllib.error`](https://docs.python.org/3.14/library/urllib.error.html#module-urllib.error) module.

[Subject index](INDEX.md) · [Previous source context](headers.md) · [Following source context](urlerror.md)
