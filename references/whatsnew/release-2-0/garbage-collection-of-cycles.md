# What’s New in Python 2.0 / Garbage Collection of Cycles - gc

### Garbage Collection of Cycles

Python’s C implementation employs reference counting to carry out garbage collection. Each Python object keeps a tally of how many references point at it, updating that tally whenever references come into being or are torn down. As soon as the reference count hits zero, the object becomes unreachable, since accessing an object requires holding a reference to it, and a count of zero means no references remain anywhere.

Reference counting carries a few agreeable traits: it’s simple to grasp and to implement, and the resulting implementation is portable, reasonably quick, and cooperates well with other libraries that run their own memory management schemes. Reference counting’s chief drawback is that it occasionally fails to recognize that objects have become unreachable, which yields a memory leak. This arises when cycles of references are present.

Picture the most basic cycle imaginable, a class instance carrying a reference to itself:

```python
instance = SomeClass()
instance.myself = instance

```

Once those two lines of code above have run, the reference count of `instance` sits at 2; one reference originates from the variable called `'instance'`, and the second from the `myself` attribute of the instance.

Suppose the following line of code is `del instance` — what occurs? The reference count of `instance` drops by 1, leaving it at a reference count of 1; the reference held in the `myself` attribute persists. Even so, the instance can no longer be reached from Python code, and it would be eligible for deletion. Multiple objects can take part in a cycle when they hold references to one another, which causes every one of those objects to be leaked.

Python 2.0 remedies this by running, at intervals, a cycle detection algorithm that hunts for unreachable cycles and removes the objects caught up in them. A new [`gc`](https://docs.python.org/3.14/library/gc.html#module-gc) module offers functions for triggering a garbage collection, retrieving debugging statistics, and adjusting the collector’s parameters.

Executing the cycle detection algorithm consumes some time, and consequently introduces a bit of extra overhead. The expectation is that once we’ve built up experience with the cycle collection from running 2.0, Python 2.1 will manage to cut the overhead through careful tuning. Exactly how much performance is sacrificed isn’t yet clear, since benchmarking it is awkward and hinges heavily on how frequently the program creates and discards objects. Cycle detection can be turned off when Python is compiled, in case you can’t spare even a slight speed hit or suspect the cycle collection harbors bugs, by passing the `--without-cycle-gc` switch when you run the **configure** script.

Several people took on this problem and helped produce a fix. Toby Kelsey wrote an early implementation of the cycle detection approach. Eric Tiedemann proposed the current algorithm while visiting CNRI, and Guido van Rossum and Neil Schemenauer produced two separate implementations, which Neil afterward merged. A host of other folks contributed suggestions throughout; the March 2000 archives of the python-dev mailing list hold the bulk of the pertinent discussion, particularly in the threads named “Reference cycle collection for Python” and “Finalization again”.

[Subject index](INDEX.md) · [Previous source section](string-methods.md) · [Next source section](other-core-changes.md) · [Release/subject declaration](introduction.md)
