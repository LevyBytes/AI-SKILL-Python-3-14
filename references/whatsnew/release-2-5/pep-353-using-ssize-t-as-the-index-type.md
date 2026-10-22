# What's New in Python 2.5 / PEP 353: Using ssize_t as the index type

### PEP 353: Using ssize_t as the index type

An extensive revision to Python's C API — swapping in a new [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) type definition in place of int — will let the interpreter cope with larger amounts of data on 64-bit platforms. On 32-bit platforms, Python's capacity is unaffected by this change.

Throughout the Python interpreter, C's int type was used to keep sizes or counts; for instance, how many items a list or tuple held was kept in an int. On most 64-bit platforms the C compilers continue to define int as a 32-bit type, which meant lists were capped at `2**31 - 1` = 2147483647 items. (There happen to be several distinct programming models a 64-bit C compiler may adopt — refer to [https://unix.org/version2/whatsnew/lp64_wp.html](https://unix.org/version2/whatsnew/lp64_wp.html) for that discussion — but the model you'll most often encounter keeps int at 32 bits.)

On a 32-bit platform a ceiling of 2147483647 items is basically irrelevant, because memory will run out long before you reach that length. Every list slot needs room for a pointer — 4 bytes — together with room for a [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) standing for the item. 2147483647*4 already exceeds the number of bytes a 32-bit address space is able to hold.

On a 64-bit platform, though, addressing that volume of memory is feasible. A list of that magnitude would need only 16 GiB of space for its pointers, so it's perfectly plausible that Python programmers could build lists that big. The Python interpreter therefore had to switch away from int to a different type, one that on 64-bit platforms will be a 64-bit type. Since the change introduces incompatibilities on 64-bit machines, it was judged worthwhile to make the move now, while 64-bit users remain comparatively few. (Within 5 or 10 years, perhaps *every* one of us will run 64-bit machines, and the transition would hurt more by then.)

Authors of C extension modules feel the brunt of this change. Python strings together with container types like lists and tuples now rely on [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) to record their size. Functions like [`PyList_Size()`](https://docs.python.org/3.14/c-api/list.html#c.PyList_Size) now hand back `Py_ssize_t`. As a result, extension-module code may need certain variables switched over to `Py_ssize_t`.

A new conversion code, `n`, for [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) has been added to the [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple) and [`Py_BuildValue()`](https://docs.python.org/3.14/c-api/arg.html#c.Py_BuildValue) functions. By default `PyArg_ParseTuple()`'s `s#` and `t#` keep producing int, yet defining the `PY_SSIZE_T_CLEAN` macro ahead of including `Python.h` makes them yield `Py_ssize_t` instead.

[**PEP 353**](https://peps.python.org/pep-0353/) contains a section of conversion guidelines that extension authors ought to study to understand how to support 64-bit platforms.

See also

[**PEP 353**](https://peps.python.org/pep-0353/) - Using ssize_t as the index type

PEP authored and implemented by Martin von Löwis.

[Subject index](INDEX.md) · [Previous source section](pep-352-exceptions-as-new-style-classes.md) · [Next source section](pep-357-the-index-method.md) · [Release/subject declaration](pep-308-conditional-expressions.md)
