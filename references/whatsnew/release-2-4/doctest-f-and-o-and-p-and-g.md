# Python 2.4 changes: Doctest enhancements and failure example

### doctest

A sizable refactoring reshaped the [`doctest`](https://docs.python.org/3.14/library/doctest.html#module-doctest) module, courtesy of Edward Loper and Tim Peters. Running [`doctest.testmod()`](https://docs.python.org/3.14/library/doctest.html#doctest.testmod) remains all it takes to test, yet the rework opens up assorted ways to tailor how the module behaves

Pulling the tests out of an object's docstrings is the job of the new `DocTestFinder` class:

```python
def f (x, y):
    """>>> f(2,2)
4
>>> f(3,2)
6
    """
    return x*y

finder = doctest.DocTestFinder()

# Get list of DocTest instances
tests = finder.find(f)

```

From there the new `DocTestRunner` class executes the tests one by one and can roll up a summary of how they fared:

```python
runner = doctest.DocTestRunner()
for t in tests:
    tried, failed = runner.run(t)

runner.summarize(verbose=1)

```

What the example above prints is shown here:

```python
1 items passed all tests:
   2 tests in f
2 tests in 1 items.
2 passed and 0 failed.
Test passed.

```

To weigh the expected output against what actually appeared, `DocTestRunner` relies on an instance of the `OutputChecker` class. That class accepts a range of flags for shaping its behaviour, and the more adventurous can roll an entirely fresh subclass of `OutputChecker`.

Several convenient capabilities come built into the default output checker. With the [`doctest.ELLIPSIS`](https://docs.python.org/3.14/library/doctest.html#doctest.ELLIPSIS) option flag set, for one, an ellipsis (`...`) sitting in the expected output stands in for any substring, which smooths over outputs that drift in small ways:

```python
def o (n):
    """>>> o(1)
<__main__.C instance at 0x...>
>>>
"""

```

One more reserved string, `<BLANKLINE>`, lines up with an empty line:

```python
def p (n):
    """>>> p(1)
<BLANKLINE>
>>>
"""

```

A further addition lets you render the output diff-style by passing one of the [`doctest.REPORT_UDIFF`](https://docs.python.org/3.14/library/doctest.html#doctest.REPORT_UDIFF) (unified diffs), [`doctest.REPORT_CDIFF`](https://docs.python.org/3.14/library/doctest.html#doctest.REPORT_CDIFF) (context diffs), or [`doctest.REPORT_NDIFF`](https://docs.python.org/3.14/library/doctest.html#doctest.REPORT_NDIFF) (delta-style) option flags. As an example:

```python
def g (n):
    """>>> g(4)
here
is
a
lengthy
>>>"""
    L = 'here is a rather lengthy list of words'.split()
    for word in L[:n]:
        print word

```

[Subject index](INDEX.md) · [Previous source section](cookielib.md) · [Next source section](doctest-is-to-a.md) · [Release/subject declaration](pep-218-built-in-set-objects.md)
