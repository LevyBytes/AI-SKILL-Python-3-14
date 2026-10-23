# dataclasses - Descriptor-typed fields

### Descriptor-typed fields

When a field receives a [descriptor object](https://docs.python.org/3.14/reference/datamodel.html#descriptors) as its default, the following special behaviors come into play:

- Whatever value is handed for the field to the dataclass's [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) method gets routed into the descriptor's [`__set__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__set__) method instead of clobbering the descriptor object.

- In the same way, reading or writing the field triggers a call to the descriptor's [`__get__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__get__) or `__set__()` method in place of handing back or replacing the descriptor object.

- To find out whether a field carries a default, `@dataclass` invokes the descriptor's `__get__()` method through its class-access form, namely `descriptor.__get__(obj=None, type=cls)`. A value returned by the descriptor here becomes that field's default. Conversely, should the descriptor throw [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) under these circumstances, the field is left without any default value.

```python
class IntConversionDescriptor:
    def __init__(self, *, default):
        self._default = default

    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, obj, type):
        if obj is None:
            return self._default

        return getattr(obj, self._name, self._default)

    def __set__(self, obj, value):
        setattr(obj, self._name, int(value))

@dataclass
class InventoryItem:
    quantity_on_hand: IntConversionDescriptor = IntConversionDescriptor(default=100)

i = InventoryItem()
print(i.quantity_on_hand)   # 100
i.quantity_on_hand = 2.5    # calls __set__ with 2.5
print(i.quantity_on_hand)   # 2

```

Bear in mind that a field carrying a descriptor-type annotation, yet given no descriptor object as its default, simply behaves the way an ordinary field would.

[Subject index](INDEX.md) · [Previous](mutable-default-values.md) · [Owning module, declaration or section: dataclasses](dataclasses-data-classes.md)
