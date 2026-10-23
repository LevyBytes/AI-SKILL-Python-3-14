# weakref - Comparing finalizers with `__del__()` methods

### Comparing finalizers with [`__del__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__del__) methods

Imagine we wish to build a class whose instances stand for temporary directories. Each directory, along with everything inside it, ought to be deleted the moment the earliest of these events happens:

- the object is garbage collected,

- the object's `remove()` method gets called, or

- the program exits.

A first attempt at the class might rely on a [`__del__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__del__) method, like so:

```python
class TempDir:
    def __init__(self):
        self.name = tempfile.mkdtemp()

    def remove(self):
        if self.name is not None:
            shutil.rmtree(self.name)
            self.name = None

    @property
    def removed(self):
        return self.name is None

    def __del__(self):
        self.remove()

```

From Python 3.4 onward, [`__del__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__del__) methods no longer block reference cycles from being garbage collected, and module globals are no longer coerced to [`None`](https://docs.python.org/3.14/library/constants.html#None) during [interpreter shutdown](https://docs.python.org/3.14/glossary.html#term-interpreter-shutdown). So on CPython this code ought to run without trouble.

That said, how [`__del__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__del__) methods are handled is famously implementation-specific, hinging as it does on the inner workings of the interpreter's garbage collector.

A sturdier route is to define a finalizer that touches only the particular functions and objects it actually requires, instead of having the run of the object's whole state:

```python
class TempDir:
    def __init__(self):
        self.name = tempfile.mkdtemp()
        self._finalizer = weakref.finalize(self, shutil.rmtree, self.name)

    def remove(self):
        self._finalizer()

    @property
    def removed(self):
        return not self._finalizer.alive

```

Set up this way, our finalizer is handed a reference only to the specifics it needs in order to clean up the directory properly. Even if the object is never garbage collected, the finalizer still fires at exit.

A further upside of weakref-based finalizers is that they let you enroll finalizers for classes whose definition belongs to a third party — for instance, to run code at the point a module is unloaded:

```python
import weakref, sys
def unloading_module():
    # implicit reference to the module globals from the function body
weakref.finalize(sys.modules[__name__], unloading_module)

```

Note

Should you spin up a finalizer object inside a daemonic thread right as the program is exiting, there is a chance the finalizer never fires at exit. Then again, within a daemonic thread neither [`atexit.register()`](https://docs.python.org/3.14/library/atexit.html#atexit.register), `try: ... finally: ...`, nor `with: ...` promises that cleanup will happen either.

[Subject index](INDEX.md) · [Previous](finalizer-objects.md) · [Owning module, declaration or section: weakref](weakref-ref-class.md)
