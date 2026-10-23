# timeit - Basic Examples

### Basic Examples

The example below shows the Command-Line Interface being put to use to weigh three distinct expressions against one another:

```shell
$ python -m timeit "'-'.join(str(n) for n in range(100))"
10000 loops, best of 5: 30.2 usec per loop
$ python -m timeit "'-'.join([str(n) for n in range(100)])"
10000 loops, best of 5: 27.5 usec per loop
$ python -m timeit "'-'.join(map(str, range(100)))"
10000 loops, best of 5: 23.2 usec per loop

```

The same result is reachable from the Python Interface with:

```python
>>> import timeit
>>> timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
0.3018611848820001
>>> timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
0.2727368790656328
>>> timeit.timeit('"-".join(map(str, range(100)))', number=10000)
0.23702679807320237

```

You can equally pass a callable through the Python Interface:

```python
>>> timeit.timeit(lambda: "-".join(map(str, range(100))), number=10000)
0.19665591977536678

```

Bear in mind, though, that `timeit()` works out the number of repetitions on its own only with the command-line interface. The Examples section holds further advanced examples.

[Subject index](INDEX.md) · [Previous](timeit-measure-execution-time-of-small-code-snippets.md) · [Continue](timeit-timeit-to-timeit-default-timer.md) · [Owning module, declaration or section: timeit](timeit-measure-execution-time-of-small-code-snippets.md)
