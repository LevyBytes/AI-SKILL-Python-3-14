# dir

dir()

 dir(*object*, */*)

Called without arguments, hand back the list of names within the current local scope. Called with an argument, try to hand back a list of that object’s valid attributes.

When the object carries a method called [`__dir__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__dir__), that method gets invoked and has to return the list of attributes. Through this, objects that supply a custom [`__getattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__) or [`__getattribute__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattribute__) function can tailor how `dir()` presents their attributes.

When the object supplies no [`__dir__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__dir__), the function does what it can with the object’s [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__) attribute, where present, together with its type object. The list that results need not be exhaustive and can be off the mark whenever the object carries a custom [`__getattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__).

How the default `dir()` mechanism acts shifts according to the object type, since it aims for the most pertinent information over an exhaustive one:

- When the object is a module object, the list carries the names of that module’s attributes.

- When the object is a type or class object, the list carries the names of its attributes, and recursively those of its bases’ attributes.

- In every other case, the list carries the object’s own attribute names, the names of its class’s attributes, and recursively the attributes of its class’s base classes.

The list that comes out is sorted alphabetically. To illustrate:

```python
>>> import struct
>>> dir()   # show the names in the module namespace
['__builtins__', '__name__', 'struct']
>>> dir(struct)   # show the names in the struct module
['Struct', '__all__', '__builtins__', '__cached__', '__doc__', '__file__',
 '__initializing__', '__loader__', '__name__', '__package__',
 '_clearcache', 'calcsize', 'error', 'pack', 'pack_into',
 'unpack', 'unpack_from']
>>> class Shape:
...     def __dir__(self):
...         return ['area', 'perimeter', 'location']
...
>>> s = Shape()
>>> dir(s)
['area', 'location', 'perimeter']

```

Note

Since `dir()` exists mainly as a handy aid at an interactive prompt, it leans toward offering an interesting collection of names rather than a strictly or uniformly defined one, and the fine points of its behavior may shift between releases. As an example, metaclass attributes stay out of the result list whenever the argument is a class.

[Builtin task index](INDEX.md).
