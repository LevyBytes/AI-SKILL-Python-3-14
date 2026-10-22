# Small functions and the lambda expression

### Small functions and the lambda expression

As you build functional-style programs, you'll regularly require tiny functions that serve as predicates or that join elements together somehow.

Whenever a fitting Python built-in or module function already exists, there's no need to define a brand-new function:

```python
stripped_lines = [line.strip() for line in lines]
existing_files = filter(os.path.exists, file_list)

```

When the function you require isn't available, you'll have to write it yourself. One approach to crafting small functions relies on the [`lambda`](https://docs.python.org/3.14/reference/expressions.html#lambda) expression. `lambda` accepts some parameters plus an expression that combines them, and builds an anonymous function returning the value of that expression:

```python
adder = lambda x, y: x+y

print_assign = lambda name, value: name + '=' + str(value)

```

The alternative is simply to reach for the `def` statement and declare a function the ordinary way:

```python
def adder(x, y):
    return x + y

def print_assign(name, value):
    return name + '=' + str(value)

```

So which approach wins out? It comes down to style; my own habit is to steer clear of `lambda`.

A factor behind my preference is that `lambda` is rather restricted in what functions it's able to define. Its result must be expressible as one single expression, so you get no multiway `if... elif... else` comparisons and no `try... except` statements. Pack too much into a `lambda` statement and you wind up with an overly tangled expression that's tough to read. Quick now, what does the code below do?

```python
import functools
total = functools.reduce(lambda a, b: (0, a[1] + b[1]), items)[1]

```

It's solvable, but unraveling the expression to see what's happening eats up time. Switching to a brief nested `def` statement improves matters a bit:

[Subject index](INDEX.md) · [Following source continuation](small-functions-and-the-lambda-expression-continuation.md) · [Previous source context](the-operator-module.md)
