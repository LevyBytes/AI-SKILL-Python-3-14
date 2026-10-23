# pickle - What can be pickled and unpickled?

### What can be pickled and unpickled?

The following types can be pickled:

- built-in constants (`None`, `True`, `False`, `Ellipsis`, and [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented));

- integers, floating-point numbers, complex numbers;

- strings, bytes, bytearrays;

- tuples, lists, sets, and dictionaries containing only picklable objects;

- functions (whether built-in or user-defined) reachable from a module's top level (defined with [`def`](https://docs.python.org/3.14/reference/compound_stmts.html#def), not [`lambda`](https://docs.python.org/3.14/reference/expressions.html#lambda));

- classes accessible from the top level of a module;

- instances of those classes whenever the value returned by `__getstate__()` is itself picklable (the Pickling Class Instances section covers this).

Trying to pickle unpicklable objects raises the `PicklingError` exception; when that occurs, an unspecified number of bytes may already have been written to the underlying file. Trying to pickle a deeply recursive data structure can blow past the maximum recursion depth, which raises a [`RecursionError`](https://docs.python.org/3.14/library/exceptions.html#RecursionError). You can cautiously lift this limit via [`sys.setrecursionlimit()`](https://docs.python.org/3.14/library/sys.html#sys.setrecursionlimit).

Remember that functions (whether built-in or user-defined) get pickled by fully [qualified name](https://docs.python.org/3.14/glossary.html#term-qualified-name) rather than by value. [2] As a result, only the function name is stored, together with the names of the containing module and classes. The function's code is not pickled, and neither are any of its function attributes. Consequently the defining module must be importable in the unpickling environment, and that module must hold the named object, or else an exception is raised. [3]

In the same way, classes are pickled by fully qualified name, so the same restrictions apply in the unpickling environment. Note that none of the class's code or data gets pickled, so in the example below the class attribute `attr` is not restored in the unpickling environment:

```python
class Foo:
    attr = 'A class attribute'

picklestring = pickle.dumps(Foo)

```

These restrictions explain why picklable functions and classes have to be defined at the top level of a module.

In the same way, pickling class instances does not drag their class's code and data along; only the instance data gets pickled. That is by design, so you can patch bugs in a class or extend it with methods and still load objects built under an older version of the class. When you anticipate long-lived objects that will outlast many class versions, it can be worthwhile to embed a version number in the objects, letting the class's `__setstate__()` method apply whatever conversions are needed.

[Subject index](INDEX.md) · [Previous](pickle-picklebuffer-class-to-pickle-picklebuffer-release.md) · [Continue](object-getnewargs-ex.md) · [Owning module, declaration or section: pickle](pickle-python-object-serialization.md)
