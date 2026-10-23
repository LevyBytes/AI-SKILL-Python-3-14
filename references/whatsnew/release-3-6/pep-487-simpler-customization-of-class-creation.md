# What's New In Python 3.6 / PEP 487: Simpler customization of class creation

### PEP 487: Simpler customization of class creation

You can now shape how subclasses come into being without reaching for a metaclass. The fresh `__init_subclass__` classmethod fires on the base class each time a subclass appears:

```python
class PluginBase:
    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

class Plugin1(PluginBase):
    pass

class Plugin2(PluginBase):
    pass

```

So that zero-argument [`super()`](https://docs.python.org/3.14/library/functions.html#super) calls behave correctly inside [`__init_subclass__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init_subclass__) bodies, a custom metaclass has to forward the fresh `__classcell__` namespace entry along to `type.__new__` (per [Creating the class object](https://docs.python.org/3.14/reference/datamodel.html#class-object-creation)).

See also

[**PEP 487**](https://peps.python.org/pep-0487/): Simpler customization of class creation

PEP written and implemented by Martin Teichmann.

[Feature documentation](https://docs.python.org/3.14/reference/datamodel.html#class-customization)

[Subject index](INDEX.md) · [Previous source section](pep-530-asynchronous-comprehensions.md) · [Next source section](pep-487-descriptor-protocol-enhancements.md) · [Release/subject declaration](summary-release-highlights.md)
