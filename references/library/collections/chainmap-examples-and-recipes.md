# collections — `ChainMap` Examples and Recipes

### `ChainMap` Examples and Recipes

Here are several techniques for handling chained maps.

An example that mimics Python's internal lookup chain:

```python
import builtins
pylookup = ChainMap(locals(), globals(), vars(builtins))

```

An example that gives user-supplied command-line arguments priority over environment variables, which in their turn rank above default values:

```python
import os, argparse

defaults = {'color': 'red', 'user': 'guest'}

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v is not None}

combined = ChainMap(command_line_args, os.environ, defaults)
print(combined['color'])
print(combined['user'])

```

Sample patterns that employ the `ChainMap` class to emulate nested contexts:

```python
c = ChainMap()        # Create root context
d = c.new_child()     # Create nested child context
e = c.new_child()     # Child of c, independent from d
e.maps[0]             # Current context dictionary -- like Python's locals()
e.maps[-1]            # Root context -- like Python's globals()
e.parents             # Enclosing context chain -- like Python's nonlocals

d['x'] = 1            # Set value in current context
d['x']                # Get first key in the chain of contexts
del d['x']            # Delete from current context
list(d)               # All nested values
k in d                # Check all nested values
len(d)                # Number of nested values
d.items()             # All nested items
dict(d)               # Flatten into a regular dictionary

```

Although the `ChainMap` class confines its updates (writes and deletions) to the chain's first mapping while lookups span the whole chain, deep writes and deletions are simple to obtain: just write a subclass that revises keys located further down the chain:

```python
class DeepChainMap(ChainMap):
    'Variant of ChainMap that allows direct updates to inner scopes'

    def __setitem__(self, key, value):
        for mapping in self.maps:
            if key in mapping:
                mapping[key] = value
                return
        self.maps[0][key] = value

    def __delitem__(self, key):
        for mapping in self.maps:
            if key in mapping:
                del mapping[key]
                return
        raise KeyError(key)

>>> d = DeepChainMap({'zebra': 'black'}, {'elephant': 'blue'}, {'lion': 'yellow'})
>>> d['lion'] = 'orange'         # update an existing key two levels down
>>> d['snake'] = 'red'           # new keys get added to the topmost dict
>>> del d['elephant']            # remove an existing key one level down
>>> d                            # display result
DeepChainMap({'zebra': 'black', 'snake': 'red'}, {}, {'lion': 'orange'})

```

[Subject index](INDEX.md) · [Previous](collections-chainmap-new-child.md) · [Continue](collections-counter-class-to-collections-counter-class.md) · [Owning module, declaration or section: collections](collections-container-datatypes.md)
