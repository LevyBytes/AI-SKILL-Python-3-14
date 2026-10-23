# ctypes - Calling functions, continued

### Calling functions, continued

Be aware that printf writes to the genuine standard output channel, *not* to [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout), so the examples here only function at the console prompt and will not work from inside *IDLE* or *PythonWin*:

```python
>>> printf = libc.printf
>>> printf(b"Hello, %s\n", b"World!")
Hello, World!
14
>>> printf(b"Hello, %S\n", "World!")
Hello, World!
14
>>> printf(b"%d bottles of beer\n", 42)
42 bottles of beer
19
>>> printf(b"%f bottles of beer\n", 42.5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ctypes.ArgumentError: argument 2: TypeError: Don't know how to convert parameter 2
>>>

```

As pointed out previously, every Python type aside from integers, strings, and bytes objects must be wrapped in the matching `ctypes` type so that it can be converted into the C data type required:

```python
>>> printf(b"An int %d, a double %f\n", 1234, c_double(3.14))
An int 1234, a double 3.140000
31
>>>

```

[Subject index](INDEX.md) · [Previous](ctypes-and-given-that-python-string-objects-cannot-be-mutated.md) · [Continue](calling-variadic-functions.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md)
