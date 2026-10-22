# How does Python manage memory?

### How does Python manage memory?

How Python manages memory hinges on the implementation. Python's standard implementation, [CPython](https://docs.python.org/3.14/glossary.html#term-CPython), relies on reference counting to spot objects that can no longer be reached, plus a separate mechanism for collecting reference cycles, running a cycle detection algorithm on a periodic basis that hunts for unreachable cycles and removes the objects they contain. The [`gc`](https://docs.python.org/3.14/library/gc.html#module-gc) module supplies functions to trigger a garbage collection, gather debugging statistics, and adjust the collector's parameters.

Other implementations (for instance [Jython](https://www.jython.org) or [PyPy](https://pypy.org)), on the other hand, may depend on a different mechanism, such as a full-blown garbage collector. That distinction can give rise to some subtle porting issues when your Python code leans on the behavior of the reference counting implementation.

Under some Python implementations, the code below (which behaves fine in CPython) will likely exhaust the available file descriptors:

```python
for file in very_long_list_of_files:
    f = open(file)
    c = f.read(1)

```

Indeed, with CPython's reference counting and destructor scheme, every fresh assignment to `f` shuts the prior file. Under a traditional GC, however, those file objects get collected (and closed) only at irregular and potentially lengthy intervals.

To write code that functions under any Python implementation, you should close the file explicitly or rely on the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement; this holds up no matter the memory management scheme:

```python
for file in very_long_list_of_files:
    with open(file) as f:
        c = f.read(1)

```

[Subject index](INDEX.md)
