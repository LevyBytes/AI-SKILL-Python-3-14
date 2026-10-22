# How do you make an array in Python?

### How do you make an array in Python?

Use a list:

```python
["this", 1, "is", "an", "array"]

```

In terms of time complexity, lists match C or Pascal arrays; the key distinction is that a Python list is able to hold objects of many different types.

There is also the `array` module, which supplies methods for building arrays of fixed types with compact representations, though indexing them is slower than indexing lists. Note as well that [NumPy](https://numpy.org/) and other third-party packages define array-like structures with assorted characteristics too.

For Lisp-style linked lists, you can imitate *cons cells* by means of tuples:

```python
lisp_list = ("like",  ("this",  ("example", None) ) )

```

When mutability matters, you might use lists rather than tuples. Here the counterpart of a Lisp *car* is `lisp_list[0]` and the counterpart of *cdr* is `lisp_list[1]`. Only go this route if you're truly certain you need it, because it tends to run a good deal slower than using Python lists.

[Subject index](INDEX.md)
