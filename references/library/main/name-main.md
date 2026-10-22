# __main__ — `__name__ == '__main__'`

### `__name__ == '__main__'`

Importing a Python module or package assigns the module's name to `__name__`. As a rule, that name matches the Python file itself with the `.py` extension stripped off:

```python
>>> import configparser
>>> configparser.__name__
'configparser'

```

When the file belongs to a package, `__name__` carries the parent package's path as well:

```python
>>> from concurrent.futures import process
>>> process.__name__
'concurrent.futures.process'

```

If, on the other hand, the module runs inside the top-level code environment, its `__name__` becomes the string `'__main__'`.

[Subject index](INDEX.md) · [Previous](main-top-level-code-environment.md) · [Continue](what-is-the-top-level-code-environment.md) · [Owning module, declaration or section: __main__](main-top-level-code-environment.md)
