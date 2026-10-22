# Try-except dispatch, multiple handlers and exception inheritance

### 8.3. Handling Exceptions

You can author programs that cope with particular exceptions you choose. Consider the example below: it keeps prompting the user for input until a valid integer arrives, while still letting the user break out of the program (via Control-C, or whatever your operating system provides); be aware that such a user-triggered break is announced by raising the [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt) exception.

```python
>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
...

```

Here is how the [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) statement operates.

- To begin, the *try clause* (the statement(s) sitting between the [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) and [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) keywords) runs.

- Should no exception arise, the *except clause* gets bypassed and the [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) statement's run wraps up.

- Should an exception arise while the [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) clause runs, whatever remains of that clause is bypassed. After that, provided its type lines up with the exception named following the [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) keyword, the *except clause* runs, and execution then resumes past the try/except block.

- Should an exception arise that fails to match the one named in the *except clause*, it gets handed up to enclosing [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) statements; when no handler turns up, it counts as an *unhandled exception* and execution halts with an error message.

A single [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) statement can carry several *except clauses*, providing handlers for distinct exceptions. No more than one handler runs. A handler only deals with exceptions arising in the matching *try clause*, never those in fellow handlers belonging to the same `try` statement. One *except clause* is allowed to list several exceptions, like so:

```python
... except RuntimeError, TypeError, NameError:
...     pass

```

A class placed in an [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) clause matches exceptions that are instances either of that class itself or of any class derived from it (though not in reverse — an *except clause* naming a derived class won't match instances of the classes it descends from). As an illustration, the code below prints B, C, D in that sequence:

```python
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

```

Observe that had the *except clauses* been flipped (placing `except B` at the top), the output would have been B, B, B — whichever *except clause* matches first is the one that fires.

[Subject index](INDEX.md) · [Previous source section](exceptions.md) · [Following source section](exception-arguments-reraising-and-else.md) · [Related tutorial example and explanation](exception-arguments-reraising-and-else.md)
