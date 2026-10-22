# What’s New In Python 3.5 / inspect — inspect

### inspect

Pickling and hashing are now supported by both the [`Signature`](https://docs.python.org/3.14/library/inspect.html#inspect.Signature) and [`Parameter`](https://docs.python.org/3.14/library/inspect.html#inspect.Parameter) classes. (Contributed by Yury Selivanov in [bpo-20726](https://bugs.python.org/issue?@action=redirect&bpo=20726) and [bpo-20334](https://bugs.python.org/issue?@action=redirect&bpo=20334).)

Filling in default values for arguments that are absent is now possible via a new [`BoundArguments.apply_defaults()`](https://docs.python.org/3.14/library/inspect.html#inspect.BoundArguments.apply_defaults) method:

```python
>>> def foo(a, b='ham', *args): pass
>>> ba = inspect.signature(foo).bind('spam')
>>> ba.apply_defaults()
>>> ba.arguments
OrderedDict([('a', 'spam'), ('b', 'ham'), ('args', ())])

```

(Contributed by Yury Selivanov in [bpo-24190](https://bugs.python.org/issue?@action=redirect&bpo=24190).)

Subclassing [`Signature`](https://docs.python.org/3.14/library/inspect.html#inspect.Signature) is made simpler by a new class method, [`Signature.from_callable()`](https://docs.python.org/3.14/library/inspect.html#inspect.Signature.from_callable). (Contributed by Yury Selivanov and Eric Snow in [bpo-17373](https://bugs.python.org/issue?@action=redirect&bpo=17373).)

A *follow_wrapped* optional keyword argument is now taken by the [`signature()`](https://docs.python.org/3.14/library/inspect.html#inspect.signature) function; passing `False` turns off the automatic traversal of `__wrapped__` links. (Contributed by Yury Selivanov in [bpo-20691](https://bugs.python.org/issue?@action=redirect&bpo=20691).)

For examining [coroutine functions](https://docs.python.org/3.14/glossary.html#term-coroutine-function) and [coroutine objects](https://docs.python.org/3.14/glossary.html#term-coroutine), a group of new functions has arrived: [`iscoroutine()`](https://docs.python.org/3.14/library/inspect.html#inspect.iscoroutine), [`iscoroutinefunction()`](https://docs.python.org/3.14/library/inspect.html#inspect.iscoroutinefunction), [`isawaitable()`](https://docs.python.org/3.14/library/inspect.html#inspect.isawaitable), [`getcoroutinelocals()`](https://docs.python.org/3.14/library/inspect.html#inspect.getcoroutinelocals), and [`getcoroutinestate()`](https://docs.python.org/3.14/library/inspect.html#inspect.getcoroutinestate). (Contributed by Yury Selivanov in [bpo-24017](https://bugs.python.org/issue?@action=redirect&bpo=24017) and [bpo-24400](https://bugs.python.org/issue?@action=redirect&bpo=24400).)

Named tuples are now what the [`stack()`](https://docs.python.org/3.14/library/inspect.html#inspect.stack), [`trace()`](https://docs.python.org/3.14/library/inspect.html#inspect.trace), [`getouterframes()`](https://docs.python.org/3.14/library/inspect.html#inspect.getouterframes), and [`getinnerframes()`](https://docs.python.org/3.14/library/inspect.html#inspect.getinnerframes) functions hand back in a list. (Contributed by Daniel Shahaf in [bpo-16808](https://bugs.python.org/issue?@action=redirect&bpo=16808).)

[Subject index](INDEX.md) · [Previous source section](importlib.md) · [Next source section](io.md) · [Release/subject declaration](summary-release-highlights.md)
