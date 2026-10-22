# graphlib.TopologicalSorter: `static_order()`

static_order()

Returns an iterator object that walks the nodes in a topological order. While using this method, you should not call `prepare()` or `done()`. This method amounts to:

```python
def static_order(self):
    self.prepare()
    while self.is_active():
        node_group = self.get_ready()
        yield from node_group
        self.done(*node_group)

```

Which particular order comes back can hinge on the exact order the items were inserted into the graph. For instance:

```pycon
>>> ts = TopologicalSorter()
>>> ts.add(3, 2, 1)
>>> ts.add(1, 0)
>>> print([*ts.static_order()])
[2, 0, 1, 3]

>>> ts2 = TopologicalSorter()
>>> ts2.add(1, 0)
>>> ts2.add(3, 2, 1)
>>> print([*ts2.static_order()])
[0, 2, 1, 3]

```

This happens because “0” and “2” sit at the same level in the graph (they would have come back from the same call to `get_ready()`), and their relative order is fixed by the insertion order.

Should any cycle turn up, `CycleError` is raised.

Added in version 3.9.

[Subject index](INDEX.md) · [Previous](topological-sorter-graph-and-ready-nodes.md) · [Continue](graphlib-cycleerror.md) · [Owning module, declaration or section: graphlib](graphlib-topologicalsorter-class.md) · [Owning module, declaration or section: graphlib.TopologicalSorter](graphlib-topologicalsorter-class.md)
