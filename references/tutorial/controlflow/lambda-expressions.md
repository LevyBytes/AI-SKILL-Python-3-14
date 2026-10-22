# 4.9.6. Lambda Expressions

### 4.9.6. Lambda Expressions

The [`lambda`](https://docs.python.org/3.14/reference/expressions.html#lambda) keyword lets you build tiny unnamed functions. The one here gives back the total of its pair of arguments: `lambda a, b: a+b`. You may drop a lambda into any place that expects a function object. Syntax limits each one to a lone expression. In meaning, they amount to nothing more than convenient shorthand for an ordinary function definition. Much like nested definitions, a lambda can pull in variables from the surrounding scope:

```python
>>> def make_incrementor(n):
...     return lambda x: x + n
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43

```

In that sample a lambda expression hands back a function. Another handy application is supplying a compact function as an argument. As an illustration, [`list.sort()`](https://docs.python.org/3.14/library/stdtypes.html#list.sort) accepts a sorting key function *key*, and a lambda can fill that role:

```python
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

```

[Subject index](INDEX.md) · [Previous source section](unpacking-argument-lists.md) · [Following source section](documentation-strings.md)
