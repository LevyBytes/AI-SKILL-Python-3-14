# pickle - Restricting Globals

### Restricting Globals

By default, unpickling imports whatever class or function it runs across in the pickle data. For plenty of applications that is unacceptable, since it lets the unpickler import and run arbitrary code. Just look at what this hand-crafted pickle data stream does once it is loaded:

```python
>>> import pickle
>>> pickle.loads(b"cos\nsystem\n(S'echo hello world'\ntR.")
hello world
0

```

Here the unpickler imports the [`os.system()`](https://docs.python.org/3.14/library/os.html#os.system) function and then applies it to the string argument "echo hello world". Harmless as this example is, it takes little imagination to picture one that could wreck your system.

Because of this, you may wish to govern what gets unpickled by customizing `Unpickler.find_class()`. Despite what the name implies, `Unpickler.find_class()` runs whenever a global (a class or a function) is requested. That makes it possible either to ban globals entirely or to narrow them down to a safe subset.

What follows is an unpickler that permits loading only a handful of safe classes from the [`builtins`](https://docs.python.org/3.14/library/builtins.html#module-builtins) module:

```python
import builtins
import io
import pickle

safe_builtins = {
    'range',
    'complex',
    'set',
    'frozenset',
    'slice',
}

class RestrictedUnpickler(pickle.Unpickler):

    def find_class(self, module, name):
        # Only allow safe classes from builtins.
        if module == "builtins" and name in safe_builtins:
            return getattr(builtins, name)
        # Forbid everything else.
        raise pickle.UnpicklingError("global '%s.%s' is forbidden" %
                                     (module, name))

def restricted_loads(s):
    """Helper function analogous to pickle.loads()."""
    return RestrictedUnpickler(io.BytesIO(s)).load()

```

An illustration of the unpickler above doing its job correctly:

```python
>>> restricted_loads(pickle.dumps([1, 2, range(15)]))
[1, 2, range(0, 15)]
>>> restricted_loads(b"cos\nsystem\n(S'echo hello world'\ntR.")
Traceback (most recent call last):
  ...
pickle.UnpicklingError: global 'os.system' is forbidden
>>> restricted_loads(b'cbuiltins\neval\n'
...                  b'(S\'getattr(__import__("os"), "system")'
...                  b'("echo hello world")\'\ntR.')
Traceback (most recent call last):
  ...
pickle.UnpicklingError: global 'builtins.eval' is forbidden

```

These examples make clear that you must exercise caution over which things you permit to be unpickled. So when security matters, it is worth weighing other approaches — for instance the marshalling API found in [`xmlrpc.client`](https://docs.python.org/3.14/library/xmlrpc.client.html#module-xmlrpc.client), or solutions provided by third parties.

[Subject index](INDEX.md) · [Previous](example.md) · [Owning module, declaration or section: pickle](pickle-python-object-serialization.md) · [Continue](performance.md)
