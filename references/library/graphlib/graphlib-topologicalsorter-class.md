# graphlib: `graphlib.TopologicalSorter`

## graphlib - Functionality to operate with graph-like structures

### `graphlib` - Functionality to operate with graph-like structures

**Source code:** [Lib/graphlib.py](https://github.com/python/cpython/tree/3.14/Lib/graphlib.py)

---

 *class *graphlib.TopologicalSorter(*graph=None*)

Supplies the means to topologically sort a graph whose nodes are [hashable](https://docs.python.org/3.14/glossary.html#term-hashable).

A topological order is a linear arrangement of a graph’s vertices in which, for each directed edge u -> v running from vertex u to vertex v, vertex u precedes vertex v in the arrangement. As an illustration, the graph’s vertices might stand for tasks to carry out and the edges for constraints requiring one task to finish ahead of another; here, a topological ordering is simply a workable sequence for the tasks. A full topological ordering exists exactly when the graph contains no directed cycles — that is, when it is a directed acyclic graph.

When the optional *graph* argument is supplied it has to be a dictionary depicting a directed acyclic graph, with the keys serving as nodes and the values as iterables holding every predecessor of that node in the graph (those nodes with edges aimed at the node in the key). Further nodes can be added to the graph through the `add()` method.

Broadly, sorting a particular graph takes the steps below:

- Build an instance of the `TopologicalSorter` with an optional starting graph.

- Add further nodes onto the graph.

- Invoke `prepare()` on the graph.

- For as long as `is_active()` is `True`, loop over the nodes that `get_ready()` returns and process them. Invoke `done()` on each node once its processing wraps up.

Where all you need is an immediate sort of the graph’s nodes with no parallelism in the picture, the convenience method `TopologicalSorter.static_order()` can be applied directly:

```pycon
>>> graph = {"D": {"B", "C"}, "C": {"A"}, "B": {"A"}}
>>> ts = TopologicalSorter(graph)
>>> tuple(ts.static_order())
('A', 'C', 'B', 'D')

```

The class is built to readily accommodate parallel processing of nodes as each one becomes ready. For instance:

```python
topological_sorter = TopologicalSorter()

# Add nodes to 'topological_sorter'...

topological_sorter.prepare()
while topological_sorter.is_active():
    for node in topological_sorter.get_ready():
        # Worker threads or processes take nodes to work on off the
        # 'task_queue' queue.
        task_queue.put(node)

    # When the work for a node is done, workers put the node in
    # 'finalized_tasks_queue' so we can get more nodes to work on.
    # The definition of 'is_active()' guarantees that, at this point, at
    # least one node has been placed on 'task_queue' that hasn't yet
    # been passed to 'done()', so this blocking 'get()' must (eventually)
    # succeed.  After calling 'done()', we loop back to call 'get_ready()'
    # again, so put newly freed nodes on 'task_queue' as soon as
    # logically possible.
    node = finalized_tasks_queue.get()
    topological_sorter.done(node)

```

[Subject index](INDEX.md) · [Continue](topological-sorter-graph-and-ready-nodes.md)
