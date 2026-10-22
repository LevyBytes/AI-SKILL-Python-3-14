# 6. Modules

### 6. Modules

Whenever you leave the Python interpreter and start it back up, whatever definitions you previously made (functions and variables) disappear. So if you plan to write a program of any real length, it pays to compose the interpreter's input in a text editor and feed that file to it instead. The result of doing so is called a *script*. Once your code grows large, you might choose to break it across multiple files, which keeps things easier to maintain. And you might want to reuse a convenient function you wrote across several programs, rather than pasting its definition into every one.

Python provides for exactly this: you can store definitions in a file and then pull them into a script or into an interactive interpreter session. A file like that is termed a *module*; the definitions inside it can be *imported* into other modules or into the *main* module (the set of variables you reach in a top-level script and in calculator mode).

A module is simply a file holding Python definitions and statements. Its file name is the module's name plus the `.py` suffix tacked on. Inside a module, that module's own name (as a string) can be read from the global variable `__name__`. As an example, fire up your preferred text editor and make a file named `fibo.py` in the current directory holding the following:

```python
# Fibonacci numbers module

def fib(n):
    """Write Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    """Return Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

```

Next, launch the Python interpreter and bring in this module via the command below:

```python
>>> import fibo

```

Doing this won't drop the names of the functions declared in `fibo` straight into the current [namespace](https://docs.python.org/3.14/glossary.html#term-namespace) (consult [Python Scopes and Namespaces](https://docs.python.org/3.14/tutorial/classes.html#tut-scopes) for the full story); all it does is place the module name `fibo` there. With that module name in hand you can reach the functions:

```python
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'

```

Should you plan to call a function repeatedly, you can bind it to a local name:

```python
>>> fib = fibo.fib
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

```

[Subject index](INDEX.md) · [Following source section](more-on-modules.md)
