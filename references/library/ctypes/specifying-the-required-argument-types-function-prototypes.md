# ctypes - Specifying the required argument types (function prototypes)

### Specifying the required argument types (function prototypes)

You may declare the required argument types for functions exported from DLLs by assigning the `argtypes` attribute.

`argtypes` has to be a sequence of C data types (the `printf()` function is admittedly a poor choice for illustration here, since it accepts a varying count and assortment of parameters governed by the format string, though on the flip side it makes for handy experimentation with this feature):

```python
>>> printf.argtypes = [c_char_p, c_char_p, c_int, c_double]
>>> printf(b"String '%s', Int %d, Double %f\n", b"Hi", 10, 2.2)
String 'Hi', Int 10, Double 2.200000
37
>>>

```

Declaring a format guards against mismatched argument types (in the same way a prototype does for a C function) and attempts to coerce the arguments into valid types:

```python
>>> printf(b"%d %d %d", 1, 2, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ctypes.ArgumentError: argument 2: TypeError: 'int' object cannot be interpreted as ctypes.c_char_p
>>> printf(b"%s %d %f\n", b"X", 2, 3)
X 2 3.000000
13
>>>

```

If you have written your own classes that you pass into function calls, you need to give them a `from_param()` class method so they qualify for use within the `argtypes` sequence. The `from_param()` class method is handed the Python object passed to the function call; it should run a typecheck or any other validation needed to confirm the object is acceptable, then return the object itself, its `_as_parameter_` attribute, or whatever you intend to pass as the C function argument in that situation. As before, the result needs to be an integer, string, bytes, a `ctypes` instance, or an object carrying an `_as_parameter_` attribute.

[Subject index](INDEX.md) · [Previous](calling-functions-with-your-own-custom-data-types.md) · [Continue](return-types.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md)
