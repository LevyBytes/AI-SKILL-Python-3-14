# unittest — `unittest` — Unit testing framework

### `unittest` — Unit testing framework

**Source code:** [Lib/unittest/__init__.py](https://github.com/python/cpython/tree/3.14/Lib/unittest/__init__.py)

---

(Readers who already understand the fundamentals of testing may prefer to jump ahead to the list of assert methods.)

Drawing its initial design from JUnit, the `unittest` unit testing framework feels familiar alongside the major unit testing frameworks found in other programming languages. The framework handles test automation, lets tests share their setup and shutdown code, gathers individual tests into collections, and keeps the tests decoupled from the reporting framework.

`unittest` realizes this by modeling several key concepts using an object-oriented design:

test fixture

The term *test fixture* refers to whatever groundwork must be laid to carry out one or more tests, plus any cleanup that goes with it. Examples of such groundwork include spinning up a server process or creating temporary or proxy databases and directories.

test case

The smallest standalone unit of testing is the *test case*. It confirms that a given set of inputs yields a specific response. A base class named `TestCase` ships with `unittest` for building new test cases.

test suite

A grouping of test cases, of other test suites, or of both, is a *test suite*. Its purpose is to bundle together tests that are meant to run as a unit.

test runner

The component that drives the running of tests and surfaces the results back to the user is the *test runner*. To report what happened when the tests ran, a runner might present a graphical interface, present a textual interface, or hand back a special value.

See also

Module [`doctest`](https://docs.python.org/3.14/library/doctest.html#module-doctest)

A second module for test support, with a markedly different flavor.

[Simple Smalltalk Testing: With Patterns](https://web.archive.org/web/20150315073817/http://www.xprogramming.com/testfram.htm)

The original paper by Kent Beck describing testing frameworks built on the pattern that `unittest` follows.

[pytest](https://docs.pytest.org/)

A third-party unittest framework offering lighter-weight syntax for authoring tests. As an example, `assert func(10) == 42`.

[The Python Testing Tools Taxonomy](https://wiki.python.org/moin/PythonTestingToolsTaxonomy)

A wide-ranging catalog of Python testing tools, covering functional testing frameworks and mock object libraries.

[Testing in Python Mailing List](http://lists.idyll.org/listinfo/testing-in-python)

A special-interest-group devoted to talking about testing, and the tools for testing, within Python.

Bundled in the Python source distribution, the script `Tools/unittestgui/unittestgui.py` is a GUI tool that discovers and runs tests. It exists chiefly to make life easy for people new to unit testing. When it comes to production environments, the recommendation is to let a continuous integration system drive the tests, for instance [Buildbot](https://buildbot.net/), [Jenkins](https://www.jenkins.io/), [GitHub Actions](https://github.com/features/actions), or [AppVeyor](https://www.appveyor.com/).

[Subject index](INDEX.md) · [Continue](basic-example.md)
