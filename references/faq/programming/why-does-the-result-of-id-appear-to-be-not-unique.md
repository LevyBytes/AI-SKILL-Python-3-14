# Why does the result of `id()` appear to be not unique?

### Why does the result of `id()` appear to be not unique?

The [`id()`](https://docs.python.org/3.14/library/functions.html#id) builtin hands back an integer promised to be unique for as long as the object lives. Because that value is the object’s memory address under CPython, it’s common that once an object leaves memory, the very next object created lands at that same memory location. The following example shows this:

```python
>>> id(1000)
13901272
>>> id(2000)
13901272

```

Those two ids correspond to separate integer objects, each built just before and discarded right after the `id()` call runs. To guarantee the objects you’re inspecting the id of remain alive, hold an extra reference to each:

```python
>>> a = 1000; b = 2000
>>> id(a)
13901272
>>> id(b)
13891296

```

[Subject index](INDEX.md)
