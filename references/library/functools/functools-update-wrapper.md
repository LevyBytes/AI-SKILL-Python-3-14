# functools: `functools.update_wrapper()`, `functools.wraps()`

functools.update_wrapper(*wrapper*, *wrapped*, *assigned=WRAPPER_ASSIGNMENTS*, *updated=WRAPPER_UPDATES*)

Adjusts a *wrapper* function so that it resembles the *wrapped* one. Its optional arguments are tuples that say which attributes of the original function get copied straight onto the wrapper function's matching attributes, and which of the wrapper function's attributes get refreshed using the original function's equivalents. Those arguments default to the module-level constants `WRAPPER_ASSIGNMENTS` (responsible for assigning the wrapper function's [`__module__`](https://docs.python.org/3.14/reference/datamodel.html#function.__module__), [`__name__`](https://docs.python.org/3.14/reference/datamodel.html#function.__name__), [`__qualname__`](https://docs.python.org/3.14/reference/datamodel.html#function.__qualname__), [`__annotations__`](https://docs.python.org/3.14/reference/datamodel.html#function.__annotations__), [`__type_params__`](https://docs.python.org/3.14/reference/datamodel.html#function.__type_params__), and [`__doc__`](https://docs.python.org/3.14/reference/datamodel.html#function.__doc__), the documentation string) together with `WRAPPER_UPDATES` (responsible for refreshing the wrapper function's [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#function.__dict__), that is, its instance dictionary).

So that the original function stays reachable for introspection and similar needs (for example, sidestepping a caching decorator like `lru_cache()`), this routine tacks a `__wrapped__` attribute onto the wrapper on its own, and that attribute points back at the function under wrap.

Where this routine is chiefly meant to be applied is inside [decorator](https://docs.python.org/3.14/glossary.html#term-decorator) functions, the ones that wrap a decorated function and then hand back the wrapper. Leave the wrapper function un-updated and the returned function's metadata will mirror the wrapper's own definition instead of the original's — an outcome that is rarely of any use.

You are free to apply `update_wrapper()` to callables that are not functions. Whenever an attribute listed in *assigned* or *updated* is absent from the object being wrapped, it is simply skipped — the routine makes no effort to place it on the wrapper function. Even so, [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) still gets raised should the wrapper function itself lack any attribute named in *updated*.

Changed in version 3.2: The `__wrapped__` attribute now gets added on its own. By default the [`__annotations__`](https://docs.python.org/3.14/reference/datamodel.html#function.__annotations__) attribute is now copied across. Absent attributes no longer set off an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError).

Changed in version 3.4: From now on the `__wrapped__` attribute consistently points at the wrapped function, even where that function had a `__wrapped__` attribute of its own. (see [bpo-17482](https://bugs.python.org/issue?@action=redirect&bpo=17482))

Changed in version 3.12: By default the [`__type_params__`](https://docs.python.org/3.14/reference/datamodel.html#function.__type_params__) attribute now gets copied over.

 @functools.wraps(*wrapped*, *assigned=WRAPPER_ASSIGNMENTS*, *updated=WRAPPER_UPDATES*)

Think of this as a shortcut that calls `update_wrapper()` in the guise of a function decorator while you are writing a wrapper function. It amounts to the same thing as `partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated)`. As an illustration:

```python
>>> from functools import wraps
>>> def my_decorator(f):
...     @wraps(f)
...     def wrapper(*args, **kwds):
...         print('Calling decorated function')
...         return f(*args, **kwds)
...     return wrapper
...
>>> @my_decorator
... def example():
...     """Docstring"""
...     print('Called example function')
...
>>> example()
Calling decorated function
Called example function
>>> example.__name__
'example'
>>> example.__doc__
'Docstring'

```

Had this decorator factory not been employed, the example function would have ended up named `'wrapper'`, and the docstring belonging to the original `example()` would have vanished.

[Subject index](INDEX.md) · [Previous](functools-singledispatchmethod-class.md) · [Continue](partial-func-to-partial-keywords.md) · [Owning module, declaration or section: functools](cached-factorial-and-dataset-examples.md)
