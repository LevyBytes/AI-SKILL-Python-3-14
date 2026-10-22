# What’s New In Python 3.5 / heapq — heapq

### heapq

You can now tailor how elements are compared inside [`merge()`](https://docs.python.org/3.14/library/heapq.html#heapq.merge) by handing a [key function](https://docs.python.org/3.14/glossary.html#term-key-function) to the new optional *key* keyword argument; a fresh optional *reverse* keyword argument flips the comparison:

```python
>>> import heapq
>>> a = ['9', '777', '55555']
>>> b = ['88', '6666']
>>> list(heapq.merge(a, b, key=len))
['9', '88', '777', '6666', '55555']
>>> list(heapq.merge(reversed(a), reversed(b), key=len, reverse=True))
['55555', '6666', '777', '88', '9']

```

(Contributed by Raymond Hettinger in [bpo-13742](https://bugs.python.org/issue?@action=redirect&bpo=13742).)

[Subject index](INDEX.md) · [Previous source section](gzip.md) · [Next source section](http.md) · [Release/subject declaration](summary-release-highlights.md)
