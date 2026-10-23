# unittest.mock - patch.dict - Signature and initial contract

### patch.dict

 patch.dict(*in_dict*, *values=()*, *clear=False*, ***kwargs*)

Patch a dictionary (or a dictionary-like object), then return it to its starting state once the test wraps up; the restored dictionary is a copy of how the dictionary stood before the test ran.

*in_dict* may be a dictionary or a mapping-like container. A mapping has to at minimum support fetching, assigning, and removing items, along with iterating over its keys.

*in_dict* may instead be a string naming the dictionary, in which case it gets retrieved by importing it.

*values* may be a dictionary of values to apply within the dictionary. It may also be an iterable of `(key, value)` pairs.

When *clear* is true, the dictionary is emptied before the fresh values get written.

`patch.dict()` may additionally be invoked with arbitrary keyword arguments to assign values in the dictionary.

Changed in version 3.8: serving as a context manager, `patch.dict()` now hands back the dictionary it patched.

`patch.dict()` works as a context manager, a decorator, or a class decorator:

```python
>>> foo = {}
>>> @patch.dict(foo, {'newkey': 'newvalue'})
... def test():
...     assert foo == {'newkey': 'newvalue'}
...
>>> test()
>>> assert foo == {}

```

As a class decorator, `patch.dict()` respects `patch.TEST_PREFIX` (which defaults to `'test'`) when picking which methods to wrap:

```python
>>> import os
>>> import unittest
>>> from unittest.mock import patch
>>> @patch.dict('os.environ', {'newkey': 'newvalue'})
... class TestSample(unittest.TestCase):
...     def test_sample(self):
...         self.assertEqual(os.environ['newkey'], 'newvalue')

```

Should you prefer a different prefix for your tests, you can tell the patchers about it by setting `patch.TEST_PREFIX`. For fuller detail on changing the value of see TEST_PREFIX.

Use `patch.dict()` either to insert members into a dictionary, or merely to let a test mutate one, guaranteeing the dictionary is put back when the test finishes.

```python
>>> foo = {}
>>> with patch.dict(foo, {'newkey': 'newvalue'}) as patched_foo:
...     assert foo == {'newkey': 'newvalue'}
...     assert patched_foo == {'newkey': 'newvalue'}
...     # You can add, update or delete keys of foo (or patched_foo, it's the same dict)
...     patched_foo['spam'] = 'eggs'
...
>>> assert foo == {}
>>> assert patched_foo == {}

```

```python
>>> import os
>>> with patch.dict('os.environ', {'newkey': 'newvalue'}):
...     print(os.environ['newkey'])
...
newvalue
>>> assert 'newkey' not in os.environ

```

Within the `patch.dict()` call, keywords let you assign values into the dictionary:

```python
>>> mymodule = MagicMock()
>>> mymodule.function.return_value = 'fish'
>>> with patch.dict('sys.modules', mymodule=mymodule):
...     import mymodule
...     mymodule.function('some', 'args')
...
'fish'

```

`patch.dict()` is usable with dictionary-like objects that aren't genuinely dictionaries. They must, as a bare minimum, allow item fetching, assigning, and deleting, plus either iteration or a membership check. Those correspond to the magic methods [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__), [`__setitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__setitem__), [`__delitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__delitem__) and one of [`__iter__()`](https://docs.python.org/3.14/library/stdtypes.html#container.__iter__) or [`__contains__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__contains__).

[Subject index](INDEX.md) · [Continue](patch-dict-code-example-class-container.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md)
