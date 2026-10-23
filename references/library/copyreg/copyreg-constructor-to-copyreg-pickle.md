# copyreg`copyreg` - Register `pickle` support functions

## copyreg - Register pickle support functions

### `copyreg` - Register `pickle` support functions

**Source code:** [Lib/copyreg.py](https://github.com/python/cpython/tree/3.14/Lib/copyreg.py)

---

A mechanism for declaring functions to call while pickling particular objects is what the `copyreg` module provides. Those functions are then consulted by the [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) and [`copy`](https://docs.python.org/3.14/library/copy.html#module-copy) modules whenever such objects are pickled or copied. It also records configuration about object constructors that are not themselves classes — constructors that might be factory functions or instances of a class.

 copyreg.constructor(*object*)

Registers *object* as an acceptable constructor. Should *object* not be callable — and therefore unusable as a constructor — a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is thrown.

 copyreg.pickle(*type*, *function*, *constructor_ob=None*)

States that *function* is to serve as the “reduction” function for objects whose type is *type*. What *function* returns has to be either a string or a tuple of two through six elements. The [`dispatch_table`](https://docs.python.org/3.14/library/pickle.html#pickle.Pickler.dispatch_table) spells out *function*'s interface in more depth.

Left over from older versions, the *constructor_ob* parameter is disregarded these days, though when you do pass it, it has to be callable.

Keep in mind that you can likewise declare reduction functions via the [`dispatch_table`](https://docs.python.org/3.14/library/pickle.html#pickle.Pickler.dispatch_table) attribute on a pickler object or on a subclass of [`pickle.Pickler`](https://docs.python.org/3.14/library/pickle.html#pickle.Pickler).

[Subject index](INDEX.md) · [Continue](example.md)
