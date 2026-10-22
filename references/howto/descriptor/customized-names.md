# Customized names

### Customized names

A class built on descriptors is able to tell each descriptor the variable name under which it was stored.

Here, the `Person` class holds two descriptor instances, *name* and *age*. As the `Person` class is being defined, it triggers a callback to [`__set_name__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__set_name__) within *LoggedAccess*, allowing the field names to be captured and giving each descriptor a distinct *public_name* and *private_name*:

```python
import logging

logging.basicConfig(level=logging.INFO)

class LoggedAccess:

    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        value = getattr(obj, self.private_name)
        logging.info('Accessing %r giving %r', self.public_name, value)
        return value

    def __set__(self, obj, value):
        logging.info('Updating %r to %r', self.public_name, value)
        setattr(obj, self.private_name, value)

class Person:

    name = LoggedAccess()                # First descriptor instance
    age = LoggedAccess()                 # Second descriptor instance

    def __init__(self, name, age):
        self.name = name                 # Calls the first descriptor
        self.age = age                   # Calls the second descriptor

    def birthday(self):
        self.age += 1

```

An interactive session verifies that the `Person` class invoked [`__set_name__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__set_name__) so the field names were captured. We use [`vars()`](https://docs.python.org/3.14/library/functions.html#vars) here to fetch the descriptor without firing it:

```pycon
>>> vars(vars(Person)['name'])
{'public_name': 'name', 'private_name': '_name'}
>>> vars(vars(Person)['age'])
{'public_name': 'age', 'private_name': '_age'}

```

This revised class now records access to *name* as well as *age*:

```pycon
>>> pete = Person('Peter P', 10)
INFO:root:Updating 'name' to 'Peter P'
INFO:root:Updating 'age' to 10
>>> kate = Person('Catherine C', 20)
INFO:root:Updating 'name' to 'Catherine C'
INFO:root:Updating 'age' to 20

```

Each of the two *Person* instances holds nothing but the private names:

```pycon
>>> vars(pete)
{'_name': 'Peter P', '_age': 10}
>>> vars(kate)
{'_name': 'Catherine C', '_age': 20}

```

[Subject index](INDEX.md) · [Previous source context](managed-attributes.md) · [Following source context](closing-thoughts.md)
