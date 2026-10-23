# doctest - Simple Usage: Checking Examples in a Text File

### Simple Usage: Checking Examples in a Text File

A second straightforward use of doctest is checking interactive examples stored in a text file. The `testfile()` function handles this:

```python
import doctest
doctest.testfile("example.txt")

```

That brief script runs and validates whatever interactive Python examples sit inside the file `example.txt`. Its contents are handled as though they formed one enormous docstring; there's no requirement that the file hold an actual Python program! Suppose, for instance, `example.txt` holds the following:

```none
The ``example`` module
======================

Using ``factorial``
-------------------

This is an example text file in reStructuredText format.  First import
``factorial`` from the ``example`` module:

    >>> from example import factorial

Now use it:

    >>> factorial(6)
    120

```

Invoking `doctest.testfile("example.txt")` will then surface the mistake buried in this documentation:

```python
File "./example.txt", line 14, in example.txt
Failed example:
    factorial(6)
Expected:
    120
Got:
    720

```

Just like `testmod()`, `testfile()` stays silent unless an example breaks. Should one fail, then the failing example(s) and the reason(s) behind the failure(s) land on stdout, in the very same format that `testmod()` uses.

Out of the box, `testfile()` searches the calling module's directory for files. Consult the section Basic API for an account of the optional arguments you can supply to point it at files kept elsewhere.

As with `testmod()`, the verbosity of `testfile()` may be controlled through the `-v` command-line flag or via the optional keyword argument *verbose*.

A command line shortcut also exists for invoking `testfile()`; refer to the section Command-line Usage.

Further detail on `testfile()` lives in the section Basic API.

[Subject index](INDEX.md) · [Previous](simple-usage-checking-examples-in-docstrings.md) · [Continue](command-line-usage.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md)
