# inspect: `inspect.getmembers()`, `inspect.getmembers_static()`, `inspect.getmodulename()`, `inspect.ismodule()`, `inspect.isclass()`, `inspect.ismethod()`

inspect.getmembers(*object*[, *predicate*])

Hand back every member of an object as a list of `(name, value)` pairs ordered by name. Supplying the optional *predicate* argument — invoked with the `value` object belonging to each member — limits the result to those members for which the predicate yields a true value.

Note

When the argument is a class, `getmembers()` surfaces class attributes coming from the metaclass only if those attributes appear in the metaclass' custom [`__dir__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__dir__).

 inspect.getmembers_static(*object*[, *predicate*])

Hand back every member of an object as a list of `(name, value)` pairs ordered by name, but without setting off any dynamic lookup through the descriptor protocol, __getattr__ or __getattribute__. A predicate may optionally restrict the returned members to those that satisfy it.

Note

There are members `getmembers` can fetch that `getmembers_static()` may miss (for instance, attributes built dynamically), and conversely it may surface members `getmembers` cannot (for instance, descriptors that raise AttributeError). In certain situations it hands back descriptor objects rather than the instance members.

Added in version 3.11.

 inspect.getmodulename(*path*)

Hand back the module name designated by the file *path*, leaving out any enclosing package names. The file's extension is compared against every entry in [`importlib.machinery.all_suffixes()`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.all_suffixes). On a match, the trailing path component is handed back with its extension stripped. Failing that, `None` comes back.

Be aware that this function yields a meaningful name *only* for genuine Python modules - paths that might point at Python packages will still hand back `None`.

Changed in version 3.3: The function now builds directly on [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib).

 inspect.ismodule(*object*)

Return `True` if the object is a module.

 inspect.isclass(*object*)

Return `True` for an object that is a class, be it built-in or written in Python code.

For [generic aliases](https://docs.python.org/3.14/library/stdtypes.html#types-genericalias) of classes — `list[int]` being one example — this function yields `False`.

 inspect.ismethod(*object*)

Return `True` if the object is a bound method written in Python.

Note

Take this class as an illustration:

```python
>>> class Greeter:
...     def say_hello(self):
...         print('hello!')

```

Reaching `say_hello` (a [function](https://docs.python.org/3.14/glossary.html#term-function) declared in the `Greeter` namespace) by way of an instance of the `Greeter` class yields a bound method, otherwise called an *instance method*:

```python
>>> instance = Greeter()

>>> instance.say_hello
<bound method Greeter.say_hello of <__main__.Greeter object ...>>
>>> ismethod(instance.say_hello)
True
>>> isfunction(instance.say_hello)
False

```

Reaching `say_hello` by way of the `Greeter` class hands back the function on its own. With that function, `ismethod()` yields `False`, whereas `isfunction()` yields `True`:

```python
>>> Greeter.say_hello
<function Greeter.say_hello at 0x7f7503854a90>
>>> ismethod(Greeter.say_hello)
False
>>> isfunction(Greeter.say_hello)
True

```

See [Methods](https://docs.python.org/3.14/library/stdtypes.html#typesmethods) for details.

[Subject index](INDEX.md) · [Previous](generator-qualified-name-and-yieldfrom-inspection.md) · [Continue](inspect-isfunction-to-inspect-isawaitable.md) · [Owning module, declaration or section: inspect](inspect-inspect-live-objects.md) · [Owning module, declaration or section: Types and members](types-and-members-section-introduction-and-initial-examples.md)
