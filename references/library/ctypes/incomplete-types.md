# ctypes — Incomplete Types

### Incomplete Types

*Incomplete Types* are structures, unions, or arrays whose members have not been spelled out yet. C handles them through forward declarations, with the actual definition supplied afterward:

```python
struct cell; /* forward declaration */

struct cell {
    char *name;
    struct cell *next;
};

```

The obvious port of that into ctypes code looks like the following, but it fails:

```python
>>> class cell(Structure):
...     _fields_ = [("name", c_char_p),
...                 ("next", POINTER(cell))]
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in cell
NameError: name 'cell' is not defined
>>>

```

The reason is that the freshly created `class cell` isn’t yet visible from inside its own class statement. With `ctypes`, the fix is to declare the `cell` class first and attach the `_fields_` attribute afterward, once the class statement has finished:

```python
>>> from ctypes import *
>>> class cell(Structure):
...     pass
...
>>> cell._fields_ = [("name", c_char_p),
...                  ("next", POINTER(cell))]
>>>

```

Let’s give it a go. We make two `cell` instances, wire them to reference one another, and then walk the pointer chain several times:

```python
>>> c1 = cell()
>>> c1.name = b"foo"
>>> c2 = cell()
>>> c2.name = b"bar"
>>> c1.next = pointer(c2)
>>> c2.next = pointer(c1)
>>> p = c1
>>> for i in range(8):
...     print(p.name, end=" ")
...     p = p.next[0]
...
foo bar foo bar foo bar foo bar
>>>

```

[Subject index](INDEX.md) · [Previous](type-conversions.md) · [Continue](callback-functions-section-introduction-and-initial-examples.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md)
