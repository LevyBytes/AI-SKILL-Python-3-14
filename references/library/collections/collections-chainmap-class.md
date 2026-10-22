# collections: `collections.ChainMap`

### `ChainMap` objects

Added in version 3.3.

The `ChainMap` class exists to quickly tie together several mappings, letting you handle them as one combined object. This is frequently far quicker than building a fresh dictionary and applying several [`update()`](https://docs.python.org/3.14/library/stdtypes.html#dict.update) calls.

You can use the class to model nested scopes, and it proves handy in templating.

 *class *collections.ChainMap(**maps*)

By grouping together several dicts or comparable mappings, a `ChainMap` yields one combined, updateable view. When no *maps* get passed in, a lone empty dictionary is supplied, ensuring every new chain holds at least one mapping.

A list keeps the underlying mappings. That list is public, and you can read or change it through the *maps* attribute. Nothing else is held as state.

To resolve a lookup, the underlying mappings are scanned one after another until the key turns up. By contrast, writes, updates, and deletions touch only the first mapping.

Because a `ChainMap` holds the underlying mappings by reference, any update to one of those underlying mappings will show up in the `ChainMap`.

Every standard dictionary method works here. On top of that, there is the *maps* attribute, a method that builds new subcontexts, and a property that reaches every mapping save the first:

[Subject index](INDEX.md) · [Previous](collections-container-datatypes.md) · [Continue](collections-chainmap-new-child.md) · [Owning module, declaration or section: collections](collections-container-datatypes.md)
