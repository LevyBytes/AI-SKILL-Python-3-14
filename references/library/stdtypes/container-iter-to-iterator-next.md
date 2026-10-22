# Iterator Types

### Iterator Types

Python embraces the notion of iterating across containers. Two separate methods implement this, and they let user-defined classes participate in iteration. Sequences, covered more fully further down, invariably support these iteration methods.

To make a container object an [iterable](https://docs.python.org/3.14/glossary.html#term-iterable), exactly one method has to be defined:

 container.__iter__()

Hand back an [iterator](https://docs.python.org/3.14/glossary.html#term-iterator) object. That object must honour the iterator protocol laid out below. Where a container offers several kinds of iteration, you can add further methods that explicitly ask for iterators tied to those particular iteration kinds. (A tree structure, for instance, that allows both breadth-first and depth-first traversal would be an object offering more than one form of iteration.) Within the Python/C API, this method corresponds to the [`tp_iter`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_iter) slot on the type structure used for Python objects.

The iterator objects must in turn provide the two methods below, which jointly make up the *iterator protocol*:

 iterator.__iter__()

Hand back the [iterator](https://docs.python.org/3.14/glossary.html#term-iterator) object itself. This is necessary so that both containers and iterators can serve with the [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) and [`in`](https://docs.python.org/3.14/reference/expressions.html#in) statements. Over in the Python/C API, this method lines up with the [`tp_iter`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_iter) slot belonging to the type structure that backs Python objects.

 iterator.__next__()

Hand back the next item out of the [iterator](https://docs.python.org/3.14/glossary.html#term-iterator). Once nothing remains, raise the [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) exception. Inside the Python/C API, this method answers to the [`tp_iternext`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_iternext) slot found on the type structure for Python objects.

Python ships a number of iterator objects to drive iteration over both general and particular sequence types, dictionaries, and assorted more specialised structures. What distinguishes those concrete types matters little aside from their adherence to the iterator protocol.

After an iterator's `__next__()` method has raised [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration), every later call has to keep raising it as well. Any implementation that ignores this rule is considered broken.

[Subject index](INDEX.md) · [Previous](boolean-type-bool.md) · [Continue](generator-types.md)
