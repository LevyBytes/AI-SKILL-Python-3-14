# What’s New in Python 2.4 / PEP 322: Reverse Iteration

### PEP 322: Reverse Iteration

There’s a fresh built-in function, `reversed(seq)`, which accepts a sequence and gives back an iterator that walks the sequence’s elements in the opposite order.

```python
>>> for i in reversed(xrange(1,4)):
...    print i
...
3
2
1

```

Set against extended slicing such as `range(1,4)[::-1]`, [`reversed()`](https://docs.python.org/3.14/library/functions.html#reversed) reads more easily, executes faster, and consumes far less memory.

Keep in mind that [`reversed()`](https://docs.python.org/3.14/library/functions.html#reversed) takes sequences only, not iterators of any kind. To reverse an iterator, first turn it into a list via [`list()`](https://docs.python.org/3.14/library/stdtypes.html#list).

```python
>>> input = open('/etc/passwd', 'r')
>>> for line in reversed(list(input)):
...   print line
...
root:*:0:0:System Administrator:/var/root:/bin/tcsh
  ...

```

See also

[**PEP 322**](https://peps.python.org/pep-0322/) - Reverse Iteration

Authored and built by Raymond Hettinger.

[Subject index](INDEX.md) · [Previous source section](pep318-function-and-method-decorators.md) · [Next source section](pep-324-new-subprocess-module.md) · [Release/subject declaration](pep-218-built-in-set-objects.md)
