# doctest`doctest` - Test interactive Python examples - Section introduction and initial examples

### `doctest` - Test interactive Python examples

**Source code:** [Lib/doctest.py](https://github.com/python/cpython/tree/3.14/Lib/doctest.py)

---

The `doctest` module hunts through text for fragments resembling interactive Python sessions, then runs each one to confirm it behaves precisely the way the example claims. People typically reach for doctest in a handful of ways:

- Confirm that a module's docstrings remain current, by re-running every interactive example to ensure it still behaves as documented.

- Carry out regression testing, checking that the interactive examples drawn from a test file or test object behave the way they should.

- Compose tutorial-style documentation for a package, generously seasoned with input-output examples. Whether the spotlight falls on the examples or on the explanatory prose, the result feels like either "literate testing" or "executable documentation".

What follows is a complete, though compact, example module:

The complete program is in the [upstream source](https://docs.python.org/3.14/library/doctest.html#module-doctest).

Invoke `example.py` straight from the command line and `doctest` quietly does its job:

[Subject index](INDEX.md) · [Continue](interactive-example-testing-command.md)
