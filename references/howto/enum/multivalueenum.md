# MultiValueEnum

### MultiValueEnum

Allows each member to carry more than one value:

```python
>>> class MultiValueEnum(Enum):
...     def __new__(cls, value, *values):
...         self = object.__new__(cls)
...         self._value_ = value
...         for v in values:
...             self._add_value_alias_(v)
...         return self
...
>>> class DType(MultiValueEnum):
...     float32 = 'f', 8
...     double64 = 'd', 9
...
>>> DType('f')
<DType.float32: 'f'>
>>> DType(9)
<DType.double64: 'd'>

```

[Subject index](INDEX.md) · [Previous source context](duplicatefreeenum.md) · [Following source context](planet.md)
