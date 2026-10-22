# What’s New In Python 3.5 / Changes in Python behavior

### Changes in Python behavior

- Through an oversight, older Python releases wrongly tolerated this syntax:

```python
f(1 for x in [1], *args)
f(1 for x in [1], **kwargs)

```

Now Python 3.5 properly raises a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError), since a generator expression must sit inside parentheses unless it is the only argument handed to a function.

[Subject index](INDEX.md) · [Previous source section](porting-to-python-3-5.md) · [Next source section](changes-in-the-python-api.md) · [Release/subject declaration](summary-release-highlights.md)
