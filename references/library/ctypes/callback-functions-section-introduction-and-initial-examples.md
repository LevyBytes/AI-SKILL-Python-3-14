# ctypes - Callback functions - Section introduction and initial examples

### Callback functions

With `ctypes` you can turn Python callables into C-callable function pointers. People often refer to these as *callback functions*.

To begin, you have to define a class for the callback. That class captures the calling convention, the return type, and how many arguments — and of which types — the function will be handed.

For callbacks that use the `cdecl` calling convention, build their types with the `CFUNCTYPE()` factory function. On Windows, use the `WINFUNCTYPE()` factory function to build types for callbacks following the `stdcall` calling convention.

You call either factory with the result type as the first argument, followed by the argument types the callback is expected to receive as the rest of the arguments.

The example I’ll walk through relies on the C standard library’s `qsort()` function, which sorts items using a callback you provide. Here `qsort()` sorts an array of integers:

```python
>>> IntArray5 = c_int * 5
>>> ia = IntArray5(5, 1, 7, 33, 99)
>>> qsort = libc.qsort
>>> qsort.restype = None
>>>

```

You invoke `qsort()` with a pointer to the data being sorted, how many items the array holds, the size of a single item, and a pointer to the comparison routine — the callback. ctypes then calls that callback with two pointers to items, and it should return a negative integer when the first item ranks below the second, zero when they match, and a positive integer otherwise.

This means our callback gets pointers to integers and has to give back an integer. We start by building the `type` for the callback:

```python
>>> CMPFUNC = CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))
>>>

```

As a first step, here is a minimal callback that just prints the values handed to it:

```python
>>> def py_cmp_func(a, b):
...     print("py_cmp_func", a[0], b[0])
...     return 0
...
>>> cmp_func = CMPFUNC(py_cmp_func)
>>>

```

The outcome:

```python
>>> qsort(ia, len(ia), sizeof(c_int), cmp_func)
py_cmp_func 5 1
py_cmp_func 33 99
py_cmp_func 7 33
py_cmp_func 5 7
py_cmp_func 1 7
>>>

```

At this point we can perform the real comparison of the two items and hand back something meaningful:

```python
>>> def py_cmp_func(a, b):
...     print("py_cmp_func", a[0], b[0])
...     return a[0] - b[0]
...
>>>
>>> qsort(ia, len(ia), sizeof(c_int), CMPFUNC(py_cmp_func))
py_cmp_func 5 1
py_cmp_func 33 99
py_cmp_func 7 33
py_cmp_func 1 7
py_cmp_func 5 7
>>>

```

A quick check confirms the array is now in order:

```python
>>> for i in ia: print(i, end=" ")
...
1 5 7 33 99
>>>

```

[Subject index](INDEX.md) · [Previous](incomplete-types.md) · [Continue](ctypes-and-we-could-equally-have-written.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md)
