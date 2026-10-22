# What's New in Python 2.5 / PEP 352: Exceptions as New-Style Classes — sys

### PEP 352: Exceptions as New-Style Classes

Going forward exception classes are allowed to be new-style classes rather than only classic classes, and the built-in [`Exception`](https://docs.python.org/3.14/library/exceptions.html#Exception) class together with every standard built-in exception ([`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError), [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError), and so on) are now new-style classes.

The class hierarchy used for exceptions has been reorganized somewhat. Within 2.5, the inheritance looks like this:

```python
BaseException       # New in Python 2.5
|- KeyboardInterrupt
|- SystemExit
|- Exception
   |- (all other current built-in exceptions)

```

The motivation for this reshuffle is that programmers frequently wish to trap every exception signaling a program error. Yet [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt) and [`SystemExit`](https://docs.python.org/3.14/library/exceptions.html#SystemExit) are not errors; they typically stand for a deliberate act, like the user pressing Control-C or the code invoking [`sys.exit()`](https://docs.python.org/3.14/library/sys.html#sys.exit). Since a plain `except:` traps everything, you'd often have to name `KeyboardInterrupt` and `SystemExit` explicitly just to re-raise them. The customary idiom looks like:

```python
try:
    ...
except (KeyboardInterrupt, SystemExit):
    raise
except:
    # Log error...
    # Continue running program...

```

Under Python 2.5 you may instead write `except Exception` for the same outcome — catching the exceptions that normally signal errors while leaving [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt) and [`SystemExit`](https://docs.python.org/3.14/library/exceptions.html#SystemExit) untouched. Just as before, a plain `except:` continues to trap every exception.

What Python 3.0 is aiming for is to mandate that any class thrown as an exception inherit from [`BaseException`](https://docs.python.org/3.14/library/exceptions.html#BaseException) or some descendant of `BaseException`, and upcoming releases in the Python 2.x line might start enforcing that rule. With that in mind, I'd advise you to start deriving all of your exception classes from [`Exception`](https://docs.python.org/3.14/library/exceptions.html#Exception) right away. There's been a proposal that the plain `except:` form ought to disappear in Python 3.0, but Guido van Rossum has yet to decide one way or the other.

Throwing strings as exceptions, like the statement `raise "Error occurred"`, is deprecated as of Python 2.5 and now produces a warning. The intent is to drop the string-exception feature after a handful of releases.

See also

[**PEP 352**](https://peps.python.org/pep-0352/) - Required Superclass for Exceptions

PEP authored by Brett Cannon and Guido van Rossum; implemented by Brett Cannon.

[Subject index](INDEX.md) · [Previous source section](the-contextlib-module.md) · [Next source section](pep-353-using-ssize-t-as-the-index-type.md) · [Release/subject declaration](pep-308-conditional-expressions.md)
