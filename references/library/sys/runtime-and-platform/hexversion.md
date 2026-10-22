# sys.hexversion

sys.hexversion

The version number packed into one integer. It is guaranteed to climb with each successive version, and it handles non-production releases correctly too. For instance, to check that the Python interpreter is at least version 1.5.2, write:

```python
if sys.hexversion >= 0x010502F0:
    # use some advanced feature
    ...
else:
    # use an alternative implementation or warn the user
    ...

```

The name `hexversion` comes from the fact that it only really makes sense once you view it as the output of feeding it to the built-in [`hex()`](https://docs.python.org/3.14/library/functions.html#hex) function. For a more human-friendly encoding of that same information, you can turn to the [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple) `sys.version_info`.

Further details about `hexversion` are available at [API and ABI Versioning](https://docs.python.org/3.14/c-api/apiabiversion.html#apiabiversion).

[API family](INDEX.md) · [sys context index](../INDEX.md).
