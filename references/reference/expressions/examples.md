# 6.2.10.2. Examples

#### 6.2.10.2. Examples

What follows is a short example that illustrates how generators and generator functions behave:

```python
>>> def echo(value=None):
...     print("Execution starts when 'next()' is called for the first time.")
...     try:
...         while True:
...             try:
...                 value = (yield value)
...             except Exception as e:
...                 value = e
...     finally:
...         print("Don't forget to clean up when 'close()' is called.")
...
>>> generator = echo(1)
>>> print(next(generator))
Execution starts when 'next()' is called for the first time.
1
>>> print(next(generator))
None
>>> print(generator.send(2))
2
>>> generator.throw(TypeError, "spam")
TypeError('spam',)
>>> generator.close()
Don't forget to clean up when 'close()' is called.

```

For examples using `yield from`, see [PEP 380: Syntax for Delegating to a Subgenerator](https://docs.python.org/3.14/whatsnew/3.3.html#pep-380) in ?What's New in Python.?

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Owning language section](atoms.md) · [Owning language section](yield-expressions.md) · [Previous source section](generator-close.md) · [Following source section](asynchronous-generator-functions.md)
