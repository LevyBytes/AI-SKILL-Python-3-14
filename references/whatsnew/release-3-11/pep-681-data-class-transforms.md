# What's New In Python 3.11 / PEP 681: Data class transforms — dataclasses, typing

> (Contributed by Jelle Zijlstra in [bpo-47088](https://bugs.python.org/issue?@action=redirect&bpo=47088). PEP written by Pradeep Kumar Srinivasan and Graham Bleaney.)

### PEP 681: Data class transforms

You can apply [`dataclass_transform`](https://docs.python.org/3.14/library/typing.html#typing.dataclass_transform) to a class, a metaclass, or even a function that is itself a decorator. Seeing `@dataclass_transform()` signals to a static type checker that the wrapped object does runtime "magic" reshaping a class so it picks up [`dataclass`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass)-style behaviors.

To illustrate:

```python
# The create_model decorator is defined by a library.
@typing.dataclass_transform()
def create_model(cls: Type[T]) -> Type[T]:
    cls.__init__ = ...
    cls.__eq__ = ...
    cls.__ne__ = ...
    return cls

# The create_model decorator can now be used to create new model classes:
@create_model
class CustomerModel:
    id: int
    name: str

c = CustomerModel(id=327, name="Eric Idle")

```

Consult [**PEP 681**](https://peps.python.org/pep-0681/) for the full treatment.

[Subject index](INDEX.md) · [Previous source section](pep-675-arbitrary-literal-string-type.md) · [Next source section](pep-563-may-not-be-the-future.md) · [Release/subject declaration](summary-release-highlights.md)
