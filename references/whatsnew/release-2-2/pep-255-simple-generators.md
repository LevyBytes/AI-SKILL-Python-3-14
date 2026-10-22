# What’s New in Python 2.2 / PEP 255: Simple Generators

### PEP 255: Simple Generators

Another addition in this release is generators, a feature closely tied to the arrival of iterators.

You almost certainly understand the mechanics of calling a function in Python or in C. Invoking a function gives it a private namespace in which its local variables come into being. Once execution hits a [`return`](https://docs.python.org/3.14/reference/simple_stmts.html#return) statement, those local variables vanish and the computed value flows back to the caller. Calling that same function again hands you a brand-new batch of local variables. Now imagine the locals survived past the function's exit. Imagine you could pick the function back up exactly where it had paused. That capability is precisely what generators deliver; picture them as functions you can resume.

Here’s the simplest example of a generator function:

```python
def generate_ints(N):
    for i in range(N):
        yield i

```

Generators brought a fresh keyword, [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield), into the language. Whenever a function holds a `yield` statement it counts as a generator function; the bytecode compiler in Python notices this and compiles that function in a special manner. Since this keyword was new, a module had to turn generators on deliberately by placing a `from __future__ import generators` statement somewhere near the start of its source. By Python 2.3 you will no longer need that line.

Calling a generator function won’t hand back one plain value; what you get instead is a generator object that honours the iterator protocol. Executing the [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) statement makes the generator emit `i`'s value, much as a [`return`](https://docs.python.org/3.14/reference/simple_stmts.html#return) statement would. Where `yield` truly differs from a `return` statement is this: hitting a `yield` pauses the generator's execution state and keeps its local variables intact. When the generator’s `next()` method is invoked again, execution picks back up right after that `yield` statement. (Owing to intricate reasons, you may not place a `yield` statement within the `try` block of a [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try)…[`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) statement; see [**PEP 255**](https://peps.python.org/pep-0255/) for the complete account of how `yield` and exceptions interact.)

Here’s a sample usage of the `generate_ints()` generator:

```python
>>> gen = generate_ints(3)
>>> gen
<generator object at 0x8117f90>
>>> gen.next()
0
>>> gen.next()
1
>>> gen.next()
2
>>> gen.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
  File "<stdin>", line 2, in generate_ints
StopIteration

```

It would work just as well to write `for i in generate_ints(5)`, or `a,b,c = generate_ints(3)`.

Within a generator function, the [`return`](https://docs.python.org/3.14/reference/simple_stmts.html#return) statement may appear only bare, with no value, marking the close of the stream of values; from that point the generator yields nothing more. Writing `return` together with a value, like `return 5`, counts as a syntax error within a generator function. You can also mark the close of a generator’s output by raising [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) yourself, or simply by allowing execution to run off the end of the function.

The same outcome generators provide is reachable by hand: write your own class and keep each of the generator’s local variables as instance variables. As an illustration, you could yield a list of integers by initialising `self.count` to 0 and writing a [`next()`](https://docs.python.org/3.14/library/functions.html#next) method that bumps `self.count` and hands it back. Yet once a generator grows even mildly involved, the matching class turns out far uglier. `Lib/test/test_generators.py` holds several richer examples. Its most basic walks a tree in order, calling generators recursively.

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

A pair of additional examples in `Lib/test/test_generators.py` work out the N-Queens problem (positioning $N$ queens on an $NxN$ chess board such that none of them attacks any other) along with the Knight’s Tour (a path carrying a knight across every square of an $NxN$ chessboard without ever landing on a square more than once).

Generators trace their lineage back to other languages, Icon ([https://www2.cs.arizona.edu/icon/](https://www2.cs.arizona.edu/icon/)) above all, where they sit at the heart of the design. Within Icon, each expression and each function call acts as a generator. A snippet drawn from “An Overview of the Icon Programming Language” at [https://www2.cs.arizona.edu/icon/docs/ipd266.htm](https://www2.cs.arizona.edu/icon/docs/ipd266.htm) conveys the flavour:

```python
sentence := "Store it in the neighboring harbor"
if (i := find("or", sentence)) > 5 then write(i)

```

Within Icon the `find()` function hands back the positions where the substring “or” turns up: 3, 23, 33. Inside the [`if`](https://docs.python.org/3.14/reference/compound_stmts.html#if) statement, `i` initially takes the value 3, yet 3 falls below 5, so the test fails and Icon tries again with the next value, 23. Because 23 exceeds 5, the test passes this time, and the code writes the value 23 out to the screen.

Python stops well short of Icon's wholesale embrace of generators as a foundational idea. They form a fresh piece of the core Python language, though picking them up or putting them to work is entirely optional; should they not address any problem you face, you're welcome to skip them. A point where Python’s design departs from Icon’s is that a generator’s state shows up as a tangible object (the iterator), one you can hand off to other functions or tuck into a data structure.

See also

[**PEP 255**](https://peps.python.org/pep-0255/) - Simple Generators

Authored by Neil Schemenauer, Tim Peters, Magnus Lie Hetland. The bulk of the implementation came from Neil Schemenauer and Tim Peters, plus assorted fixes contributed by the Python Labs crew.

[Subject index](INDEX.md) · [Previous source section](iterator-direction-and-container-implementations.md) · [Next source section](pep-237-unifying-long-integers-and-integers.md) · [Release/subject declaration](introduction.md)
