# ctypes - Structures and unions

### Structures and unions

Structures and unions are required to derive from the `Structure` and `Union` base classes, both defined within the `ctypes` module. Every subclass has to define a `_fields_` attribute. `_fields_` must be a list of *2-tuples*, each holding a *field name* together with a *field type*.

The field type has to be a `ctypes` type such as `c_int`, or any other type derived from `ctypes`: structure, union, array, pointer.

Below is a straightforward example of a POINT structure that holds two integers named *x* and *y*, and which also demonstrates how a structure is initialized in the constructor:

```python
>>> from ctypes import *
>>> class POINT(Structure):
...     _fields_ = [("x", c_int),
...                 ("y", c_int)]
...
>>> point = POINT(10, 20)
>>> print(point.x, point.y)
10 20
>>> point = POINT(y=5)
>>> print(point.x, point.y)
0 5
>>> POINT(1, 2, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: too many initializers
>>>

```

That said, you can assemble far more intricate structures. A structure can itself embed other structures simply by using a structure as a field type.

Here is a RECT structure holding two POINTs named *upperleft* and *lowerright*:

```python
>>> class RECT(Structure):
...     _fields_ = [("upperleft", POINT),
...                 ("lowerright", POINT)]
...
>>> rc = RECT(point)
>>> print(rc.upperleft.x, rc.upperleft.y)
0 5
>>> print(rc.lowerright.x, rc.lowerright.y)
0 0
>>>

```

Nested structures can be initialized in the constructor in more than one fashion as well:

```python
>>> r = RECT(POINT(1, 2), POINT(3, 4))
>>> r = RECT((1, 2), (3, 4))

```

Field [descriptor](https://docs.python.org/3.14/glossary.html#term-descriptor)s can be obtained from the *class*; they come in handy for debugging since they surface useful information. Refer to `CField`:

```python
>>> POINT.x
<ctypes.CField 'x' type=c_int, ofs=0, size=4>
>>> POINT.y
<ctypes.CField 'y' type=c_int, ofs=4, size=4>
>>>

```

Warning

`ctypes` will not pass unions or structures containing bit-fields to functions by value. Although that might happen to work on 32-bit x86, the library makes no guarantee it works in the general case. Always pass unions and structures with bit-fields to functions by pointer.

[Subject index](INDEX.md) · [Previous](passing-pointers-or-passing-parameters-by-reference.md) · [Continue](structure-union-layout-alignment-and-byte-order.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md)
