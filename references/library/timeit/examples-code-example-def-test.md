# timeit — Examples — Code example: def test():

```python
def test():
    """Stupid test function"""
    L = [i for i in range(100)]

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test"))

```

A further option is to hand [`globals()`](https://docs.python.org/3.14/library/functions.html#globals) to the *globals* parameter, which makes the code run inside your current global namespace. That can prove handier than naming imports one by one:

```python
def f(x):
    return x**2
def g(x):
    return x**4
def h(x):
    return x**8

import timeit
print(timeit.timeit('[func(42) for func in (f,g,h)]', globals=globals()))

```

[Subject index](INDEX.md) · [Previous](examples-section-introduction-and-initial-examples.md) · [Owning module, declaration or section: timeit](timeit-measure-execution-time-of-small-code-snippets.md) · [Owning module, declaration or section: Examples](examples-section-introduction-and-initial-examples.md)
