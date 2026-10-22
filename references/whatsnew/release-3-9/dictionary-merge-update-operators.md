# What's New In Python 3.9 / Dictionary Merge & Update Operators

### New Features

### Dictionary Merge & Update Operators

The built-in [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) class gains a merge operator (`|`) plus an update operator (`|=`). These sit alongside the already-available `dict.update` and `{**d1, **d2}` approaches to combining dictionaries.

Example:

```python
>>> x = {"key1": "value1 from x", "key2": "value2 from x"}
>>> y = {"key2": "value2 from y", "key3": "value3 from y"}
>>> x | y
{'key1': 'value1 from x', 'key2': 'value2 from y', 'key3': 'value3 from y'}
>>> y | x
{'key2': 'value2 from x', 'key3': 'value3 from y', 'key1': 'value1 from x'}

```

Consult [**PEP 584**](https://peps.python.org/pep-0584/) for the complete writeup. (Contributed by Brandt Bucher in [bpo-36144](https://bugs.python.org/issue?@action=redirect&bpo=36144).)

[Subject index](INDEX.md) · [Previous source section](you-should-check-for-deprecationwarning-in-your-code.md) · [Next source section](new-string-methods-to-remove-prefixes-and-suffixes.md) · [Release/subject declaration](summary-release-highlights.md)
