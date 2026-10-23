# unittest - Re-using old test code

### Re-using old test code

Certain users will discover they already have test code that they'd like to drive from `unittest`, without rewriting each of their old test functions as a `TestCase` subclass.

To address this, `unittest` includes a `FunctionTestCase` class. That subclass of `TestCase` lets you wrap an existing test function. You may also provide set-up and tear-down functions.

Suppose you have the test function below:

```python
def testSomething():
    something = makeSomething()
    assert something.name is not None
    # ...

```

you can produce a matching test case instance like the following, with set-up and tear-down methods being optional:

```python
testcase = unittest.FunctionTestCase(testSomething,
                                     setUp=makeSomethingDB,
                                     tearDown=deleteSomethingDB)

```

Note

`FunctionTestCase` can serve to swiftly migrate an existing test base onto a `unittest`-based system, yet this route is not recommended. Investing the effort to set up proper `TestCase` subclasses will make future test refactorings vastly easier.

Sometimes the tests you already have were authored with the [`doctest`](https://docs.python.org/3.14/library/doctest.html#module-doctest) module. When that's the case, `doctest` supplies a [`DocTestSuite`](https://docs.python.org/3.14/library/doctest.html#doctest.DocTestSuite) class capable of building `unittest.TestSuite` instances automatically from those existing `doctest`-based tests.

[Subject index](INDEX.md) · [Previous](standalone-test-module-execution.md) · [Continue](skipping-tests-and-expected-failures.md) · [Owning module, declaration or section: unittest](unittest-unit-testing-framework.md)
