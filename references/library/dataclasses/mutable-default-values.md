# dataclasses — Mutable default values

### Mutable default values

Default values for member variables are held by Python inside class attributes. Take the following example, which avoids dataclasses:

```python
class C:
    x = []
    def add(self, element):
        self.x.append(element)

o1 = C()
o2 = C()
o1.add(1)
o2.add(2)
assert o1.x == [1, 2]
assert o1.x is o2.x

```

As you would anticipate, both instances of class `C` end up sharing the very same class variable `x`.

Were the equivalent dataclass code valid (which it is not):

```python
@dataclass
class D:
    x: list = []      # This code raises ValueError
    def add(self, element):
        self.x.append(element)

```

the emitted code would resemble this:

```python
class D:
    x = []
    def __init__(self, x=x):
        self.x = x
    def add(self, element):
        self.x.append(element)

assert D().x is D().x

```

The trouble here mirrors the earlier example built on class `C`: any pair of class `D` instances that leave `x` unset at construction time wind up pointing at one shared copy of `x`. Dataclasses inherit this behavior because they lean on ordinary Python class creation. No reliable mechanism exists for Data Classes to spot this situation in general. What the `@dataclass` decorator does instead is raise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) on encountering an unhashable default parameter, working from the premise that an unhashable value is a mutable one. The safeguard is incomplete, yet it guards against a great many frequent mistakes.

Default factory functions give you a route to manufacture fresh instances of mutable types to serve as a field's default:

```python
@dataclass
class D:
    x: list = field(default_factory=list)

assert D().x is not D().x

```

Changed in version 3.11: Rather than singling out and forbidding objects whose type is [`list`](https://docs.python.org/3.14/library/stdtypes.html#list), [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict), or [`set`](https://docs.python.org/3.14/library/stdtypes.html#set), the rule now rejects any unhashable object as a default value, treating unhashability as a stand-in for mutability.

[Subject index](INDEX.md) · [Previous](default-factory-functions.md) · [Continue](descriptor-typed-fields.md) · [Owning module, declaration or section: dataclasses](dataclasses-data-classes.md)
