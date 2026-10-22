# Calling functions on elements

### Calling functions on elements

The [`operator`](https://docs.python.org/3.14/library/operator.html#module-operator) module holds a collection of functions that mirror Python's operators. A few examples are [`operator.add(a, b)`](https://docs.python.org/3.14/library/operator.html#operator.add) (sums two values), [`operator.ne(a, b)`](https://docs.python.org/3.14/library/operator.html#operator.ne) (equivalent to `a != b`), and [`operator.attrgetter('id')`](https://docs.python.org/3.14/library/operator.html#operator.attrgetter) (hands back a callable that grabs the `.id` attribute).

[`itertools.starmap(func, iter)`](https://docs.python.org/3.14/library/itertools.html#itertools.starmap) presumes the iterable will produce a stream of tuples, then invokes *func* with each such tuple supplying the arguments:

```python
itertools.starmap(os.path.join,
                  [('/bin', 'python'), ('/usr', 'bin', 'java'),
                   ('/usr', 'bin', 'perl'), ('/usr', 'bin', 'ruby')])
=>
  /bin/python, /usr/bin/java, /usr/bin/perl, /usr/bin/ruby

```

[Subject index](INDEX.md) · [Previous source context](creating-new-iterators.md) · [Following source context](selecting-elements.md)
