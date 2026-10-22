# Why do lambdas defined in a loop with different values all return the same result?

### Why do lambdas defined in a loop with different values all return the same result?

Suppose you employ a for loop to create several distinct lambdas (or even ordinary functions), like so:

```python
>>> squares = []
>>> for x in range(5):
...     squares.append(lambda: x**2)

```

The result is a list holding 5 lambdas that compute `x**2`. You might assume that calling them would yield, in turn, `0`, `1`, `4`, `9`, and `16`. But when you actually test it, you'll find every one of them returns `16`:

```python
>>> squares[2]()
16
>>> squares[4]()
16

```

The cause is that `x` isn't local to the lambdas; it lives in the outer scope and gets read at the moment the lambda runs — not at the moment it was defined. Once the loop finishes, `x` holds `4`, so each of the functions now yields `4**2`, namely `16`. You can confirm this too by altering the value of `x` and watching how the lambda results shift:

```python
>>> x = 8
>>> squares[2]()
64

```

To prevent this, you have to capture the values in variables local to the lambdas, so they no longer depend on the global `x`:

```python
>>> squares = []
>>> for x in range(5):
...     squares.append(lambda n=x: n**2)

```

In this case, `n=x` makes a fresh variable `n` local to the lambda, evaluated when the lambda is defined so that it carries whatever value `x` held at that spot in the loop. That means `n` will be `0` for the first lambda, `1` for the second, `2` for the third, and onward. As a result each lambda now produces the right answer:

```python
>>> squares[2]()
4
>>> squares[4]()
16

```

Keep in mind this behaviour isn't unique to lambdas; it holds for regular functions as well.

[Subject index](INDEX.md)
