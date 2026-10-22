# Passing values into a generator continuation

To feed a value into a generator, invoke its [`send(value)`](https://docs.python.org/3.14/reference/expressions.html#generator.send) method. Doing so wakes the generator back up and makes the `yield` expression evaluate to the value you passed. When the ordinary [`__next__()`](https://docs.python.org/3.14/reference/expressions.html#generator.__next__) method runs instead, `yield` evaluates to `None`.

The following is a basic counter that steps upward by 1 while letting you reset its internal count.

```python
def counter(maximum):
    i = 0
    while i < maximum:
        val = (yield i)
        # If value provided, change counter
        if val is not None:
            i = val
        else:
            i += 1

```

And below is a demonstration that resets the counter:

```python
>>> it = counter(10)
>>> next(it)
0
>>> next(it)
1
>>> it.send(8)
8
>>> next(it)
9
>>> next(it)
Traceback (most recent call last):
  File "t.py", line 15, in <module>
    it.next()
StopIteration

```

Since `yield` frequently hands back `None`, it's wise to always handle that situation. Avoid feeding its result straight into expressions unless you can guarantee that [`send()`](https://docs.python.org/3.14/reference/expressions.html#generator.send) is the sole means by which your generator function gets resumed.

Beyond [`send()`](https://docs.python.org/3.14/reference/expressions.html#generator.send), generators expose two further methods:

- [`throw(value)`](https://docs.python.org/3.14/reference/expressions.html#generator.throw) raises an exception within the generator; that exception surfaces from the `yield` expression at the point where execution had been suspended.

- [`close()`](https://docs.python.org/3.14/reference/expressions.html#generator.close) delivers a [`GeneratorExit`](https://docs.python.org/3.14/library/exceptions.html#GeneratorExit) exception into the generator so that iteration stops. When it gets this exception, the generator's body has to either re-raise `GeneratorExit` or [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration); swallowing the exception and proceeding with anything else is forbidden and will produce a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError). Python's garbage collector invokes `close()` as well whenever the generator gets garbage-collected.

When you have teardown code that should run on a [`GeneratorExit`](https://docs.python.org/3.14/library/exceptions.html#GeneratorExit), my recommendation is to wrap it in a `try: ... finally:` suite rather than trapping `GeneratorExit` directly.

Taken together, these features transform generators from purely one-directional emitters of data into things that both emit and absorb data.

That also makes generators **coroutines**, a broader kind of subroutine. A subroutine has a single entry and a single exit (its first line, and a `return` statement), whereas a coroutine may be entered, left, and picked back up at numerous distinct spots (its `yield` statements).

[Subject index](INDEX.md) · [Previous source owning section](passing-values-into-a-generator.md) · [Following source context](map-and-filter-transformations.md)
