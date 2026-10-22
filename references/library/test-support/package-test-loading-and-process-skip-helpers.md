# test.support — `test.support` — Utilities for the Python test suite

test.support.load_package_tests(*pkg_dir*, *loader*, *standard_tests*, *pattern*)

A general-purpose implementation of the [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) `load_tests` protocol meant for use inside test packages. *pkg_dir* names the package's root directory; *loader*, *standard_tests*, and *pattern* are the arguments that `load_tests` expects. For straightforward situations, the test package's `__init__.py` may read as follows:

```python
import os
from test.support import load_package_tests

def load_tests(*args):
    return load_package_tests(os.path.dirname(__file__), *args)

```

 test.support.detect_api_mismatch(*ref_api*, *other_api*, ***, *ignore=()*)

Yields the collection of attributes, functions, or methods present on *ref_api* but absent from *other_api*, apart from a designated list of entries to disregard during this check, given via *ignore*.

By default, this passes over private attributes that start with '_', yet it keeps every magic method, that is, those that both begin and end with '__'.

Added in version 3.5.

 test.support.patch(*test_instance*, *object_to_patch*, *attr_name*, *new_value*)

Replaces *object_to_patch.attr_name* with *new_value*. It additionally registers a cleanup routine on *test_instance* that reinstates *object_to_patch* at *attr_name*. The *attr_name* must be a legitimate attribute of *object_to_patch*.

 test.support.run_in_subinterp(*code*)

Executes *code* inside a subinterpreter. Raises [`unittest.SkipTest`](https://docs.python.org/3.14/library/unittest.html#unittest.SkipTest) when [`tracemalloc`](https://docs.python.org/3.14/library/tracemalloc.html#module-tracemalloc) is active.

 test.support.check_free_after_iterating(*test*, *iter*, *cls*, *args=()*)

Confirms that instances of *cls* get deallocated once iteration completes.

 test.support.missing_compiler_executable(*cmd_names=[]*)

Verifies whether the compiler executables named in *cmd_names* exist — or all compiler executables when *cmd_names* holds nothing — and returns either the first executable found absent or `None` when each one is present.

 test.support.check__all__(*test_case*, *module*, *name_of_module=None*, *extra=()*, *not_exported=()*)

Confirms that the `__all__` variable belonging to *module* lists every public name.

A module's public names (its API) are found automatically according to whether each matches the public-name convention and was defined within *module*.

The *name_of_module* argument may indicate (as a string or a tuple of strings) which module(s) an API could be defined within so that it counts as a detected public API. This applies, for instance, when *module* pulls some of its public API in from other modules, perhaps a C backend (such as `csv` together with its `_csv`).

The *extra* argument may hold a set of names that would not otherwise be picked up automatically as "public," such as objects lacking a correct [`__module__`](https://docs.python.org/3.14/library/stdtypes.html#definition.__module__) attribute. When supplied, it gets merged with those detected automatically.

The *not_exported* argument may hold a set of names that should be excluded from the public API regardless of whether their names suggest otherwise.

Example use:

```python
import bar
import foo
import unittest
from test import support

class MiscTestCase(unittest.TestCase):
    def test__all__(self):
        support.check__all__(self, foo)

class OtherTestCase(unittest.TestCase):
    def test__all__(self):
        extra = {'BAR_CONST', 'FOO_CONST'}
        not_exported = {'baz'}  # Undocumented name.
        # bar imports part of its API from _bar.
        support.check__all__(self, bar, ('bar', '_bar'),
                             extra=extra, not_exported=not_exported)

```

Added in version 3.6.

 test.support.skip_if_broken_multiprocessing_synchronize()

Skips tests when the `multiprocessing.synchronize` module cannot be found, when no semaphore implementation is on hand, or when constructing a lock triggers an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

Added in version 3.10.

[Subject index](INDEX.md) · [Previous](musl-detection-and-unraisable-exception-helpers.md) · [Continue](instantiation-checks-and-integer-digit-limit-helpers.md) · [Owning module, declaration or section: test.support](test-support-testfailed-to-test-support-internet-timeout.md)
