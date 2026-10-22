# When I edit an imported module and reimport it, the changes don’t show up. Why does this happen?

### When I edit an imported module and reimport it, the changes don’t show up. Why does this happen?

Both for speed and for consistency, Python loads a module's file only the first occasion it gets imported. Were that not the case, in a program made up of many modules that each import the same foundational one, that foundational module would be parsed over and over. To compel Python to re-read a module you've altered, do the following:

```python
import importlib
import modname
importlib.reload(modname)

```

Warning: this trick isn't 100% reliable. Specifically, any module that holds statements such as:

```python
from modname import some_objects

```

will keep referencing the prior version of whatever it imported. And when a module defines classes, instances created earlier are *not* migrated to the freshly reloaded class definition. That mismatch can produce behaviour that looks contradictory:

```python
>>> import importlib
>>> import cls
>>> c = cls.C()                # Create an instance of C
>>> importlib.reload(cls)
<module 'cls' from 'cls.py'>
>>> isinstance(c, cls.C)       # isinstance is false?!?
False

```

What's really going on becomes obvious once you display the “identity” of each class object:

```python
>>> hex(id(c.__class__))
'0x7352a0'
>>> hex(id(cls.C))
'0x4198d0'

```

[Subject index](INDEX.md)
