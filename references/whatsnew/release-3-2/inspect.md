# What's New In Python 3.2 / inspect — inspect

### inspect

- A new [`getgeneratorstate()`](https://docs.python.org/3.14/library/inspect.html#inspect.getgeneratorstate) function joins the [`inspect`](https://docs.python.org/3.14/library/inspect.html#module-inspect) module, making it simple to read off a generator-iterator’s current state:

```python
>>> from inspect import getgeneratorstate
>>> def gen():
...     yield 'demo'
...
>>> g = gen()
>>> getgeneratorstate(g)
'GEN_CREATED'
>>> next(g)
'demo'
>>> getgeneratorstate(g)
'GEN_SUSPENDED'
>>> next(g, None)
>>> getgeneratorstate(g)
'GEN_CLOSED'

```

(Contributed by Rodolpho Eckhardt and Nick Coghlan, [bpo-10220](https://bugs.python.org/issue?@action=redirect&bpo=10220).)

- So that lookups can happen without tripping a dynamic attribute, the [`inspect`](https://docs.python.org/3.14/library/inspect.html#module-inspect) module adds [`getattr_static()`](https://docs.python.org/3.14/library/inspect.html#inspect.getattr_static). In contrast to [`hasattr()`](https://docs.python.org/3.14/library/functions.html#hasattr), it performs a genuinely read-only lookup that is guaranteed never to mutate state mid-search:

```python
>>> class A:
...     @property
...     def f(self):
...         print('Running')
...         return 10
...
>>> a = A()
>>> getattr(a, 'f')
Running
10
>>> inspect.getattr_static(a, 'f')
<property object at 0x1022bd788>

```

>

(Contributed by Michael Foord.)

[Subject index](INDEX.md) · [Previous source section](tempfile.md) · [Next source section](pydoc.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
