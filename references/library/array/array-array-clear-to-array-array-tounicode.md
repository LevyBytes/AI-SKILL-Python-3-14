# array.array: `clear()`, `reverse()`, `tobytes()`, `tofile()`, `tolist()`, `tounicode()`

clear()

Clear every element out of the array.

Added in version 3.13.

 reverse()

Flip the array’s items so their order runs the other way.

 tobytes()

Turn the array into an array of machine values and yield the bytes form — precisely the byte sequence that the `tofile()` method would emit to a file.

Added in version 3.2: For the sake of clarity, `tostring()` became `tobytes()`.

 tofile(*f*, */*)

Emit every item (as machine values) out to the [file object](https://docs.python.org/3.14/glossary.html#term-file-object) *f*.

 tolist()

Turn the array into a plain list carrying the very same items.

 tounicode()

Turn the array into a Unicode string. Its type has to be `'u'` or `'w'`, failing which a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised. For an array of any other type, reach a Unicode string via `array.tobytes().decode(enc)`.

An array object renders as a string shaped like `array(typecode, initializer)`. When the array is empty the *initializer* drops out; otherwise it appears as a Unicode string if the *typecode* is `'u'` or `'w'`, and as a list of numbers in every other case. That string form is guaranteed to round-trip back into an array of matching type and value through [`eval()`](https://docs.python.org/3.14/library/functions.html#eval), provided the `array` class was brought in via `from array import array`. Should it hold the corresponding floating-point values, the `inf` and `nan` variables have to be defined as well. Examples:

```python
array('l')
array('w', 'hello \u2641')
array('l', [1, 2, 3, 4, 5])
array('d', [1.0, 2.0, 3.14, -inf, nan])

```

See also

Module [`struct`](https://docs.python.org/3.14/library/struct.html#module-struct)

Packs and unpacks binary data of mixed kinds.

[NumPy](https://numpy.org/)

A separate array type comes from the NumPy package.

[Subject index](INDEX.md) · [Previous](array-array-class-to-array-array-remove.md) · [Owning module, declaration or section: array](array-typecodes.md) · [Owning module, declaration or section: array.array](array-array-class-to-array-array-remove.md)
