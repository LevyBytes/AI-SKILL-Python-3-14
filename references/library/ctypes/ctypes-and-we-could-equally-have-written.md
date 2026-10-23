# ctypes - Callback functions - Contract: Because the function factories double as decorator factories, we could equally have written:

Because the function factories double as decorator factories, we could equally have written:

```python
>>> @CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))
... def py_cmp_func(a, b):
...     print("py_cmp_func", a[0], b[0])
...     return a[0] - b[0]
...
>>> qsort(ia, len(ia), sizeof(c_int), py_cmp_func)
py_cmp_func 5 1
py_cmp_func 33 99
py_cmp_func 7 33
py_cmp_func 1 7
py_cmp_func 5 7
>>>

```

Note

Be sure to hold on to references to your `CFUNCTYPE()` objects for the entire time C code might use them. `ctypes` won’t do this for you, and if you neglect it, they can be garbage collected — which crashes your program the moment the callback fires.

Keep in mind, too, that when the callback runs in a thread spun up outside of Python’s control (for instance by the foreign code invoking the callback), ctypes spawns a fresh dummy Python thread for each call. That is the right behavior in nearly every case, but it does mean that anything stored via [`threading.local`](https://docs.python.org/3.14/library/threading.html#threading.local) will *not* carry over between separate callbacks, even when the same C thread issues them.

[Subject index](INDEX.md) · [Previous](callback-functions-section-introduction-and-initial-examples.md) · [Continue](accessing-values-exported-from-dlls.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md) · [Owning module, declaration or section: Callback functions](callback-functions-section-introduction-and-initial-examples.md)
