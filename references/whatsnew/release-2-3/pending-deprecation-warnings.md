# What’s New in Python 2.3 / Other Language Changes — warnings

```python
>>> import types
>>> m = types.ModuleType('abc','docstring')
>>> m
<module 'abc' (built-in)>
>>> m.__doc__
'docstring'

```

- A new warning, [`PendingDeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#PendingDeprecationWarning), arrived to flag features on their way to being deprecated. By default this warning will *not* be shown. To spot usage of features slated for future deprecation, pass [`-Walways::PendingDeprecationWarning::`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-W) on the command line or call [`warnings.filterwarnings()`](https://docs.python.org/3.14/library/warnings.html#warnings.filterwarnings).

- Deprecation of string-based exceptions, like `raise "Error occurred"`, is underway. Raising a string now sets off [`PendingDeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#PendingDeprecationWarning).

- Taking `None` as a variable name now produces a [`SyntaxWarning`](https://docs.python.org/3.14/library/exceptions.html#SyntaxWarning) warning. Some later Python version may at last turn `None` into a keyword.

- The `xreadlines()` method on file objects, brought in with Python 2.1, is no longer needed, because files now act as their own iterator. `xreadlines()` first showed up as a quicker way to iterate over every line in a file, but these days you can just write `for line in file_obj`. File objects gained a new read-only `encoding` attribute as well, reporting the encoding the file uses; Unicode strings written to that file will be turned into bytes automatically with the named encoding.

- New-style classes changed how they compute method resolution order, but you'll spot the difference only with a genuinely tangled inheritance hierarchy. This change leaves classic classes untouched. Python 2.2 originally relied on a topological sort of a class's ancestors, whereas 2.3 now applies the C3 algorithm laid out in the paper [“A Monotonic Superclass Linearization for Dylan”](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.19.3910). For the reasoning behind the change, read Michele Simionato's article [The Python 2.3 Method Resolution Order](https://docs.python.org/3.14/howto/mro.html#python-2-3-mro), or follow the python-dev thread that begins with the message at [https://mail.python.org/pipermail/python-dev/2002-October/029035.html](https://mail.python.org/pipermail/python-dev/2002-October/029035.html). Samuele Pedroni was first to flag the problem and also supplied the fix by implementing the C3 algorithm.

- Python handles multithreaded programs by hopping between threads once it has run N bytecodes. N's default has gone up from 10 to 100 bytecodes, which speeds up single-threaded applications by cutting the switching overhead. A few multithreaded applications may see slower response time, but you can readily remedy that by lowering the limit again with `sys.setcheckinterval(N)`. The new `sys.getcheckinterval()` function fetches the current limit.

- One modest but far-reaching shift: for extension types that Python's bundled modules define, the type names now include the module followed by a `'.'` before the type name itself. As an example, under Python 2.2, building a socket and printing its `__class__` gave you this:

```python
>>> s = socket.socket()
>>> s.__class__
<type 'socket'>

```

Under 2.3, you get this:

```python
>>> s.__class__
<type '_socket.socket'>

```

- One of the well-known incompatibilities separating old- and new-style classes is gone: you can now assign to the [`__name__`](https://docs.python.org/3.14/reference/datamodel.html#type.__name__) and [`__bases__`](https://docs.python.org/3.14/reference/datamodel.html#type.__bases__) attributes of new-style classes. A few limits apply to what `__bases__` will accept, in the same spirit as those governing assignment to an instance's [`__class__`](https://docs.python.org/3.14/reference/datamodel.html#object.__class__) attribute.

[Subject index](INDEX.md) · [Previous source section](other-language-changes.md) · [Next source section](string-changes.md) · [Release/subject declaration](standard-set-type.md) · [Release/subject declaration](other-language-changes.md)
