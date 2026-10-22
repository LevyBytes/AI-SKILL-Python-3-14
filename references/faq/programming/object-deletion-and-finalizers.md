# My class defines __del__ but it is not called when I delete the object.

### My class defines __del__ but it is not called when I delete the object.

A handful of explanations could account for this.

The [`del`](https://docs.python.org/3.14/reference/simple_stmts.html#del) statement won’t automatically trigger [`__del__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__del__) – all it does is lower the object’s reference count by one, and `__del__()` runs only once that count hits zero.

When your data structures hold circular links (say, a tree in which every child points to its parent and every parent keeps a list of its children), the reference counts can never fall back to zero. Every so often Python runs an algorithm that finds such cycles, but the garbage collector may not fire until some time after the final reference to your structure disappears, so your `__del__()` method could run at a random and awkward moment. That makes reproducing a bug harder. Worse still, the sequence in which various objects’ `__del__()` methods run is arbitrary. Calling [`gc.collect()`](https://docs.python.org/3.14/library/gc.html#gc.collect) forces a collection, but there *are* pathological cases in which objects are never collected.

Even with the cycle collector around, it remains wise to give objects an explicit `close()` method you can invoke once you’re finished with them. That `close()` method can then drop attributes pointing at subobjects. Avoid calling `__del__()` yourself – instead `__del__()` should call `close()`, and `close()` should be safe to invoke repeatedly on the same object.

A further tactic for dodging cyclical references is the [`weakref`](https://docs.python.org/3.14/library/weakref.html#module-weakref) module, which lets you reference objects without bumping their reference count. Tree structures, for example, ought to hold weak references for their parent and sibling links (where such links are actually needed!).

Lastly, should your `__del__()` method throw an exception, a warning message goes to [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr).

[Subject index](INDEX.md)
