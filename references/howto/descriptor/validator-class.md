# Validator class

### Validator class

A validator is a descriptor governing managed attribute access. Before committing any data, it confirms that the incoming value satisfies assorted type and range constraints. Should those constraints fail, it throws an exception to halt data corruption right where it begins.

The `Validator` class below serves simultaneously as an [abstract base class](https://docs.python.org/3.14/glossary.html#term-abstract-base-class) and as a managed attribute descriptor:

```python
from abc import ABC, abstractmethod

class Validator(ABC):

    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass

```

Each custom validator should subclass `Validator` and provide a `validate()` method that checks whatever constraints apply.

[Subject index](INDEX.md) · [Previous source context](complete-practical-example.md) · [Following source context](custom-validators.md)
