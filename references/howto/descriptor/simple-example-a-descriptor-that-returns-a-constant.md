# Simple example: A descriptor that returns a constant

### Simple example: A descriptor that returns a constant

The `Ten` class acts as a descriptor whose [`__get__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__get__) method consistently hands back the constant `10`:

```python
class Ten:
    def __get__(self, obj, objtype=None):
        return 10

```

For the descriptor to take effect, you must place it as a class variable inside some other class:

```python
class A:
    x = 5                       # Regular class attribute
    y = Ten()                   # Descriptor instance

```

An interactive session highlights how ordinary attribute lookup differs from descriptor lookup:

```pycon
>>> a = A()                     # Make an instance of class A
>>> a.x                         # Normal attribute lookup
5
>>> a.y                         # Descriptor lookup
10

```

During the `a.x` attribute lookup, the dot operator locates `'x': 5` within the class dictionary. During the `a.y` lookup, the dot operator instead encounters a descriptor instance, identified by its `__get__` method. Invoking that method yields `10`.

Observe that neither the class dictionary nor the instance dictionary holds the value `10`. Rather, `10` gets calculated when requested.

While this illustrates the basic mechanics of a descriptor, it has little practical value. Plain attribute lookup would serve better when fetching constants.

The following section builds something more genuinely useful: a dynamic lookup.

[Subject index](INDEX.md) · [Previous source context](primer.md) · [Following source context](dynamic-lookups.md)
