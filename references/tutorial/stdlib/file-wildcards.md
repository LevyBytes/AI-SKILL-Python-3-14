# 10.2. File wildcards

### 10.2. File wildcards

A function in the [`glob`](https://docs.python.org/3.14/library/glob.html#module-glob) module builds file lists by running wildcard searches over a directory:

```python
>>> import glob
>>> glob.glob('*.py')
['primes.py', 'random.py', 'quote.py']

```

[Subject index](INDEX.md) · [Previous source section](operating-system-interface.md) · [Following source section](command-line-arguments.md)
