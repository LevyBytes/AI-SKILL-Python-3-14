# 6.1.1. Executing modules as scripts

### 6.1.1. Executing modules as scripts

When you launch a Python module like this

```python
python fibo.py <arguments>

```

the module's code gets executed exactly as though you had imported it, except `__name__` is set to `"__main__"`. So by appending this code at the bottom of your module:

```python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

```

you can make the file serve both as a script and as an importable module, since the command-line parsing code only fires when the module runs as the "main" file:

```shell
$ python fibo.py 50
0 1 1 2 3 5 8 13 21 34

```

When the module is imported instead, that code stays dormant:

```python
>>> import fibo
>>>

```

This pattern commonly serves to give a module a handy user interface, or to support testing (running the module as a script kicks off a test suite).

[Subject index](INDEX.md) · [Previous source section](more-on-modules.md) · [Following source section](the-module-search-path.md)
