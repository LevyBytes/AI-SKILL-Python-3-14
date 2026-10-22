# 3.3.13. Special method lookup

### 3.3.13. Special method lookup

For user-defined classes, implicit calls to special methods are guaranteed to behave correctly only when defined on an object's type, not within the object's instance dictionary. That behaviour explains why the following code raises an exception:

```python
>>> class C:
...     pass
...
>>> c = C()
>>> c.__len__ = lambda: 5
>>> len(c)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'C' has no len()

```

The reasoning behind this behaviour stems from several special methods such as `__hash__()` and `__repr__()` that every object implements, including type objects. Were the implicit lookup of these methods to follow the ordinary lookup process, they would fail when called on the type object itself:

```python
>>> 1 .__hash__() == hash(1)
True
>>> int.__hash__() == hash(int)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: descriptor '__hash__' of 'int' object needs an argument

```

Mistakenly trying to invoke an unbound method of a class in this manner is occasionally called 'metaclass confusion', and it is sidestepped by bypassing the instance while looking up special methods:

```python
>>> type(1).__hash__(1) == hash(1)
True
>>> type(int).__hash__(int) == hash(int)
True

```

Beyond skipping any instance attributes for the sake of correctness, implicit special method lookup typically also skips the `__getattribute__()` method even of the object's metaclass:

```python
>>> class Meta(type):
...     def __getattribute__(*args):
...         print("Metaclass getattribute invoked")
...         return type.__getattribute__(*args)
...
>>> class C(object, metaclass=Meta):
...     def __len__(self):
...         return 10
...     def __getattribute__(*args):
...         print("Class getattribute invoked")
...         return object.__getattribute__(*args)
...
>>> c = C()
>>> c.__len__()                 # Explicit lookup via instance
Class getattribute invoked
10
>>> type(c).__len__(c)          # Explicit lookup via type
Metaclass getattribute invoked
10
>>> len(c)                      # Implicit lookup
10

```

Sidestepping the `__getattribute__()` machinery this way opens up considerable room for the interpreter to run faster, though it sacrifices a degree of freedom in how special methods get handled (to be invoked dependably by the interpreter, the special method *must* live on the class object itself).

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Previous source section](object-annotate.md) · [Following source section](awaitable-objects.md)
