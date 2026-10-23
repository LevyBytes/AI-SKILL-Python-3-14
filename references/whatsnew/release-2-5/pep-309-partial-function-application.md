# What's New in Python 2.5 / PEP 309: Partial Function Application - functools

### PEP 309: Partial Function Application

The aim of the [`functools`](https://docs.python.org/3.14/library/functools.html#module-functools) module is to gather utilities geared toward functional-style programming.

A handy member of this module is the `partial()` function. When you write in a functional style, you'll occasionally need to build variants of functions that already exist but with a few of their parameters pre-supplied. Take a Python function `f(a, b, c)`; from it you might derive a fresh function `g(b, c)` that behaves like `f(1, b, c)`. The term for this is ?partial function application?.

`partial()` accepts the arguments `(function, arg1, arg2, ... kwarg1=value1, kwarg2=value2)`. What you get back is callable, so simply calling it runs *function* together with the pre-supplied arguments.

Here's a small but realistic example:

```python
import functools

def log (message, subsystem):
    "Write the contents of 'message' to the specified subsystem."
    print '%s: %s' % (subsystem, message)
    ...

server_log = functools.partial(log, subsystem='server')
server_log('Unable to open socket')

```

Here's a second example, drawn from a program built on PyGTK. In it a context-sensitive pop-up menu gets assembled on the fly. The callback handed to the menu entry is a partially applied form of the `open_item()` method, with its first argument already supplied.

```python
...
class Application:
    def open_item(self, path):
       ...
    def init (self):
        open_func = functools.partial(self.open_item, item_path)
        popup_menu.append( ("Open", open_func, 1) )

```

The [`functools`](https://docs.python.org/3.14/library/functools.html#module-functools) module carries a further function, `update_wrapper(wrapper, wrapped)`, which assists you in producing well-behaved decorators. `update_wrapper()` carries over the name, module, and docstring attribute onto a wrapper function, making tracebacks that originate inside the wrapped function simpler to follow. For instance, you might write:

```python
def my_decorator(f):
    def wrapper(*args, **kwds):
        print 'Calling decorated function'
        return f(*args, **kwds)
    functools.update_wrapper(wrapper, f)
    return wrapper

```

`wraps()` is a decorator you can apply within decorators of your own to carry across the information from the wrapped function. A different take on the prior example would read:

```python
def my_decorator(f):
    @functools.wraps(f)
    def wrapper(*args, **kwds):
        print 'Calling decorated function'
        return f(*args, **kwds)
    return wrapper

```

See also

[**PEP 309**](https://peps.python.org/pep-0309/) - Partial Function Application

This PEP was proposed and authored by Peter Harris; the implementation came from Hye-Shik Chang and Nick Coghlan, with later adaptations by Raymond Hettinger.

[Subject index](INDEX.md) · [Previous source section](pep-308-conditional-expressions.md) · [Next source section](pep-314-metadata-for-python-software-packages-v1-1.md) · [Release/subject declaration](pep-308-conditional-expressions.md)
