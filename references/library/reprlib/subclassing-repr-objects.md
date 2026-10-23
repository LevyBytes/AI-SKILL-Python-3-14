# reprlib - Subclassing Repr Objects

### Subclassing Repr Objects

Because `Repr.repr1()` dispatches dynamically, subclasses of `Repr` can extend support to extra built-in object types or change how already-supported types are handled. The example here demonstrates how dedicated support for file objects might be added:

```python
import reprlib
import sys

class MyRepr(reprlib.Repr):

    def repr_TextIOWrapper(self, obj, level):
        if obj.name in {'<stdin>', '<stdout>', '<stderr>'}:
            return obj.name
        return repr(obj)

aRepr = MyRepr()
print(aRepr.repr(sys.stdin))         # prints '<stdin>'

```

```none
<stdin>

```

[Subject index](INDEX.md) · [Previous](repr-indent-to-repr-repr-type.md) · [Owning module, declaration or section: reprlib](reprlib-repr-class-to-reprlib-repr.md)
