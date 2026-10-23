# ctypes - Calling functions with your own custom data types

### Calling functions with your own custom data types

You can additionally tailor the way `ctypes` converts arguments so that instances of your own classes may serve as function arguments. `ctypes` searches for an `_as_parameter_` attribute and treats its value as the function argument. That attribute has to be an integer, string, bytes, a `ctypes` instance, or an object that itself carries an `_as_parameter_` attribute:

```python
>>> class Bottles:
...     def __init__(self, number):
...         self._as_parameter_ = number
...
>>> bottles = Bottles(42)
>>> printf(b"%d bottles of beer\n", bottles)
42 bottles of beer
19
>>>

```

Should you prefer not to keep the instance's data inside the `_as_parameter_` instance variable, you can instead define a [`property`](https://docs.python.org/3.14/library/functions.html#property) that produces the attribute on demand.

[Subject index](INDEX.md) · [Previous](calling-variadic-functions.md) · [Continue](specifying-the-required-argument-types-function-prototypes.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md)
