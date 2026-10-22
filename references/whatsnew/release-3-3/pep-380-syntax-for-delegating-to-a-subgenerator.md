# What's New In Python 3.3 / PEP 380: Syntax for Delegating to a Subgenerator

### PEP 380: Syntax for Delegating to a Subgenerator

PEP 380 introduces the `yield from` expression, which lets a [generator](https://docs.python.org/3.14/glossary.html#term-generator) hand off a portion of its work to a second generator. Thanks to this, a stretch of code holding [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) can be lifted out and relocated into a separate generator. The subgenerator may furthermore return carrying a value, and that value reaches the delegating generator.

Even though its main purpose is delegating to a subgenerator, the `yield from` expression in fact permits delegation to any arbitrary subiterators.

When the iterators are simple, `yield from iterable` amounts to little more than a condensed spelling of `for item in iterable: yield item`:

```python
>>> def g(x):
...     yield from range(x, 0, -1)
...     yield from range(x)
...
>>> list(g(5))
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]

```

Unlike a plain loop, though, `yield from` lets subgenerators take in sent and thrown values straight from the calling scope, and pass a final value back up to the outer generator:

```python
>>> def accumulate():
...     tally = 0
...     while 1:
...         next = yield
...         if next is None:
...             return tally
...         tally += next
...
>>> def gather_tallies(tallies):
...     while 1:
...         tally = yield from accumulate()
...         tallies.append(tally)
...
>>> tallies = []
>>> acc = gather_tallies(tallies)
>>> next(acc)  # Ensure the accumulator is ready to accept values
>>> for i in range(4):
...     acc.send(i)
...
>>> acc.send(None)  # Finish the first tally
>>> for i in range(5):
...     acc.send(i)
...
>>> acc.send(None)  # Finish the second tally
>>> tallies
[6, 10]

```

What chiefly motivates this change is to make it possible for even generators built to work with the `send` and `throw` methods to be carved into several subgenerators just as readily as one big function can be carved into several subfunctions.

See also

[**PEP 380**](https://peps.python.org/pep-0380/) - Syntax for Delegating to a Subgenerator

Authored as a PEP by Greg Ewing; built by Greg Ewing, folded into 3.3 by Renaud Blanch, Ryan Kelly and Nick Coghlan; docs from Zbigniew Jędrzejewski-Szmek and Nick Coghlan

[Subject index](INDEX.md) · [Previous source section](pep-3151-reworking-the-os-and-io-exception-hierarchy.md) · [Next source section](pep-409-suppressing-exception-context.md) · [Release/subject declaration](summary-release-highlights.md)
