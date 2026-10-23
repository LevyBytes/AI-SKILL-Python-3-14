# threading - Thread-local data - Code example: >>> mydata.color

```python
>>> mydata.color
'red'
>>> del mydata.color

```

And a method that operates on the data:

```python
>>> mydata.squared()
4

```

Just like earlier, the data is reachable from a separate thread:

```python
>>> log = []
>>> thread = threading.Thread(target=f)
>>> thread.start()
>>> thread.join()
>>> log
[[('color', 'red')], 11]

```

while this thread’s data stays unaffected:

```python
>>> mydata.number
2
>>> mydata.color
Traceback (most recent call last):
...
AttributeError: 'MyLocal' object has no attribute 'color'

```

Bear in mind that subclasses are allowed to declare [__slots__](https://docs.python.org/3.14/glossary.html#term-__slots__), yet those are not thread local. Every thread shares them:

```python
>>> class MyLocal(local):
...     __slots__ = 'number'

>>> mydata = MyLocal()
>>> mydata.number = 42
>>> mydata.color = 'red'

```

So, the separate thread:

```python
>>> thread = threading.Thread(target=f)
>>> thread.start()
>>> thread.join()

```

affects what we see:

```python
>>> mydata.number
11

```

[Subject index](INDEX.md) · [Previous](thread-local-data-section-introduction-and-initial-examples.md) · [Continue](threading-local-class.md) · [Owning module, declaration or section: threading](threading-thread-based-parallelism.md) · [Owning module, declaration or section: Thread-local data](thread-local-data-section-introduction-and-initial-examples.md)
