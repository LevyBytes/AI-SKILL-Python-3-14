# test — `test` — Regression tests package for Python

### `test` — Regression tests package for Python

Note

Python alone is the intended consumer of the `test` package; it exists for internal purposes. The documentation here serves Python's core developers. Relying on this package from anywhere outside Python's standard library is not recommended, because the code described here may shift or disappear without warning from one Python release to the next.

---

Every regression test for Python lives in the `test` package, which also ships the `test.support` and `test.regrtest` modules. You use `test.support` to augment your own tests, whereas `test.regrtest` runs the suite.

Within the `test` package, any module whose name begins with `test_` forms a test suite covering one particular module or feature. Author every new test with the [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) or [`doctest`](https://docs.python.org/3.14/library/doctest.html#module-doctest) module. A handful of older tests follow a “traditional” approach that checks output sent to `sys.stdout`; that approach is now regarded as deprecated.

See also

Module [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest)

Writing PyUnit regression tests.

Module [`doctest`](https://docs.python.org/3.14/library/doctest.html#module-doctest)

Tests embedded in documentation strings.

[Subject index](INDEX.md) · [Continue](cpython-unit-test-authoring-overview.md)
