# Dynamic lookups

### Dynamic lookups

Useful descriptors usually perform computations rather than handing back fixed values:

```python
import os

class DirectorySize:

    def __get__(self, obj, objtype=None):
        return len(os.listdir(obj.dirname))

class Directory:

    size = DirectorySize()              # Descriptor instance

    def __init__(self, dirname):
        self.dirname = dirname          # Regular instance attribute

```

An interactive session demonstrates the dynamic nature of the lookup — each call recomputes a fresh, current result:

```python
>>> s = Directory('songs')
>>> g = Directory('games')
>>> s.size                              # The songs directory has twenty files
20
>>> g.size                              # The games directory has three files
3
>>> os.remove('games/chess')            # Delete a game
>>> g.size                              # File count is automatically updated
2

```

Beyond demonstrating that descriptors can perform computations, this example also clarifies what the arguments to [`__get__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__get__) are for. The *self* parameter is *size*, an instance of *DirectorySize*. The *obj* parameter resolves to either *g* or *s*, an instance of *Directory*. The *obj* parameter is precisely what enables the `__get__()` method to identify the directory of interest. The *objtype* parameter holds the class *Directory*.

[Subject index](INDEX.md) · [Previous source context](simple-example-a-descriptor-that-returns-a-constant.md) · [Following source context](managed-attributes.md)
