# What's New In Python 3.6 / PEP 487: Descriptor Protocol Enhancements

### PEP 487: Descriptor Protocol Enhancements

[**PEP 487**](https://peps.python.org/pep-0487/) widens the descriptor protocol with a fresh optional [`__set_name__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__set_name__) method. As each class is defined, this method runs against every descriptor present in that definition, handing it a reference to the class under construction together with the name assigned to the descriptor inside the class namespace. Put differently, a descriptor instance can finally discover what attribute name it holds in the owning class:

```python
class IntField:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f'expecting integer in {self.name}')
        instance.__dict__[self.name] = value

    # this is the new initializer:
    def __set_name__(self, owner, name):
        self.name = name

class Model:
    int_field = IntField()

```

See also

[**PEP 487**](https://peps.python.org/pep-0487/): Simpler customization of class creation

PEP written and implemented by Martin Teichmann.

[Feature documentation](https://docs.python.org/3.14/reference/datamodel.html#descriptors)

[Subject index](INDEX.md) · [Previous source section](pep-487-simpler-customization-of-class-creation.md) · [Next source section](pep-519-adding-a-file-system-path-protocol.md) · [Release/subject declaration](summary-release-highlights.md)
