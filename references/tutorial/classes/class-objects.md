# 9.3.2. Class Objects

### 9.3.2. Class Objects

Two sorts of operation are available on class objects: attribute references and instantiation.

*Attribute references* follow the ordinary syntax Python uses for every attribute reference: `obj.name`. Legitimate attribute names are all of the names that were sitting in the class's namespace at the moment the class object came into being. So, given a class definition like this:

```python
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

```

then `MyClass.i` and `MyClass.f` count as valid attribute references, yielding an integer and a function object respectively. Class attributes can be assigned to as well, so you're free to alter the value of `MyClass.i` by assignment. [`__doc__`](https://docs.python.org/3.14/reference/datamodel.html#type.__doc__) is likewise a valid attribute, handing back the class's docstring: `"A simple example class"`.

Class *instantiation* employs function notation. Simply imagine the class object as a function taking no parameters that hands back a new instance of the class. For instance (taking the class above):

```python
x = MyClass()

```

builds a new *instance* of the class and assigns that object to the local variable `x`.

The instantiation operation (that is, "calling" a class object) yields an empty object. Plenty of classes prefer to make objects whose instances start out tailored to some particular initial state. A class may therefore supply a special method called [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__), like so:

```python
def __init__(self):
    self.data = []

```

Whenever a class supplies an [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) method, instantiating the class automatically calls `__init__()` on the freshly built class instance. So in this case, you can get a new, initialized instance with:

```python
x = MyClass()

```

Naturally, the [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) method can accept arguments for added flexibility. When it does, the arguments handed to the class instantiation operator are forwarded along to `__init__()`. For instance,

```python
>>> class Complex:
...     def __init__(self, realpart, imagpart):
...         self.r = realpart
...         self.i = imagpart
...
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)

```

[Subject index](INDEX.md) · [Previous source section](class-definition-syntax.md) · [Following source section](instance-objects.md)
