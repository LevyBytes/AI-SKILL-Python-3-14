# What’s New in Python 2.6 / PEP 3129: Class Decorators

### PEP 3129: Class Decorators

The reach of decorators now stretches past functions to cover classes as well. The following is now valid:

```python
@foo
@bar
class A:
  pass

```

Which amounts to the same thing as:

```python
class A:
  pass

A = foo(bar(A))

```

See also

[**PEP 3129**](https://peps.python.org/pep-3129/) - Class Decorators

PEP written by Collin Winter.

[Subject index](INDEX.md) · [Previous source section](pep-3127-integer-literal-support-and-syntax.md) · [Next source section](pep-3141-a-type-hierarchy-for-numbers.md) · [Release/subject declaration](python-3-0.md)
