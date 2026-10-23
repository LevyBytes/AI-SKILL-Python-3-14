# unittest.mock - Magic Mock - Signature and initial contract

*class *unittest.mock.NonCallableMagicMock(**args*, ***kw*)

A non-callable version of `MagicMock`.

Its constructor parameters mean what they do for `MagicMock`, except for *return_value* and *side_effect*, which hold no meaning on a non-callable mock.

The magic methods come set up with `MagicMock` objects, letting you configure and use them as you ordinarily would:

```python
>>> mock = MagicMock()
>>> mock[3] = 'fish'
>>> mock.__setitem__.assert_called_with(3, 'fish')
>>> mock.__getitem__.return_value = 'result'
>>> mock[2]
'result'

```

By default a good many of the protocol methods must return objects of a particular type. They arrive preconfigured with a default return value, so you can rely on them without lifting a finger when the return value doesn't concern you. You're still free to *set* the return value by hand should you wish to override the default.

Methods and their defaults:

- `__lt__`: [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented)

- `__gt__`: `NotImplemented`

- `__le__`: `NotImplemented`

- `__ge__`: `NotImplemented`

- `__int__`: `1`

- `__contains__`: `False`

- `__len__`: `0`

- `__iter__`: `iter([])`

- `__exit__`: `False`

- `__aexit__`: `False`

- `__complex__`: `1j`

- `__float__`: `1.0`

- `__bool__`: `True`

- `__index__`: `1`

- `__hash__`: default hash for the mock

-

[Subject index](INDEX.md) · [Previous](unittest-mock-magicmock-class.md) · [Continue](magic-mock-contract-str-default-str-for-the-mock.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md) · [Owning module, declaration or section: Magic Mock](unittest-mock-magicmock-class.md)
