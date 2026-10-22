# Python 2.5 changes: Generator expression suspension and PEP 342 introduction

### PEP 342: New Generator Features

Python 2.5 introduces an easy mechanism for feeding values *into* a generator. When generators arrived in Python 2.3, they could only emit output; after a generator's code had been invoked to build an iterator, nothing could push fresh information into the function as its execution resumed. At times it would be handy to be able to hand in some information. The hacky workarounds for this included having the generator's code consult a global variable and then mutating that global's value, or passing in a mutable object that callers would later modify.

As a reminder of how basic generators behave, here's a simple example:

```python
def counter (maximum):
    i = 0
    while i < maximum:
        yield i
        i += 1

```

Calling `counter(10)` hands you an iterator that yields the values from 0 through 9. Upon hitting the [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) statement, the iterator hands back the supplied value and pauses the function's execution while keeping the local variables intact. Execution starts again on the next call to the iterator's [`next()`](https://docs.python.org/3.14/library/functions.html#next) method, resuming just past the `yield` statement.

Within Python 2.3, [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) was a statement that returned nothing. As of 2.5, `yield` has become an expression that returns a value you can assign to a variable or otherwise work with:

```python
val = (yield i)

```

My advice is to consistently wrap a [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) expression in parentheses whenever you're doing something with the value it returns, as the example above shows. The parentheses aren't strictly required every time, but it's simpler to always include them rather than trying to recall the cases where they matter.

([**PEP 342**](https://peps.python.org/pep-0342/) spells out the precise rules, namely that a [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield)-expression has to be parenthesized in every case except when it stands as the top-level expression on the right-hand side of an assignment. So you may write `val = yield i` while needing parentheses once there's an operation involved, as in `val = (yield i) + 12`.)

You feed values into a generator by invoking its `send(value)` method. That resumes the generator's code, and the [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) expression hands back the supplied *value*. Should the ordinary [`next()`](https://docs.python.org/3.14/library/functions.html#next) method be called instead, the `yield` hands back [`None`](https://docs.python.org/3.14/library/constants.html#None).

Here's the earlier example, reworked to let the value of the internal counter be changed.

```python
def counter (maximum):
    i = 0
    while i < maximum:
        val = (yield i)
        # If value provided, change counter
        if val is not None:
            i = val
        else:
            i += 1

```

And here's a demonstration of altering the counter:

```python
>>> it = counter(10)
>>> print it.next()
0
>>> print it.next()
1
>>> print it.send(8)
8
>>> print it.next()
9
>>> print it.next()
Traceback (most recent call last):
  File "t.py", line 15, in ?
    print it.next()
StopIteration

```

Since [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) will normally hand back [`None`](https://docs.python.org/3.14/library/constants.html#None), you ought to always test for that case. Avoid relying on its value within expressions unless you're certain that `send()` is going to be the sole method employed to resume your generator function.

Alongside `send()`, generators gain two further new methods:

- `throw(type, value=None, traceback=None)` serves to raise an exception inside the generator; the exception comes up at the [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) expression where the generator's execution sits paused.

- `close()` raises a fresh [`GeneratorExit`](https://docs.python.org/3.14/library/exceptions.html#GeneratorExit) exception inside the generator so as to end the iteration. Once it gets this exception, the generator's code is obliged to raise either `GeneratorExit` or [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration). Trapping the `GeneratorExit` exception and then returning a value is forbidden and will set off a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError); if the function throws some different exception, that exception travels up to the caller. `close()` also gets invoked by Python's garbage collector when the generator gets garbage-collected.

When you have cleanup code that must run as a [`GeneratorExit`](https://docs.python.org/3.14/library/exceptions.html#GeneratorExit) happens, I'd recommend a `try: ... finally:` suite over catching `GeneratorExit`.

Taken together, these changes convert generators from one-directional producers of information into both producers and consumers.

Generators turn into *coroutines* as well, a broader generalization of subroutines. A subroutine is entered at a single point and left at another (the function's top, and a [`return`](https://docs.python.org/3.14/reference/simple_stmts.html#return) statement), whereas coroutines can be entered, left, and resumed at numerous distinct points (the [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) statements). We’ll need to work out effective patterns for putting coroutines to use in Python.

[Subject index](INDEX.md) · [Previous source section](pep-341-unified-try-except-finally.md) · [Next source section](generator-close-and-finalization.md) · [Release/subject declaration](pep-308-conditional-expressions.md)
