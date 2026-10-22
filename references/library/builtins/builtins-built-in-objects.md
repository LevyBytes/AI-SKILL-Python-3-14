# builtins — `builtins` — Built-in objects

## builtins — Built-in objects

### `builtins` — Built-in objects

---

Through this module you get direct access to every one of Python's 'built-in' identifiers; for instance, `builtins.open` is the fully qualified name of the built-in function [`open()`](https://docs.python.org/3.14/library/functions.html#open).

Most applications don't reach for this module by name as a matter of course, yet it earns its keep in modules that expose objects sharing a built-in value's name while still needing the built-in of that name. As an illustration, a module aiming to supply an [`open()`](https://docs.python.org/3.14/library/functions.html#open) function that wraps the built-in `open()` can lean on this module directly:

```python
import builtins

def open(path):
    f = builtins.open(path, 'r')
    return UpperCaser(f)

class UpperCaser:
    '''Wrapper around a file that converts output to uppercase.'''

    def __init__(self, f):
        self._f = f

    def read(self, count=-1):
        return self._f.read(count).upper()

    # ...

```

As a matter of implementation, most modules find the name `__builtins__` placed within their globals. What `__builtins__` holds is ordinarily either this module itself or the value of this module's [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__) attribute. Being an implementation detail, it isn't guaranteed to be present in other implementations of Python.

See also

- [Built-in Constants](https://docs.python.org/3.14/library/constants.html#built-in-consts)

- [Built-in Exceptions](https://docs.python.org/3.14/library/exceptions.html#bltin-exceptions)

- [Built-in Functions](https://docs.python.org/3.14/library/functions.html#built-in-funcs)

- [Built-in Types](https://docs.python.org/3.14/library/stdtypes.html#bltin-types)

[Subject index](INDEX.md)
