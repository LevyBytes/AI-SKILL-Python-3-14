# What is the difference between arguments and parameters?

### What is the difference between arguments and parameters?

[Parameters](https://docs.python.org/3.14/glossary.html#term-parameter) are specified by the names listed in a function definition, while [arguments](https://docs.python.org/3.14/glossary.html#term-argument) are the values handed to a function at the point you call it. Parameters spell out the sort of arguments a function is able to take. Take, for example, this function definition:

```python
def func(foo, bar=None, **kwargs):
    pass

```

*foo*, *bar* and *kwargs* are parameters of `func`. When you call `func`, however, for instance:

```python
func(42, bar=314, extra=somevar)

```

the values `42`, `314`, and `somevar` are arguments.

[Subject index](INDEX.md)
