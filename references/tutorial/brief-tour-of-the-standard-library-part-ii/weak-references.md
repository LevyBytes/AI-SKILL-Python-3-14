# 11.6. Weak references

### 11.6. Weak references

Memory is managed for you in Python — reference counting handles most objects, with [garbage collection](https://docs.python.org/3.14/glossary.html#term-garbage-collection) sweeping up cycles. Memory comes back not long after the final reference to an object disappears.

That model serves the bulk of programs well, though now and then you want to keep tabs on objects only while some other code is using them. The catch: merely tracking them establishes a reference that pins them in place permanently. Tools for observing objects without setting up such a reference live in the [`weakref`](https://docs.python.org/3.14/library/weakref.html#module-weakref) module. As soon as an object is no longer wanted, it drops out of a weakref table automatically and a callback fires for the weakref objects. A common use is caching objects whose creation is costly:

```python
>>> import weakref, gc
>>> class A:
...     def __init__(self, value):
...         self.value = value
...     def __repr__(self):
...         return str(self.value)
...
>>> a = A(10)                   # create a reference
>>> d = weakref.WeakValueDictionary()
>>> d['primary'] = a            # does not create a reference
>>> d['primary']                # fetch the object if it is still alive
10
>>> del a                       # remove the one reference
>>> gc.collect()                # run garbage collection right away
0
>>> d['primary']                # entry was automatically removed
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    d['primary']                # entry was automatically removed
  File "C:/python314/lib/weakref.py", line 46, in __getitem__
    o = self.data[key]()
KeyError: 'primary'

```

[Subject index](INDEX.md) · [Previous source section](logging.md) · [Following source section](tools-for-working-with-lists.md)
