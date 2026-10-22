# Exception arguments, precise handling, reraising and else clauses

An exception that occurs may carry associated values along with it, referred to as the exception's *arguments*. Whether arguments exist and which types they take hinges on the exception type.

A variable can be placed by the *except clause* right after the exception name. That variable gets bound to the exception instance, which usually carries an `args` attribute holding the arguments. As a convenience, builtin exception types supply [`__str__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__str__) so that every argument prints without you having to reach into `.args` directly.

```python
>>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))    # the exception type
...     print(inst.args)     # arguments stored in .args
...     print(inst)          # __str__ allows args to be printed directly,
...                          # but may be overridden in exception subclasses
...     x, y = inst.args     # unpack args
...     print('x =', x)
...     print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs

```

For unhandled exceptions, the exception's [`__str__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__str__) output prints as the closing piece (the 'detail') of the message.

[`BaseException`](https://docs.python.org/3.14/library/exceptions.html#BaseException) serves as the shared base class behind every exception. Among its subclasses is [`Exception`](https://docs.python.org/3.14/library/exceptions.html#Exception), which acts as the base class for all non-fatal exceptions. Exceptions that don't descend from `Exception` usually aren't caught, since their job is to signal that the program ought to stop. Among them are [`SystemExit`](https://docs.python.org/3.14/library/exceptions.html#SystemExit), raised by [`sys.exit()`](https://docs.python.org/3.14/library/sys.html#sys.exit), and [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt), raised when someone wants to break out of the program.

[`Exception`](https://docs.python.org/3.14/library/exceptions.html#Exception) works as a catch-all that grabs nearly everything. That said, being as precise as you can about which exception types you mean to deal with is sound practice, letting any unforeseen exceptions keep propagating.

When dealing with [`Exception`](https://docs.python.org/3.14/library/exceptions.html#Exception), the usual approach is to print or log it and then re-raise it (so a caller can take its own turn handling the exception):

```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise

```

There's an optional *else clause* on the [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) … [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) statement that, whenever it appears, has to come after every *except clause*. It comes in handy for code you want run only if the *try clause* raises nothing. As an example:

```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

```

Relying on the `else` clause beats piling extra code into the [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) clause, since it keeps you from inadvertently trapping an exception that the code shielded by the `try` … `except` statement never raised.

Exception handlers cover more than just the exceptions cropping up directly within the *try clause* — they also cover ones arising in functions invoked (whether directly or not) from inside the *try clause*. For instance:

```python
>>> def this_fails():
...     x = 1/0
...
>>> try:
...     this_fails()
... except ZeroDivisionError as err:
...     print('Handling run-time error:', err)
...
Handling run-time error: division by zero

```

[Subject index](INDEX.md) · [Previous source section](exception-handler-dispatch-and-inheritance.md) · [Following source section](raising-exceptions.md) · [Related tutorial example and explanation](exception-handler-dispatch-and-inheritance.md)
