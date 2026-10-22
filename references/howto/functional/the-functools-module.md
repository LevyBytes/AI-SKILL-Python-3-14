# The functools module

### The functools module

The [`functools`](https://docs.python.org/3.14/library/functools.html#module-functools) module offers a few higher-order functions. A **higher-order function** accepts one or more functions as its input and produces a new function in return. This module's handiest tool is the [`functools.partial()`](https://docs.python.org/3.14/library/functools.html#functools.partial) function.

When you write in a functional style, there are times you'll want to build variations of existing functions with some parameters already supplied. Take a Python function `f(a, b, c)`; perhaps you'd like a new function `g(b, c)` that behaves like `f(1, b, c)`; you are supplying a value for one of `f()`'s parameters. The name for this is "partial function application".

The [`partial()`](https://docs.python.org/3.14/library/functools.html#functools.partial) constructor accepts the arguments `(function, arg1, arg2, ..., kwarg1=value1, kwarg2=value2)`. The object it returns is callable, so you simply call it to run `function` with those pre-supplied arguments.

What follows is a compact yet realistic illustration:

```python
import functools

def log(message, subsystem):
    """Write the contents of 'message' to the specified subsystem."""
    print('%s: %s' % (subsystem, message))
    ...

server_log = functools.partial(log, subsystem='server')
server_log('Unable to open socket')

```

[`functools.reduce(func, iter, [initial_value])`](https://docs.python.org/3.14/library/functools.html#functools.reduce) applies an operation cumulatively across all of the iterable's elements and therefore cannot work on infinite iterables. *func* has to be a function accepting two elements and returning one value. `functools.reduce()` grabs the first two elements A and B that the iterator yields and works out `func(A, B)`. Next it asks for the third element, C, computes `func(func(A, B), C)`, folds that result together with the fourth element returned, and keeps going until the iterable is spent. Should the iterable yield no values whatsoever, a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception gets raised. When an initial value is provided, it serves as the starting point and `func(initial_value, A)` becomes the first computation.

```python
>>> import operator, functools
>>> functools.reduce(operator.concat, ['A', 'BB', 'C'])
'ABBC'
>>> functools.reduce(operator.concat, [])
Traceback (most recent call last):
  ...
TypeError: reduce() of empty iterable with no initial value
>>> functools.reduce(operator.mul, [1, 2, 3], 1)
6
>>> functools.reduce(operator.mul, [], 1)
1

```

Pairing [`operator.add()`](https://docs.python.org/3.14/library/operator.html#operator.add) with [`functools.reduce()`](https://docs.python.org/3.14/library/functools.html#functools.reduce) sums together every element of the iterable. That scenario comes up so frequently that a dedicated built-in named [`sum()`](https://docs.python.org/3.14/library/functions.html#sum) exists for the job:

```python
>>> import functools, operator
>>> functools.reduce(operator.add, [1, 2, 3, 4], 0)
10
>>> sum([1, 2, 3, 4])
10
>>> sum([])
0

```

For plenty of [`functools.reduce()`](https://docs.python.org/3.14/library/functools.html#functools.reduce) scenarios, though, spelling out the plain [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) loop can read more clearly:

```python
import functools
# Instead of:
product = functools.reduce(operator.mul, [1, 2, 3], 1)

# You can write:
product = 1
for i in [1, 2, 3]:
    product *= i

```

A kindred function is [`itertools.accumulate(iterable, func=operator.add)`](https://docs.python.org/3.14/library/itertools.html#itertools.accumulate). It runs the identical computation, but rather than handing back just the final value, `accumulate()` produces an iterator that also emits each intermediate result:

```python
itertools.accumulate([1, 2, 3, 4, 5]) =>
  1, 3, 6, 10, 15

itertools.accumulate([1, 2, 3, 4, 5], operator.mul) =>
  1, 2, 6, 24, 120

```

[Subject index](INDEX.md) · [Previous source context](grouping-elements.md) · [Following source context](the-operator-module.md)
