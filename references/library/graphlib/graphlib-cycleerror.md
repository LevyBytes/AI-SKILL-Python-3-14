# graphlib — Exceptions

### Exceptions

The exception classes declared by the `graphlib` module are:

 *exception *graphlib.CycleError

A subclass of [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) that `TopologicalSorter.prepare()` raises when cycles are present in the working graph. Where several cycles are present, just one arbitrary pick among them gets reported and bundled into the exception.

You can reach the detected cycle through the second element of the exception instance’s [`args`](https://docs.python.org/3.14/library/exceptions.html#BaseException.args) attribute; it is a list of nodes in which each node is, within the graph, the immediate predecessor of the following node in the list. Within the reported list, the opening and closing node are identical, which signals that the path is cyclic.

[Subject index](INDEX.md) · [Previous](graphlib-topologicalsorter-static-order.md) · [Continue](../grp/grp-getgrgid-to-grp-getgrall.md) · [Owning module, declaration or section: graphlib](graphlib-topologicalsorter-class.md)
