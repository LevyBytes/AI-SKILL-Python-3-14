# ctypes — Pointers — Section introduction and initial examples

### Pointers

You obtain a pointer instance by invoking `pointer()` on a `ctypes` type:

```python
>>> from ctypes import *
>>> i = c_int(42)
>>> pi = pointer(i)
>>>

```

Each pointer instance carries a `contents` attribute that hands back the object the pointer refers to — here, the `i` object shown earlier:

```python
>>> pi.contents
c_long(42)
>>>

```

Be aware that `ctypes` lacks OOR (original object return); every time you read an attribute it builds a fresh, equivalent object:

```python
>>> pi.contents is i
False
>>> pi.contents is pi.contents
False
>>>

```

If you assign a different `c_int` instance to the pointer’s contents attribute, the pointer will then refer to the memory address where that instance lives:

```python
>>> i = c_int(99)
>>> pi.contents = i
>>> pi.contents
c_long(99)
>>>

```

You can also subscript pointer instances using integers:

```python
>>> pi[0]
99
>>>

```

Writing to an integer index updates the value being pointed at:

```python
>>> print(i)
c_long(99)
>>> pi[0] = 22
>>> print(i)
c_long(22)
>>>

```

Indexes other than 0 are allowed too, but tread carefully — exactly as in C, you can read or write any memory address you like. As a rule you reach for this only when a C function hands you a pointer and you *know* for certain it really refers to an array rather than to a lone value.

Under the hood, `pointer()` does more than just produce pointer instances; it first has to build the pointer *types*. The `POINTER()` function handles that: give it any `ctypes` type and it hands back a brand-new type:

```python
>>> PI = POINTER(c_int)
>>> PI
<class 'ctypes.LP_c_long'>
>>> PI(42)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: expected c_long instead of int
>>> PI(c_int(42))
<ctypes.LP_c_long object at 0x...>
>>>

```

Invoking the pointer type with no argument yields a `NULL` pointer. The boolean value of a `NULL` pointer is `False`:

[Subject index](INDEX.md) · [Previous](arrays.md) · [Continue](pointers-code-example-null-ptr-pointer-c-int.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md)
