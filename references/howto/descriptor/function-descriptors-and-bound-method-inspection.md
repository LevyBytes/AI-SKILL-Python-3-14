# Function descriptors, qualified names and bound-method introspection

Feeding the class below into the interpreter reveals the function descriptor at work:

```python
class D:
    def f(self):
         return self

class D2:
    pass

```

For the sake of introspection, the function carries a [qualified name](https://docs.python.org/3.14/glossary.html#term-qualified-name) attribute:

```pycon
>>> D.f.__qualname__
'D.f'

```

Reaching the function by way of the class dictionary skips [`__get__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__get__). It hands back the bare function object instead:

```python
>>> D.__dict__['f']
<function D.f at 0x00C45070>

```

A dotted access from a class invokes [`__get__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__get__), which simply returns the underlying function untouched:

```python
>>> D.f
<function D.f at 0x00C45070>

```

What's interesting happens with dotted access from an instance. That dotted lookup invokes [`__get__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__get__), and the result is a bound method object:

```python
>>> d = D()
>>> d.f
<bound method D.f of <__main__.D object at 0x00B18C90>>

```

Behind the scenes, the bound method keeps a hold of both the underlying function and the instance it is bound to:

```python
>>> d.f.__func__
<function D.f at 0x00C45070>

>>> d.f.__self__
<__main__.D object at 0x00B18C90>

```

Should you have ever puzzled over the origin of *self* in ordinary methods or *cls* in class methods, here is your answer!

[Subject index](INDEX.md) · [MethodType and Function descriptor binding](methodtype-and-function-descriptor-binding.md) · [Previous source context](methodtype-and-function-descriptor-binding.md) · [Following source context](kinds-of-methods.md)
