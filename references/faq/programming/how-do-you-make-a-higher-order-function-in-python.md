# How do you make a higher order function in Python?

### How do you make a higher order function in Python?

Two routes are open to you: nested scopes or callable objects. Say, for example, you wanted to define `linear(a,b)` so it returns a function `f(x)` computing the value `a*x+b`. Using nested scopes:

```python
def linear(a, b):
    def result(x):
        return a * x + b
    return result

```

Or using a callable object:

```python
class linear:

    def __init__(self, a, b):
        self.a, self.b = a, b

    def __call__(self, x):
        return self.a * x + self.b

```

In both cases,

```python
taxes = linear(0.3, 2)

```

gives a callable object where `taxes(10e6) == 0.3 * 10e6 + 2`.

The drawback of the callable object route is that it runs a little slower and produces somewhat longer code. Note, though, that a set of callables can share their signature through inheritance:

```python
class exponential(linear):
    # __init__ inherited
    def __call__(self, x):
        return self.a * (x ** self.b)

```

Object can encapsulate state for several methods:

```python
class counter:

    value = 0

    def set(self, x):
        self.value = x

    def up(self):
        self.value = self.value + 1

    def down(self):
        self.value = self.value - 1

count = counter()
inc, dec, reset = count.up, count.down, count.set

```

Here `inc()`, `dec()` and `reset()` act like functions which share the same counting variable.

[Subject index](INDEX.md)
