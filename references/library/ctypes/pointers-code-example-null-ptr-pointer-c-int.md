# ctypes — Pointers — Code example: >>> null_ptr = POINTER(c_int)()

```python
>>> null_ptr = POINTER(c_int)()
>>> print(bool(null_ptr))
False
>>>

```

When you dereference a pointer, `ctypes` verifies it is not `NULL` (though dereferencing a bad non-`NULL` pointer would still crash Python):

```python
>>> null_ptr[0]
Traceback (most recent call last):
    ....
ValueError: NULL pointer access
>>>

>>> null_ptr[0] = 1234
Traceback (most recent call last):
    ....
ValueError: NULL pointer access
>>>

```

[Subject index](INDEX.md) · [Previous](pointers-section-introduction-and-initial-examples.md) · [Continue](thread-safety-without-the-gil.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md) · [Owning module, declaration or section: Pointers](pointers-section-introduction-and-initial-examples.md)
