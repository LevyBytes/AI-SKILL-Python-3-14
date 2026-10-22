# 7.1.2. The String format() Method

### 7.1.2. The String format() Method

Here is how rudimentary use of the [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format) method appears:

```python
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"

```

Those brackets, along with whatever sits inside them (termed format fields), get swapped out for the objects fed to the [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format) method. Putting a number inside the brackets lets you point at the position of an object handed to the `str.format()` method.

```python
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam

```

Should you supply keyword arguments to the [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format) method, you reach their values by naming the argument.

```python
>>> print('This {food} is {adjective}.'.format(
...       food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.

```

You may freely mix positional arguments together with keyword ones:

```python
>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
...                                                    other='Georg'))
The story of Bill, Manfred, and Georg.

```

When you've got a genuinely long format string you'd rather not break apart, being able to call out the variables to format by name rather than by position is welcome. You manage that by just handing in the dict and reaching its keys with square brackets `'[]'`.

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
...       'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678

```

An alternative is to feed the `table` dictionary in as keyword arguments by way of the `**` notation.

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678

```

It proves especially handy when paired with the built-in function [`vars()`](https://docs.python.org/3.14/library/functions.html#vars), whose return value is a dictionary holding every local variable:

```python
>>> table = {k: str(v) for k, v in vars().items()}
>>> message = " ".join([f'{k}: ' + '{' + k +'};' for k in table.keys()])
>>> print(message.format(**table))
__name__: __main__; __doc__: None; __package__: None; __loader__: ...

```

By way of illustration, the lines below turn out a neatly aligned block of columns listing integers alongside their squares and cubes:

```python
>>> for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000

```

To get the full picture of string formatting via [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format), have a look at [Format string syntax](https://docs.python.org/3.14/library/string.html#formatstrings).

[Subject index](INDEX.md) · [Previous source section](formatted-string-literals.md) · [Following source section](manual-string-formatting.md)
