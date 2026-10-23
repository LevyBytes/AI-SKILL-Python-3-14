# What’s New in Python 2.6 / PEP 343: The ‘with’ statement - decimal, threading

### PEP 343: The ‘with’ statement

In its prior release, Python 2.5, the ‘[`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with)’ statement showed up as an opt-in feature that you switched on with a `from __future__ import with_statement` directive. By 2.6 you no longer have to enable the statement specially; from this point on `with` is a keyword at all times. What follows in this section is taken straight from the matching part of the “What’s New in Python 2.5” document; if the ‘`with`’ statement is already familiar to you from Python 2.5, feel free to jump past this section.

The ‘[`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with)’ statement makes code cleaner where you would otherwise reach for `try...finally` blocks to guarantee that clean-up code runs. Here I’ll go over the statement the way it’s typically applied. The section after this one looks at how it’s implemented internally and demonstrates how you build objects meant to work with the statement.

The ‘[`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with)’ statement is a control-flow structure whose basic structure is:

```python
with expression [as variable]:
    with-block

```

Evaluating the expression should yield an object that implements the context management protocol (in other words, one that has [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) and [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) methods).

Before *with-block* runs, the object’s [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) is invoked, giving it the chance to execute set-up code. It can additionally hand back a value, which gets bound to the name *variable* when one is supplied. (Take care to note that *variable* is *not* set to the outcome of *expression*.)

Once the *with-block* has run to completion, the object’s [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) method fires — this happens even when the block threw an exception — so it can carry out clean-up code.

A number of standard Python objects have gained support for the context management protocol and so can be paired with the ‘[`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with)’ statement. File objects are one example:

```python
with open('/etc/passwd', 'r') as f:
    for line in f:
        print line
        ... more processing code ...

```

Once this statement finishes running, the file object held in *f* will have been closed for you automatically, even should the [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) loop throw an exception somewhere in the middle of the block.

Note

Here, *f* is the very object that [`open()`](https://docs.python.org/3.14/library/functions.html#open) produced, since [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) returns *self*.

Locks and condition variables from the [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module likewise work with the ‘[`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with)’ statement:

```python
lock = threading.Lock()
with lock:
    # Critical section of code
    ...

```

The block runs only after the lock has been acquired, and the lock is invariably released once the block ends.

Within the [`decimal`](https://docs.python.org/3.14/library/decimal.html#module-decimal) module, the [`localcontext()`](https://docs.python.org/3.14/library/decimal.html#decimal.localcontext) function provides a simple way to preserve and then restore the active decimal context, which holds the precision and rounding behavior you want for your calculations:

```python
from decimal import Decimal, Context, localcontext

# Displays with default precision of 28 digits
v = Decimal('578')
print v.sqrt()

with localcontext(Context(prec=16)):
    # All code in this block uses a precision of 16 digits.
    # The original context is restored on exiting the block.
    print v.sqrt()

```

[Subject index](INDEX.md) · [Previous source section](new-documentation-format-restructuredtext-using-sphinx.md) · [Next source section](writing-context-managers.md) · [Release/subject declaration](python-3-0.md)
