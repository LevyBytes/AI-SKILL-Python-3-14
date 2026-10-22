# Python 2.6 changes: Core language changes and new syntax

### Other Language Changes

A few of the more minor adjustments made to the core Python language:

- You can now run a directory or a zip archive that holds a `__main__.py` file straight away by handing its name to the interpreter. That directory or zip archive is slotted in automatically as sys.path’s first entry. (Andy Chu offered the suggestion and an initial patch, which Phillip J. Eby and Nick Coghlan later reworked; [bpo-1739468](https://bugs.python.org/issue?@action=redirect&bpo=1739468).)

- The [`hasattr()`](https://docs.python.org/3.14/library/functions.html#hasattr) function used to swallow and ignore every error, on the premise that any error meant a `__getattr__()` method had failed in some way and that `hasattr()` should accordingly come back `False`. That reasoning ought not extend to [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt) and [`SystemExit`](https://docs.python.org/3.14/library/exceptions.html#SystemExit), though; from Python 2.6 onward, `hasattr()` no longer throws such exceptions away when it meets them. (Fixed by Benjamin Peterson; [bpo-2196](https://bugs.python.org/issue?@action=redirect&bpo=2196).)

- Supplying keyword arguments to a function call through the `**` syntax no longer obliges you to pass a Python dictionary; any mapping now does the job:

```python
>>> def f(**kw):
...    print sorted(kw)
...
>>> ud=UserDict.UserDict()
>>> ud['a'] = 1
>>> ud['b'] = 'string'
>>> f(**ud)
['a', 'b']

```

(Contributed by Alexander Belopolsky; [bpo-1686487](https://bugs.python.org/issue?@action=redirect&bpo=1686487).)

Supplying keyword arguments following a `*args` argument in a function call has likewise become valid.

```python
>>> def f(*args, **kw):
...     print args, kw
...
>>> f(1,2,3, *(4,5,6), keyword=13)
(1, 2, 3, 4, 5, 6) {'keyword': 13}

```

In earlier versions this would have triggered a syntax error. (Contributed by Amaury Forgeot d’Arc; [bpo-3473](https://bugs.python.org/issue?@action=redirect&bpo=3473).)

- There is a new builtin, `next(iterator, [default])`, which yields the next element of the iterator you name. Supply the *default* argument and it gets returned once *iterator* runs dry; leave it out and the [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) exception is raised instead. (Backported in [bpo-2719](https://bugs.python.org/issue?@action=redirect&bpo=2719).)

- Tuples gain [`index()`](https://docs.python.org/3.14/library/stdtypes.html#tuple.index) and [`count()`](https://docs.python.org/3.14/library/stdtypes.html#tuple.count) methods that mirror the list type’s [`index()`](https://docs.python.org/3.14/library/stdtypes.html#list.index) and [`count()`](https://docs.python.org/3.14/library/stdtypes.html#list.count) methods:

```python
>>> t = (0,1,2,3,4,0,1,2)
>>> t.index(3)
3
>>> t.count(0)
2

```

(Contributed by Raymond Hettinger)

- The built-in types handle extended slicing notation far better now, taking assorted blends of `(start, stop, step)`. Earlier the coverage was incomplete and a few edge cases failed. (Implemented by Thomas Wouters.)

- Properties pick up three attributes — `getter`, `setter`, and `deleter` — that act as decorators offering handy shortcuts to attach a getter, setter, or deleter function onto an existing property. Here is how you would apply them:

[Subject index](INDEX.md) · [Previous source section](the-fractions-module.md) · [Next source section](other-language-changes-c-and-d.md) · [Release/subject declaration](python-3-0.md)
