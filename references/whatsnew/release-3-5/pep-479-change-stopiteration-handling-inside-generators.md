# What’s New In Python 3.5 / PEP 479: Change StopIteration handling inside generators

### PEP 479: Change StopIteration handling inside generators

In Python 3.4 and prior, how generators and [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) interacted could catch you off guard and might mask hard-to-find bugs. Up to then, a `StopIteration` raised by accident within a generator function was taken as the end of the iteration by whatever loop construct was driving the generator.

[**PEP 479**](https://peps.python.org/pep-0479/) reworks how generators act: once a `StopIteration` exception arises within a generator, it gets swapped for a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) prior to leaving the generator frame. The primary aim behind this revision is to make debugging easier in the case where an unguarded [`next()`](https://docs.python.org/3.14/library/functions.html#next) call raises `StopIteration` and quietly ends the iteration that the generator drives. That trap grows particularly nasty when paired with the `yield from` construct.

Because this is a backwards incompatible change, switching on the new behavior calls for a [__future__](https://docs.python.org/3.14/glossary.html#term-__future__) import:

```python
>>> from __future__ import generator_stop

>>> def gen():
...     next(iter([]))
...     yield
...
>>> next(gen())
Traceback (most recent call last):
  File "<stdin>", line 2, in gen
StopIteration

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: generator raised StopIteration

```

When the `__future__` import is absent, a [`PendingDeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#PendingDeprecationWarning) gets raised any time a [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) exception arises within a generator.

See also

[**PEP 479**](https://peps.python.org/pep-0479/) – Change StopIteration handling inside generators

PEP authored by Chris Angelico and Guido van Rossum. The implementation was carried out by Chris Angelico, Yury Selivanov and Nick Coghlan.

[Subject index](INDEX.md) · [Previous source section](pep-475-retry-system-calls-failing-with-eintr.md) · [Release/subject declaration](summary-release-highlights.md)
