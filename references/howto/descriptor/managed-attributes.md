# Managed attributes

### Managed attributes

Controlling access to instance data ranks among the most common applications of descriptors. The descriptor lives on a public attribute in the class dictionary, whereas the underlying data resides as a private attribute in the instance dictionary. Accessing the public attribute fires the descriptor’s [`__get__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__get__) and [`__set__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__set__) methods.

In the example below, *age* serves as the public attribute and *_age* as the private one. Each time the public attribute is touched, the descriptor records the lookup or the update:

```python
import logging

logging.basicConfig(level=logging.INFO)

class LoggedAgeAccess:

    def __get__(self, obj, objtype=None):
        value = obj._age
        logging.info('Accessing %r giving %r', 'age', value)
        return value

    def __set__(self, obj, value):
        logging.info('Updating %r to %r', 'age', value)
        obj._age = value

class Person:

    age = LoggedAgeAccess()             # Descriptor instance

    def __init__(self, name, age):
        self.name = name                # Regular instance attribute
        self.age = age                  # Calls __set__()

    def birthday(self):
        self.age += 1                   # Calls both __get__() and __set__()

```

An interactive session confirms that every touch of the managed *age* attribute is recorded, whereas the ordinary *name* attribute produces no log entry:

```pycon
>>> mary = Person('Mary M', 30)         # The initial age update is logged
INFO:root:Updating 'age' to 30
>>> dave = Person('David D', 40)
INFO:root:Updating 'age' to 40

>>> vars(mary)                          # The actual data is in a private attribute
{'name': 'Mary M', '_age': 30}
>>> vars(dave)
{'name': 'David D', '_age': 40}

>>> mary.age                            # Access the data and log the lookup
INFO:root:Accessing 'age' giving 30
30
>>> mary.birthday()                     # Updates are logged as well
INFO:root:Accessing 'age' giving 30
INFO:root:Updating 'age' to 31

>>> dave.name                           # Regular attribute lookup isn't logged
'David D'
>>> dave.age                            # Only the managed attribute is logged
INFO:root:Accessing 'age' giving 40
40

```

A significant drawback here is that the private name *_age* is baked directly into the *LoggedAgeAccess* class. As a result, every instance is limited to a single logged attribute whose name can never be altered. The next example resolves that shortcoming.

[Subject index](INDEX.md) · [Previous source context](dynamic-lookups.md) · [Following source context](customized-names.md)
