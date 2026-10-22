# 4.5. `else` Clauses on Loops

### 4.5. `else` Clauses on Loops

A `for` or `while` loop can attach an `else` clause to its `break` statement. Whenever the loop runs to completion without ever hitting the `break`, that `else` clause runs.

For a [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) loop, the `else` clause runs once the loop has completed its last pass — provided no break happened.

With a [`while`](https://docs.python.org/3.14/reference/compound_stmts.html#while) loop, it runs once the loop’s test turns false.

Whichever loop is involved, a [`break`](https://docs.python.org/3.14/reference/simple_stmts.html#break) that ends the loop means the `else` clause does **not** run. Naturally, any other early exit from the loop — for instance a [`return`](https://docs.python.org/3.14/reference/simple_stmts.html#return) or a thrown exception — will likewise bypass the [`else`](https://docs.python.org/3.14/reference/compound_stmts.html#else) clause.

The `for` loop below, hunting for prime numbers, demonstrates this:

```python
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3

```

(Indeed, the code is right. Look closely: the `else` clause belongs to the `for` loop, **not** the `if` statement.)

A helpful mental model for the else clause is to picture it teamed up with the `if` sitting within the loop. While the loop runs, the order of events resembles if/if/if/else. That `if` lives inside the loop and is reached several times over. Should its test ever come out true, a `break` is triggered. Should the test never come out true, the `else` clause that sits outside the loop runs.

Attached to a loop, the `else` clause resembles the `else` clause of a [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) statement far more than the one belonging to `if` statements: the `else` of a `try` fires when nothing was raised, and a loop’s `else` fires when no `break` happened. To learn more about the `try` statement and exceptions, consult [Handling Exceptions](https://docs.python.org/3.14/tutorial/errors.html#tut-handling).

[Subject index](INDEX.md) · [Previous source section](break-and-continue-statements.md) · [Following source section](pass-statements.md)
