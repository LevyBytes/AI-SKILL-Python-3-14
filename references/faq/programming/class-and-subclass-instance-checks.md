# How do I check if an object is an instance of a given class or of a subclass of it?

### How do I check if an object is an instance of a given class or of a subclass of it?

Reach for the built-in function [`isinstance(obj, cls)`](https://docs.python.org/3.14/library/functions.html#isinstance). To test membership against several classes at once, hand it a tuple in place of one class, as in `isinstance(obj, (class1, class2, ...))`; you can equally test against one of Python’s built-in types, such as `isinstance(obj, str)` or `isinstance(obj, (int, float, complex))`.

Be aware that [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) honors virtual inheritance from an [abstract base class](https://docs.python.org/3.14/glossary.html#term-abstract-base-class) as well. Because of that, a registered class yields `True` even when it never inherited from the base directly or transitively. For a check of “true inheritance”, walk the [method resolution order](https://docs.python.org/3.14/glossary.html#term-method-resolution-order) (MRO) of the class:

```python
from collections.abc import Mapping

class P:
     pass

class C(P):
    pass

Mapping.register(P)

```

```pycon
>>> c = C()
>>> isinstance(c, C)        # direct
True
>>> isinstance(c, P)        # indirect
True
>>> isinstance(c, Mapping)  # virtual
True

# Actual inheritance chain
>>> type(c).__mro__
(<class 'C'>, <class 'P'>, <class 'object'>)

# Test for "true inheritance"
>>> Mapping in type(c).__mro__
False

```

Keep in mind that calling [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) against classes you wrote yourself is uncommon in most programs. When you own the classes, a cleaner object-oriented design is to give them methods that capture a specific behaviour, rather than inspecting an object’s class and branching on whatever class it turns out to be. Suppose, for instance, you have a function that performs some task:

```python
def search(obj):
    if isinstance(obj, Mailbox):
        ...  # code to search a mailbox
    elif isinstance(obj, Document):
        ...  # code to search a document
    elif ...

```

The preferable route is to give every class a `search()` method and simply invoke it:

```python
class Mailbox:
    def search(self):
        ...  # code to search a mailbox

class Document:
    def search(self):
        ...  # code to search a document

obj.search()

```

[Subject index](INDEX.md)
