# Why am I getting an UnboundLocalError when the variable has a value?

### Core language

### Why am I getting an UnboundLocalError when the variable has a value?

Seeing an [`UnboundLocalError`](https://docs.python.org/3.14/library/exceptions.html#UnboundLocalError) appear in code that used to work can catch you off guard, especially after you've edited it to insert an assignment statement somewhere inside a function's body.

This code:

```python
>>> x = 10
>>> def bar():
...     print(x)
...
>>> bar()
10

```

works, but this code:

```python
>>> x = 10
>>> def foo():
...     print(x)
...     x += 1

```

results in an `UnboundLocalError`:

```python
>>> foo()
Traceback (most recent call last):
  ...
UnboundLocalError: cannot access local variable 'x' where it is not associated with a value

```

The reason is that assigning to a variable within a scope makes that variable local to the scope and hides any like-named variable from an enclosing scope. Because foo's final statement gives `x` a new value, the compiler treats it as a local variable. As a result, the preceding `print(x)` tries to display the local variable before it holds anything, and the error follows.

Within the previous example, declaring the variable global lets you reach the one in the outer scope:

```python
>>> x = 10
>>> def foobar():
...     global x
...     print(x)
...     x += 1
...
>>> foobar()
10

```

Stating this explicitly is needed to remind you that (in contrast to the surface-level similar case of class and instance variables) you are genuinely altering the value of the variable in the outer scope:

```python
>>> print(x)
11

```

The [`nonlocal`](https://docs.python.org/3.14/reference/simple_stmts.html#nonlocal) keyword lets you do an equivalent thing within a nested scope:

```python
>>> def foo():
...    x = 10
...    def bar():
...        nonlocal x
...        print(x)
...        x += 1
...    bar()
...    print(x)
...
>>> foo()
10
11

```

[Subject index](INDEX.md)
