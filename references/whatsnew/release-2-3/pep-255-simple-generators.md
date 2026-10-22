# What’s New in Python 2.3 / PEP 255: Simple Generators

### PEP 255: Simple Generators

Back in Python 2.2, generators showed up as an opt-in feature switched on through a `from __future__ import generators` directive. With 2.3 that special enabling is gone — generators are now always available, which makes [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) a keyword at all times. What remains of this section reproduces the generator write-up taken from the “What’s New in Python 2.2” document; should you already have read it when Python 2.2 first appeared, you may move past the rest of this section.

How calls to functions operate in Python or in C is surely no mystery to you. Calling a function hands it a private namespace, and that is where its local variables come into being. Once the function hits a [`return`](https://docs.python.org/3.14/reference/simple_stmts.html#return) statement, those local variables vanish and the computed value goes back to the caller. Calling that same function again produces a brand-new batch of local variables. Yet suppose the local variables survived past the point where you left the function? Suppose you were able to pick the function back up afterward right where it stopped? That is exactly the capability generators deliver; picture them as functions that can be resumed.

Below is the most basic generator function you could write:

```python
def generate_ints(N):
    for i in range(N):
        yield i

```

For the sake of generators a fresh keyword, [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield), was added. A function is a generator function whenever it holds a `yield` statement; Python’s bytecode compiler spots this and, as a consequence, compiles such a function in a special way.

Calling a generator function gives back not one lone value but rather a generator object honoring the iterator protocol. When the [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) statement runs, the generator emits the value held by `i`, much as a [`return`](https://docs.python.org/3.14/reference/simple_stmts.html#return) statement would. Where `yield` parts ways with a `return` statement is that, upon hitting a `yield`, the generator’s execution state is paused and its local variables are kept intact. When the generator’s `.next()` method is invoked again, execution picks back up right after the `yield` statement. (Owing to complicated reasons, a `yield` statement may not appear within the [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) block of a `try`…`finally` statement; for a complete account of how `yield` and exceptions interact, read [**PEP 255**](https://peps.python.org/pep-0255/).)

What follows shows the `generate_ints()` generator in use:

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
  File "stdin", line 1, in ?
  File "stdin", line 2, in generate_ints
StopIteration

```

Equally well you might write `for i in generate_ints(5)`, or `a,b,c = generate_ints(3)`.

Within a generator function, you may only use the [`return`](https://docs.python.org/3.14/reference/simple_stmts.html#return) statement with no value; it marks the close of the stream of values, after which the generator yields nothing more. Using `return` together with a value — say `return 5` — is a syntax error inside a generator function. There are other ways to flag the end of a generator’s output: raise [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) yourself, or simply allow control to run off the end of the function.

The same result generators give you could be reproduced by hand if you wrote a class of your own and held every one of the generator’s local variables as instance variables. To return a list of integers, for example, you might initialize `self.count` to 0 and arrange for the [`next()`](https://docs.python.org/3.14/library/functions.html#next) method to bump `self.count` up and hand it back. That said, with a generator of even middling complexity the matching class would turn out far more tangled. `Lib/test/test_generators.py` holds several more engaging examples. The plainest of them walks a tree in in-order fashion, applying generators recursively.

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

A further pair of examples sitting in `Lib/test/test_generators.py` work out answers to the N-Queens problem (positioning $N$ queens on an $NxN$ chess board such that none attacks any other) and to the Knight’s Tour (a path that carries a knight across every square of an $NxN$ chessboard while never landing on the same square twice).

Generators trace their roots to other programming languages, Icon ([https://www2.cs.arizona.edu/icon/](https://www2.cs.arizona.edu/icon/)) above all, a language where the generator concept is fundamental. Within Icon, generator behavior is exhibited by every expression and every function call alike. A single example drawn from “An Overview of the Icon Programming Language” at [https://www2.cs.arizona.edu/icon/docs/ipd266.htm](https://www2.cs.arizona.edu/icon/docs/ipd266.htm) conveys the flavor of it:

```python
sentence := "Store it in the neighboring harbor"
if (i := find("or", sentence)) > 5 then write(i)

```

Within Icon, the `find()` function hands back the positions where the substring “or” turns up: 3, 23, 33. Inside the [`if`](https://docs.python.org/3.14/reference/compound_stmts.html#if) statement, `i` initially receives the value 3, but since 3 falls below 5 the test does not hold, so Icon attempts it once more with the next value, 23. Because 23 exceeds 5 the test passes this time, and the code writes 23 out to the screen.

Icon takes generators much further as a foundational notion than Python does. While generators count as part of the core Python language, picking them up or putting them to work is by no means required; if they address none of your problems, you are welcome to leave them alone. A distinctive trait of Python’s approach versus Icon’s is that a generator’s state shows up as a tangible object — the iterator — which you may hand off to other functions or keep inside a data structure.

See also

[**PEP 255**](https://peps.python.org/pep-0255/) - Simple Generators

Authored by Neil Schemenauer, Tim Peters, Magnus Lie Hetland. The bulk of the implementation fell to Neil Schemenauer and Tim Peters, while additional fixes arrived from the Python Labs crew.

[Subject index](INDEX.md) · [Previous source section](pep-218-a-standard-set-datatype-see-also.md) · [Next source section](pep-263-source-code-encodings.md) · [Release/subject declaration](standard-set-type.md)
