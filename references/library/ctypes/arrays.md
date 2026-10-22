# ctypes — Arrays

Worth keeping in mind: how bit fields get allocated and arranged in memory is left undefined by the C standard, so each compiler decides for itself. By default, Python tries to mirror what a “native” compiler would do on the platform you are running. The `_layout_` attribute documents that default behavior and explains how you can override it.

### Arrays

An array is a sequence holding a fixed count of items, all of the same type.

To build an array type, the preferred approach is to multiply a data type by a positive integer:

```python
TenPointsArrayType = POINT * 10

```

What follows is a slightly contrived example, a structure that bundles 4 POINTs together with some other members:

```python
>>> from ctypes import *
>>> class POINT(Structure):
...     _fields_ = ("x", c_int), ("y", c_int)
...
>>> class MyStruct(Structure):
...     _fields_ = [("a", c_int),
...                 ("b", c_float),
...                 ("point_array", POINT * 4)]
>>>
>>> print(len(MyStruct().point_array))
4
>>>

```

You make instances the normal way, by invoking the class:

```python
arr = TenPointsArrayType()
for pt in arr:
    print(pt.x, pt.y)

```

Running that snippet emits a run of `0 0` lines, since every slot of the array starts out zeroed.

You may also supply initializers that have the right type:

```python
>>> from ctypes import *
>>> TenIntegers = c_int * 10
>>> ii = TenIntegers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
>>> print(ii)
<c_long_Array_10 object at 0x...>
>>> for i in ii: print(i, end=" ")
...
1 2 3 4 5 6 7 8 9 10
>>>

```

[Subject index](INDEX.md) · [Continue](pointers-section-introduction-and-initial-examples.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md) · [Owning module, declaration or section: Bit fields in structures and unions](bit-fields-in-structures-and-unions.md) · [Preceding source contract and version conditions](bit-fields-in-structures-and-unions.md)
