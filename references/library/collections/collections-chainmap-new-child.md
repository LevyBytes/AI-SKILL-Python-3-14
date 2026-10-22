# collections.ChainMap: `new_child()`

maps

A list of mappings that the user can update. Its order runs from first-searched down to last-searched. This list is the sole state retained, and editing it changes which mappings get searched. At minimum, the list should hold one mapping at all times.

 new_child(*m=None*, ***kwargs*)

Produces a fresh `ChainMap` whose first map is new and is followed by every map from the present instance. When `m` is given, it serves as the new leading map in the mapping list; when omitted, an empty dict takes its place, making the call `d.new_child()` the same as: `ChainMap({}, *d.maps)`. Any keyword arguments supplied update the passed map or the new empty dict. The purpose of this method is to build subcontexts that you can update without disturbing values held in any parent mapping.

Changed in version 3.4: The optional `m` parameter was added.

Changed in version 3.10: Keyword arguments support was added.

 parents

A property that yields a fresh `ChainMap` holding every map from the present instance apart from the first. This helps when you want to bypass the leading map during the search. The scenarios resemble those of the [`nonlocal`](https://docs.python.org/3.14/reference/simple_stmts.html#nonlocal) keyword as used within [nested scopes](https://docs.python.org/3.14/glossary.html#term-nested-scope). They also mirror the scenarios for the built-in [`super()`](https://docs.python.org/3.14/library/functions.html#super) function. Referencing `d.parents` amounts to: `ChainMap(*d.maps[1:])`.

Be aware that a `ChainMap` iterates in an order set by scanning its mappings from last to first:

```python
>>> baseline = {'music': 'bach', 'art': 'rembrandt'}
>>> adjustments = {'art': 'van gogh', 'opera': 'carmen'}
>>> list(ChainMap(adjustments, baseline))
['music', 'art', 'opera']

```

You wind up with the same ordering produced by a run of [`dict.update()`](https://docs.python.org/3.14/library/stdtypes.html#dict.update) calls begun from the final mapping:

```python
>>> combined = baseline.copy()
>>> combined.update(adjustments)
>>> list(combined)
['music', 'art', 'opera']

```

Changed in version 3.9: Added support for `|` and `|=` operators, specified in [**PEP 584**](https://peps.python.org/pep-0584/).

See also

- The [MultiContext class](https://github.com/enthought/codetools/blob/4.0.0/codetools/contexts/multi_context.py) found in Enthought's [CodeTools package](https://github.com/enthought/codetools) offers options for writing to any mapping along the chain.

- For templating, Django's [Context class](https://github.com/django/django/blob/main/django/template/context.py) is a read-only chain of mappings. It also offers pushing and popping of contexts much like the `new_child()` method and the `parents` property.

- The [Nested Contexts recipe](https://code.activestate.com/recipes/577434-nested-contexts-a-chain-of-mapping-objects/) provides options for deciding whether writes and other mutations affect only the first mapping or any mapping in the chain.

- A [greatly simplified read-only version of Chainmap](https://code.activestate.com/recipes/305268/).

[Subject index](INDEX.md) · [Previous](collections-chainmap-class.md) · [Continue](chainmap-examples-and-recipes.md) · [Owning module, declaration or section: collections](collections-container-datatypes.md) · [Owning module, declaration or section: collections.ChainMap](collections-chainmap-class.md) · [Owning module, declaration or section: `ChainMap` objects](collections-chainmap-class.md)
