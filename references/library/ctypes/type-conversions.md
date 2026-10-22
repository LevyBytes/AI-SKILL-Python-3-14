# ctypes — Type conversions

### Type conversions

For the most part ctypes enforces strict type checking. So, when `POINTER(c_int)` appears in a function’s `argtypes` list or as the declared type of a structure member, only instances of that exact type get through. A handful of exceptions exist where ctypes will take other objects. For instance, a compatible array instance may stand in for a pointer type, so an array of c_int is accepted wherever `POINTER(c_int)` is expected:

```python
>>> class Bar(Structure):
...     _fields_ = [("count", c_int), ("values", POINTER(c_int))]
...
>>> bar = Bar()
>>> bar.values = (c_int * 3)(1, 2, 3)
>>> bar.count = 3
>>> for i in range(bar.count):
...     print(bar.values[i])
...
1
2
3
>>>

```

Beyond that, when a function parameter is declared in `argtypes` as a pointer type — say `POINTER(c_int)` — you may hand the function an object of the pointed-to type (here `c_int`). ctypes will automatically apply the necessary `byref()` conversion for you in that situation.

Assigning `None` is how you set a POINTER type field to `NULL`:

```python
>>> bar.values = None
>>>

```

Now and then you end up holding instances whose types don’t match. C lets you cast from one type to another, and `ctypes` offers a `cast()` function that works the same way. The `Bar` structure shown above takes `POINTER(c_int)` pointers or `c_int` arrays for its `values` field, yet rejects instances of any other type:

```python
>>> bar.values = (c_byte * 4)()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: incompatible types, c_byte_Array_4 instance instead of LP_c_long instance
>>>

```

This is where the `cast()` function earns its keep.

You use the `cast()` function to recast a ctypes instance as a pointer to some other ctypes data type. `cast()` expects two arguments: a ctypes object that already is, or can be turned into, a pointer of some sort, plus a ctypes pointer type. The return value is an instance of that second argument, and it points at the same block of memory as the first argument:

```python
>>> a = (c_byte * 4)()
>>> cast(a, POINTER(c_int))
<ctypes.LP_c_long object at ...>
>>>

```

With that, `cast()` lets us populate the `values` field of the `Bar` structure:

```python
>>> bar = Bar()
>>> bar.values = cast((c_byte * 4)(), POINTER(c_int))
>>> print(bar.values[0])
0
>>>

```

[Subject index](INDEX.md) · [Previous](thread-safety-without-the-gil.md) · [Continue](incomplete-types.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md)
