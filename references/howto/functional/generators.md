# Generators

### Generators

Generators form a particular category of functions that ease the job of authoring iterators. Whereas ordinary functions compute a value and return it, generators hand back an iterator that produces a stream of values.

You're surely acquainted with how ordinary function calls operate in Python or C. Calling a function gives it a private namespace in which its local variables come into being. Once the function hits a `return` statement, the local variables are discarded and the value goes back to the caller. A subsequent call to that same function brings a new private namespace and a fresh batch of local variables. But what if the local variables weren't discarded upon leaving a function? What if you could afterward pick the function back up where it stopped? That's exactly what generators deliver; you can regard them as resumable functions.

Below is the most basic example of a generator function:

```python
>>> def generate_ints(N):
...    for i in range(N):
...        yield i

```

Any function that contains a [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) keyword is a generator function; Python's [bytecode](https://docs.python.org/3.14/glossary.html#term-bytecode) compiler spots this and compiles the function in a special way because of it.

Calling a generator function doesn't hand back a single value; rather it hands back a generator object supporting the iterator protocol. Upon evaluating the `yield` expression, the generator emits the value of `i`, much like a `return` statement does. The major distinction between `yield` and a `return` statement is that reaching a `yield` suspends the generator's execution state and keeps the local variables intact. When the generator's [`__next__()`](https://docs.python.org/3.14/reference/expressions.html#generator.__next__) method is next called, the function will pick up execution again.

Below is a sample usage of the `generate_ints()` generator:

```python
>>> gen = generate_ints(3)
>>> gen
<generator object generate_ints at ...>
>>> next(gen)
0
>>> next(gen)
1
>>> next(gen)
2
>>> next(gen)
Traceback (most recent call last):
  File "stdin", line 1, in <module>
  File "stdin", line 2, in generate_ints
StopIteration

```

You could just as well write `for i in generate_ints(5)`, or `a, b, c = generate_ints(3)`.

Within a generator function, `return value` triggers `StopIteration(value)` being raised from the [`__next__()`](https://docs.python.org/3.14/reference/expressions.html#generator.__next__) method. After that occurs, or once the end of the function is reached, the flow of values stops and the generator can yield no more values.

You could reproduce the behavior of generators by hand, writing your own class and keeping every one of the generator's local variables as instance variables. For instance, returning a list of integers could be accomplished by setting `self.count` to 0 and having the [`__next__()`](https://docs.python.org/3.14/library/stdtypes.html#iterator.__next__) method bump `self.count` and return it. For a moderately involved generator, though, writing the equivalent class can turn out far messier.

The test suite shipped with Python's library, [Lib/test/test_generators.py](https://github.com/python/cpython/tree/3.14/Lib/test/test_generators.py), holds a number of more interesting examples. Here's one generator that carries out an in-order traversal of a tree by using generators recursively.

```python
# A recursive generator that generates Tree leaves in in-order.
def inorder(t):
    if t:
        for x in inorder(t.left):
            yield x

        yield t.label

        for x in inorder(t.right):
            yield x

```

Two further examples within `test_generators.py` generate solutions for the N-Queens problem (positioning N queens on an NxN chess board such that no queen menaces another) and the Knight's Tour (locating a path that carries a knight across every square of an NxN chessboard without landing on any square more than once).

[Subject index](INDEX.md) · [Previous source context](nested-iteration-products-and-tuple-expression-syntax.md) · [Following source context](passing-values-into-a-generator.md)
