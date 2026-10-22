# 3.2.8.6. Built-in functions

#### 3.2.8.6. Built-in functions

A built-in function object wraps a C function. As examples of built-in functions, consider [`len()`](https://docs.python.org/3.14/library/functions.html#len) and [`math.sin()`](https://docs.python.org/3.14/library/math.html#math.sin) (where [`math`](https://docs.python.org/3.14/library/math.html#module-math) is a standard built-in module). It is the C function that fixes how many arguments there are and their types. Special read-only attributes:

- `__doc__` holds the function’s documentation string, or `None` when none is available. Refer to `function.__doc__`.

- `__name__` holds the function’s name. Refer to `function.__name__`.

- `__self__` carries the value `None` (though refer to the following item).

- `__module__` holds the name of whichever module defined the function, or `None` when that is unavailable. Refer to `function.__module__`.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](callable-types.md) · [Previous source section](asynchronous-generator-functions.md) · [Following source section](built-in-methods.md)
