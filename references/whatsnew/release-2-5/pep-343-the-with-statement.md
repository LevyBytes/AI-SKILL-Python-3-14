# What's New in Python 2.5 / PEP 343: The "with" statement - decimal, threading

### PEP 343: The "with" statement

By using "[`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with)", code that formerly relied on `try...finally` blocks to guarantee that cleanup runs becomes much clearer. Here I'll cover how the statement is typically applied. The following section then turns to the internal mechanics and demonstrates how to build objects that cooperate with it.

The "[`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with)" statement introduces a fresh control-flow construct whose fundamental form looks like:

```python
with expression [as variable]:
    with-block

```

Evaluating the expression should yield an object conforming to the context management protocol — in other words, one providing [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) and [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) methods.

Before the *with-block* runs, the object's [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) gets invoked, so it can perform any set-up work. That call may also hand back a value which becomes bound to *variable* when one is supplied. (Be aware that *variable* does *not* receive the value of *expression*.)

Once the *with-block* has run to completion, the object's [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) method runs — this happens whether or not the block threw an exception — making it a natural place for clean-up logic.

If you want to use the statement under Python 2.5, your module must include the following directive:

```python
from __future__ import with_statement

```

From Python 2.6 onward the statement is on by default.

A number of standard Python objects already implement the context management protocol, so they work directly with "[`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with)". Take file objects as a case in point:

```python
with open('/etc/passwd', 'r') as f:
    for line in f:
        print line
        ... more processing code ...

```

Once that statement completes, the file object referenced by *f* is closed for you automatically — this holds true even when the [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) loop threw an exception somewhere inside the block.

Note

Here, *f* is precisely the object that [`open()`](https://docs.python.org/3.14/library/functions.html#open) produced, since [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) hands back *self*.

Locks and condition variables from the [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module likewise cooperate with the "[`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with)" statement:

```python
lock = threading.Lock()
with lock:
    # Critical section of code
    ...

```

Entry into the block acquires the lock, and on completion the lock is always released.

In the [`decimal`](https://docs.python.org/3.14/library/decimal.html#module-decimal) module, the freshly added `localcontext()` function provides a convenient way to capture and later restore the active decimal context, which bundles together the precision and rounding behavior wanted for calculations:

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

[Subject index](INDEX.md) · [Previous source section](generator-send-and-throw-protocols.md) · [Next source section](writing-context-managers.md) · [Release/subject declaration](pep-308-conditional-expressions.md)
