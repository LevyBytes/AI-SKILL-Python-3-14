# gc: `gc.get_count()`, `gc.get_threshold()`, `gc.get_referrers()`, `gc.get_referents()`, `gc.is_tracked()`, `gc.is_finalized()`, `gc.freeze()`, `gc.unfreeze()`

gc.get_count()

Return the current collection counts as a tuple of `(count0, count1, count2)`.

 gc.get_threshold()

Return the current collection thresholds as a tuple of `(threshold0, threshold1, threshold2)`.

 gc.get_referrers(**objs*)

Hand back the list of objects that refer directly to any of objs. Only those containers offering garbage collection support will be found by this function; extension types that reference other objects yet lack garbage collection support won't turn up.

Keep in mind that objects already dereferenced — yet still residing in cycles that the garbage collector hasn't gotten around to collecting — may show up among the referrers you get back. If you want only objects that are currently live, run `collect()` ahead of calling `get_referrers()`.

Warning

Take care while handling objects that `get_referrers()` hands back, since a few of them might still be under construction and thus momentarily in an invalid state. Don't put `get_referrers()` to any use besides debugging.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `gc.get_referrers` with argument `objs`.

 gc.get_referents(**objs*)

Hand back a list of the objects that any of the arguments refer to directly. The referents you get back are the objects reached by the C-level [`tp_traverse`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_traverse) methods of the arguments (where present), and might not cover every object that is in fact directly reachable. Support for `tp_traverse` methods exists only on objects that support garbage collection, and those methods need only visit objects capable of taking part in a cycle. Thus, as an illustration, when an integer is directly reachable from an argument, that integer object might or might not show up in the result list.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `gc.get_referents` with argument `objs`.

 gc.is_tracked(*obj*)

Hands back `True` when the garbage collector is currently tracking the object, otherwise `False`. As a broad rule, instances of atomic types go untracked while instances of non-atomic types (containers, user-defined objects…) are tracked. That said, certain type-specific optimizations may apply so that the garbage collector overhead of simple instances is suppressed (for instance, dicts whose keys and values are all atomic):

```python
>>> gc.is_tracked(0)
False
>>> gc.is_tracked("a")
False
>>> gc.is_tracked([])
True
>>> gc.is_tracked({})
False
>>> gc.is_tracked({"a": 1})
True

```

Added in version 3.1.

 gc.is_finalized(*obj*)

Hands back `True` when the garbage collector has finalized the supplied object, otherwise `False`.

```python
>>> x = None
>>> class Lazarus:
...     def __del__(self):
...         global x
...         x = self
...
>>> lazarus = Lazarus()
>>> gc.is_finalized(lazarus)
False
>>> del lazarus
>>> gc.is_finalized(x)
True

```

Added in version 3.9.

 gc.freeze()

Freeze every object the garbage collector tracks; relocate them into a permanent generation and skip them in all collections to come.

When a process is going to `fork()` without an `exec()`, steering clear of needless copy-on-write inside child processes lets memory sharing reach its maximum and brings down total memory use. Doing this calls for both keeping freed "holes" from forming in the parent's memory pages and making sure GC collections in child processes leave the `gc_refs` counter of long-lived parent-originated objects alone. To achieve both, invoke `gc.disable()` early within the parent process, call `gc.freeze()` immediately before `fork()`, and run `gc.enable()` early within child processes.

Added in version 3.7.

 gc.unfreeze()

Thaw the objects sitting in the permanent generation, returning them to the oldest generation.

Added in version 3.7.

[Subject index](INDEX.md) · [Previous](gc-enable-to-gc-set-threshold.md) · [Continue](gc-get-freeze-count-to-gc-debug-leak.md) · [Owning module, declaration or section: gc](gc-enable-to-gc-set-threshold.md)
