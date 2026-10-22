# repr

repr(*object*, */*)

Hand back a string holding a printable depiction of an object. With a lot of types, this function tries to give back a string that — fed to `eval()` — would recreate an object of equal value; failing that, the depiction is a string wrapped in angle brackets naming the object's type plus extra details, commonly the object's name and address. A class governs what this function yields for its instances by supplying a [`__repr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__repr__) method. Should [`sys.displayhook()`](https://docs.python.org/3.14/library/sys.html#sys.displayhook) be unreachable, the function raises [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

The class below carries a custom representation suitable for evaluation:

```python
class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def __repr__(self):
      return f"Person('{self.name}', {self.age})"

```

[Builtin task index](INDEX.md).
