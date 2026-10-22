# graphlib.TopologicalSorter: `add()`, `prepare()`, `is_active()`, `done()`, `get_ready()`

add(*node*, **predecessors*)

Insert a fresh node together with its predecessors into the graph. The *node* itself and every element of *predecessors* must be [hashable](https://docs.python.org/3.14/glossary.html#term-hashable).

When invoked several times with the same node argument, the dependency set becomes the union of all the dependencies handed in.

You may add a node carrying no dependencies (*predecessors* left out) or list a dependency more than once. Where a node not seen before appears among *predecessors*, it is added to the graph automatically with no predecessors of its own.

Throws [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when invoked after `prepare()`.

 prepare()

Flag the graph as complete and scan it for cycles. Should any cycle turn up, `CycleError` is raised, though `get_ready()` may still be used to draw out as many nodes as possible until cycles halt further progress. Once this function has been invoked, the graph is fixed, so no additional nodes can be added via `add()`.

A [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised when the sort has already been begun by `static_order()` or `get_ready()`.

Changed in version 3.14: provided the sort is not yet underway, `prepare()` may now be invoked repeatedly. In earlier releases doing so raised [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

 is_active()

Returns `True` when further progress remains possible and `False` otherwise. Progress remains possible so long as cycles are not blocking resolution and either there are still ready nodes that `TopologicalSorter.get_ready()` has not yet returned, or the count of nodes marked `TopologicalSorter.done()` falls short of the count that `TopologicalSorter.get_ready()` has returned.

This class’s [`__bool__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__bool__) method delegates to this function, so rather than:

```python
if ts.is_active():
    ...

```

you can simply write:

```python
if ts:
    ...

```

Throws [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when invoked without a prior call to `prepare()`.

 done(**nodes*)

Flags a set of nodes that `TopologicalSorter.get_ready()` returned as processed, which frees every successor of each node in *nodes* to be returned later on by a call to `TopologicalSorter.get_ready()`.

Throws [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when any node in *nodes* was already flagged as processed by an earlier call to this method, or when a node was never added to the graph through `TopologicalSorter.add()`, or when invoked without a prior call to `prepare()`, or when a node has not yet been returned by `get_ready()`.

 get_ready()

Returns a `tuple` holding every node that is ready. At first it returns all nodes that have no predecessors, and after those get flagged as processed via `TopologicalSorter.done()`, later calls return all the new nodes whose predecessors have already been processed. When no further progress is possible, empty tuples come back.

Throws [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when invoked without a prior call to `prepare()`.

[Subject index](INDEX.md) · [Previous](graphlib-topologicalsorter-class.md) · [Continue](graphlib-topologicalsorter-static-order.md) · [Owning module, declaration or section: graphlib](graphlib-topologicalsorter-class.md) · [Owning module, declaration or section: graphlib.TopologicalSorter](graphlib-topologicalsorter-class.md)
