# load_tests Protocol

#### load_tests Protocol

Added in version 3.2.

A module or package can shape the way its tests get loaded, both in ordinary runs and during test discovery, by supplying a function named `load_tests`.

Where a test module defines `load_tests`, `TestLoader.loadTestsFromModule()` will call it passing these arguments:

```python
load_tests(loader, standard_tests, pattern)

```

in which *pattern* arrives untouched from `loadTestsFromModule` and carries a default of `None`.

A `TestSuite` is what it ought to give back.

Here *loader* is the `TestLoader` instance handling the load, and *standard_tests* are the tests the module would supply on its own by default. Often enough a test module merely wishes to tack tests onto, or pull tests out of, that standard collection. The third argument comes into play while packages are being loaded during test discovery.

A run-of-the-mill `load_tests` function that draws its tests from a particular group of `TestCase` classes might read like this:

```python
test_cases = (TestCase1, TestCase2, TestCase3)

def load_tests(loader, tests, pattern):
    suite = TestSuite()
    for test_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite

```

When discovery kicks off inside a directory that holds a package - whether from the command line or by way of `TestLoader.discover()` - the package's `__init__.py` is examined for `load_tests`. Absent that function, discovery simply descends into the package as if it were any ordinary directory. Where the function is present, finding the package's tests is handed off to `load_tests`, called with these arguments:

```python
load_tests(loader, standard_tests, pattern)

```

What it ought to give back is a `TestSuite` standing in for every test the package holds. (Only the tests gathered out of `__init__.py` end up in `standard_tests`.)

Since the pattern flows into `load_tests`, the package can carry on with test discovery - and even reshape it along the way. A `load_tests` function that does nothing for a test package would read like this:

```python
def load_tests(loader, standard_tests, pattern):
    # top level directory cached on loader instance
    this_dir = os.path.dirname(__file__)
    package_tests = loader.discover(start_dir=this_dir, pattern=pattern)
    standard_tests.addTests(package_tests)
    return standard_tests

```

Changed in version 3.5: Discovery has stopped testing package names against *pattern*, since a package name can never line up with the default pattern anyway.

[Subject index](INDEX.md) · [Previous](unittest-texttestrunner-class-to-unittest-main.md) · [Continue](class-and-module-fixtures.md)
