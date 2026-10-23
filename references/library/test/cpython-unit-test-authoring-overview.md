# test - Writing Unit Tests for the `test` package - Section introduction and initial examples

### Writing Unit Tests for the `test` package

Tests built on the [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) module are expected to honor a handful of conventions. First, give the test module a name that begins with `test_` and finishes with the name of whichever module it covers. Inside that module, every test method should likewise begin with `test_` and close with wording that describes what the method checks. The test driver relies on this naming to spot the methods as tests. Furthermore, omit any documentation string from the method. Instead, supply documentation for a test method through a comment (for instance, `# Tests function returns only True or False`). The reason is that documentation strings, when present, are echoed to output, which leaves the identity of the running test unclear.

A basic boilerplate is often used:

```python
import unittest
from test import support

class MyTestCase1(unittest.TestCase):

    # Only use setUp() and tearDown() if necessary

    def setUp(self):
        ... code to execute in preparation for tests ...

    def tearDown(self):
        ... code to execute to clean up after tests ...

    def test_feature_one(self):
        # Test feature one.
        ... testing code ...

    def test_feature_two(self):
        # Test feature two.
        ... testing code ...

    ... more test methods ...

class MyTestCase2(unittest.TestCase):
    ... same structure as MyTestCase1 ...

... more test classes ...

if __name__ == '__main__':
    unittest.main()

```

With this layout, you can drive the suite through `test.regrtest`, run it standalone as a script that honors the [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) CLI, or invoke it through the `python -m unittest` CLI.

Breaking the code is the aim of regression testing. That objective yields several conventions worth observing:

- Every class, function, and constant should be put through the suite. That covers both the outward-facing API meant for consumers and the “private” code as well.

- Favor whitebox testing, where you look at the code under test as you author the tests. Blackbox testing, which probes only the documented user interface, falls short of confirming that every boundary and edge case is covered.

- Cover every possible value, invalid ones included. Doing so confirms both that all valid values are accepted and that bad values get handled the right way.

- Drive through as many code paths as you can. Find where branches happen and shape the input so that the test traverses as many distinct routes through the code as possible.

- For each bug you uncover in the code under test, add a dedicated test. That guards against the same fault reappearing should the code be altered down the road.

- Tidy up once your tests finish (for example, close and delete every temporary file).

- When a test relies on a particular operating-system condition, confirm that the condition holds before you run the test.

- Pull in as few modules as you can, and import them as early as you can. Doing so keeps the tests' external dependencies low and curbs the chance of strange behavior arising from a module's import side-effects.

- Aim to reuse as much code as possible. Sometimes tests differ only in a detail as minor as the kind of input supplied. Cut duplication by deriving from a base test class, then having a subclass supply the input:

[Subject index](INDEX.md) · [Previous](test-regression-tests-package-for-python.md) · [Continue](sequence-acceptance-test-mixin-example.md) · [Owning module, declaration or section: test](test-regression-tests-package-for-python.md)
