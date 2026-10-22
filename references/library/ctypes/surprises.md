# ctypes — Surprises

### Surprises

`ctypes` has a few rough corners where the result isn’t quite what you’d anticipate.

Take the example below:

```python
>>> from ctypes import *
>>> class POINT(Structure):
...     _fields_ = ("x", c_int), ("y", c_int)
...
>>> class RECT(Structure):
...     _fields_ = ("a", POINT), ("b", POINT)
...
>>> p1 = POINT(1, 2)
>>> p2 = POINT(3, 4)
>>> rc = RECT(p1, p2)
>>> print(rc.a.x, rc.a.y, rc.b.x, rc.b.y)
1 2 3 4
>>> # now swap the two points
>>> rc.a, rc.b = rc.b, rc.a
>>> print(rc.a.x, rc.a.y, rc.b.x, rc.b.y)
3 4 3 4
>>>

```

Hmm. We surely thought that final statement would show `3 4 1 2`. So what went on? These are the stages of the `rc.a, rc.b = rc.b, rc.a` line shown above:

```python
>>> temp0, temp1 = rc.b, rc.a
>>> rc.a = temp0
>>> rc.b = temp1
>>>

```

Bear in mind that `temp0` and `temp1` are objects that still sit on top of the internal buffer of the `rc` object above. Hence running `rc.a = temp0` copies the buffer contents of `temp0` into `rc`’s buffer, which in turn alters the contents of `temp1`. As a result, the final assignment `rc.b = temp1` doesn’t produce the outcome you’d hope for.

Remember that pulling a sub-object out of a Structure, Union, or Array does not *copy* that sub-object; instead you get back a wrapper object that reaches into the root object’s underlying buffer.

Here’s a second example whose behavior may not match expectations:

```python
>>> s = c_char_p()
>>> s.value = b"abc def ghi"
>>> s.value
b'abc def ghi'
>>> s.value is s.value
False
>>>

```

Note

The value of an object created from `c_char_p` may only be assigned bytes or integers.

So why does it print `False`? A ctypes instance is an object that wraps a block of memory together with some [descriptor](https://docs.python.org/3.14/glossary.html#term-descriptor)s that reach into that memory’s contents. Putting a Python object into the memory block doesn’t store the object itself; rather, the `contents` of the object are stored. Each time you read the contents back, a new Python object gets constructed!

[Subject index](INDEX.md) · [Previous](accessing-values-exported-from-dlls.md) · [Continue](variable-sized-data-types.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md)
