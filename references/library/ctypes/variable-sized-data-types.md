# ctypes - Variable-sized data types

### Variable-sized data types

`ctypes` gives you some help for arrays and structures whose size can vary.

Use the `resize()` function to change the size of the memory buffer behind an existing ctypes object. Pass the object as the first argument and the desired size in bytes as the second. You can’t shrink the memory block below the natural size dictated by the object’s type — attempting to do so raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError):

```python
>>> short_array = (c_short * 4)()
>>> print(sizeof(short_array))
8
>>> resize(short_array, 4)
Traceback (most recent call last):
    ...
ValueError: minimum size is 8
>>> resize(short_array, 32)
>>> sizeof(short_array)
32
>>> sizeof(type(short_array))
8
>>>

```

All well and good, yet how do you reach the extra elements now living inside this array? Because the type is still aware of only 4 elements, trying to touch the others raises errors:

```python
>>> short_array[:]
[0, 0, 0, 0]
>>> short_array[7]
Traceback (most recent call last):
    ...
IndexError: invalid index
>>>

```

A different route to variable-sized data types in `ctypes` is to lean on Python’s dynamism and (re)define the data type once you actually know the required size, deciding case by case.

[Subject index](INDEX.md) · [Previous](surprises.md) · [Continue](ctypes-util-find-library.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md)
