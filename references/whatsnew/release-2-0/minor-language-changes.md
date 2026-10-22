# What’s New in Python 2.0 / Minor Language Changes

You can now route the output of a `print` statement to any file-like object by placing `>> file` after the `print`, mirroring the redirection operator found in Unix shells. Before this, the alternatives were to call the file-like object's `write()` method (which gives up the ease and brevity of `print`), or to temporarily point `sys.stdout` at a new value before putting the original one back. To direct text at standard error, this is now far simpler to write:

```python
print >> sys.stderr, "Warning: action field not supplied"

```

When you import a module you can also give it a different name, via the form `import module as name` or `from module import name as othername`. Thomas Wouters submitted the patch.

The `%` operator gains a fresh formatting style: ‘%r’ inserts the [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) of whatever you pass it. It was added for the sake of symmetry, here matching the already-present ‘%s’ style, which inserts the [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) of its argument. As an illustration, `'%r %s' % ('abc', 'abc')` yields a string holding `'abc' abc`.

Up to now there was no mechanism for writing a class that replaced Python’s built-in [`in`](https://docs.python.org/3.14/reference/expressions.html#in) operator with its own behavior. `obj in seq` evaluates to true when *obj* appears somewhere in the sequence *seq*; under the hood Python walks every index of the sequence until it locates *obj* or hits an [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError). Moshe Zadka submitted a patch introducing the `__contains__()` magic method so a class can supply its own definition for `in`. On top of that, freshly written built-in objects in C can declare the meaning of `in` for themselves through a new slot in the sequence protocol.

Older Python builds relied on recursion to delete objects. Sufficiently deep data structures could overflow the interpreter’s C stack and crash it; Christian Tismer reworked the deletion code to eliminate that failure. Similarly, comparing recursive objects used to recurse without end and crash; Jeremy Hylton revised that code so it stops crashing and instead returns something meaningful. As an example, once this runs:

```python
a = []
b = []
a.append(a)
b.append(b)

```

The comparison `a==b` evaluates to true, since the pair of recursive data structures are isomorphic. For the discussion that fed into this implementation, plus a few handy related links, look at the thread “trashcan and PR#7” in the python-dev mailing list’s April 2000 archives. Be aware that comparisons may now also throw exceptions. Under older Python, a comparison like `cmp(a,b)` always handed back an answer, even when a user-supplied `__cmp__()` method ran into trouble, because the exception that arose was just quietly discarded.

Effort has gone into bringing Python to 64-bit Windows running on the Itanium processor, chiefly thanks to Trent Mick of ActiveState. (Oddly, `sys.platform` remains `'win32'` on Win64, apparently because to simplify porting MS Visual C++ compiles the code as 32 bit on Itanium.) PythonWin handles Windows CE as well; visit the Python CE page at [https://pythonce.sourceforge.net/](https://pythonce.sourceforge.net/) for further details.

Yet another fresh platform is Darwin/MacOS X, whose first round of support ships in Python 2.0. Dynamic loading is functional provided you pass “configure –with-dyld –with-suffix=.x”. See the README inside the Python source distribution for additional guidance.

There has been an effort to ease one of Python’s rough edges, the frequently puzzling [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError) exception thrown when code names a local variable that has not yet received a value. As an example, the snippet below throws an exception at the `print` statement under both 1.5.2 and 2.0; in 1.5.2 the exception thrown is `NameError`, whereas 2.0 throws the brand-new [`UnboundLocalError`](https://docs.python.org/3.14/library/exceptions.html#UnboundLocalError) exception. Because `UnboundLocalError` derives from `NameError`, any code already counting on a `NameError` being thrown should keep working.

```python
def f():
    print "i=",i
    i = i + 1
f()

```

There are two fresh exceptions, [`TabError`](https://docs.python.org/3.14/library/exceptions.html#TabError) and [`IndentationError`](https://docs.python.org/3.14/library/exceptions.html#IndentationError). Each one derives from [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError), and they fire whenever Python source turns out to be incorrectly indented.

### Minor Language Changes

A new syntax makes calling a given function more convenient when you’re supplying a tuple of positional arguments, a dictionary of keyword arguments, or both at once. Under Python 1.5 and earlier, you’d reach for the `apply()` built-in: writing `apply(f, args, kw)` runs the function `f()`, handing it *args* as its positional tuple together with the keyword arguments stored in the dictionary *kw*. That `apply()` works the same way in 2.0, yet a patch contributed by Greg Ewing makes `f(*args, **kw)` a shorter and clearer route to the very same outcome. This syntax mirrors the syntax used for defining functions:

```python
def f(*args, **kw):
    # args is a tuple of positional args,
    # kw is a dictionary of keyword args
    ...

```

[Subject index](INDEX.md) · [Next source section](changes-to-built-in-functions.md) · [Release/subject declaration](introduction.md) · [Previous source section](other-core-changes.md)
