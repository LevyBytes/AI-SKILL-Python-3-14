# 4.9.1. Default Argument Values

### 4.9.1. Default Argument Values

The handiest form lets you attach a default value to one argument or more. Such a function may then be invoked with fewer arguments than its definition permits. For instance:

```python
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

```

There are a few ways to invoke this function:

- passing nothing but the required argument: `ask_ok('Do you really want to quit?')`

- passing one of the optional arguments along: `ask_ok('OK to overwrite the file?', 2)`

- or supplying every argument: `ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')`

This example also brings in the [`in`](https://docs.python.org/3.14/reference/expressions.html#in) keyword, which checks whether a sequence holds a given value or not.

Default values get evaluated at the spot where the function is defined, inside the *defining* scope, with the result that

```python
i = 5

def f(arg=i):
    print(arg)

i = 6
f()

```

will print `5`.

**Important warning:** A default value is evaluated a single time only. That matters whenever the default happens to be a mutable object — a list, a dictionary, or an instance of most classes. To illustrate, the function below piles up the arguments handed to it across repeated calls:

```python
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

```

This will print

```python
[1]
[1, 2]
[1, 2, 3]

```

Should you prefer the default not to carry over between later calls, write the function this way instead:

```python
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

```

[Subject index](INDEX.md) · [Previous source section](more-on-defining-functions.md) · [Following source section](keyword-arguments.md)
