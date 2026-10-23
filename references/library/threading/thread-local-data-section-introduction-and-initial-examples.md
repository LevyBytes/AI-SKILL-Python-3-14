# threading - Thread-local data - Section introduction and initial examples

### Thread-local data

Thread-local data holds values that differ from one thread to another. When you want certain data confined to a single thread, build a `local` object and work through its attributes:

```python
>>> mydata = local()
>>> mydata.number = 42
>>> mydata.number
42

```

The `local`-object’s dictionary is also reachable:

```python
>>> mydata.__dict__
{'number': 42}
>>> mydata.__dict__.setdefault('widgets', [])
[]
>>> mydata.widgets
[]

```

When that same data is read from another thread:

```python
>>> log = []
>>> def f():
...     items = sorted(mydata.__dict__.items())
...     log.append(items)
...     mydata.number = 11
...     log.append(mydata.number)

>>> import threading
>>> thread = threading.Thread(target=f)
>>> thread.start()
>>> thread.join()
>>> log
[[], 11]

```

what comes back is different data. On top of that, edits made within the other thread leave the data observed in this thread untouched:

```python
>>> mydata.number
42

```

Naturally, whatever you read off a `local` object — its [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__) attribute included — reflects whichever thread happened to be current when the attribute was fetched. Because of that, it is usually a bad idea to carry such values from one thread to another, since they belong only to the thread that produced them.

Subclassing the `local` class lets you build your own `local` objects:

```python
>>> class MyLocal(local):
...     number = 2
...     def __init__(self, /, **kw):
...         self.__dict__.update(kw)
...     def squared(self):
...         return self.number ** 2

```

That comes in handy for providing default values, methods, and initialization. Keep in mind that when you supply an [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) method, it runs every time the `local` object is touched within a fresh thread. This is what sets up each thread’s dictionary.

Now suppose we build a `local` object:

```python
>>> mydata = MyLocal(color='red')

```

we have a default number:

```python
>>> mydata.number
2

```

an initial color:

[Subject index](INDEX.md) · [Previous](threading-main-thread-to-threading-timeout-max.md) · [Continue](thread-local-data-code-example-mydata-color.md) · [Owning module, declaration or section: threading](threading-thread-based-parallelism.md)
