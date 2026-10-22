# doctest: `doctest.set_unittest_reportflags()`

doctest.set_unittest_reportflags(*flags*)

Configure the `doctest` reporting flags to use.

The *flags* argument accepts the [bitwise OR](https://docs.python.org/3.14/reference/expressions.html#bitwise) of option flags. Consult the Option Flags section. Only "reporting flags" are permitted.

This setting is module-global and influences every future doctest run by module [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest): the `runTest()` method of `DocTestCase` consults the option flags given for the test case at the moment the `DocTestCase` instance was built. When no reporting flags were given (the usual and anticipated case), the `unittest` reporting flags of `doctest` are [bitwise ORed](https://docs.python.org/3.14/reference/expressions.html#bitwise) into the option flags, and the so-augmented option flags pass to the `DocTestRunner` instance that gets created to run the doctest. When reporting flags were given at the time the `DocTestCase` instance was built, the `unittest` reporting flags of `doctest` are disregarded.

The function returns whatever value the [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) reporting flags held just before the function was called.

[Subject index](INDEX.md) · [Previous](doctest-docfilesuite-to-doctest-doctestsuite.md) · [Continue](advanced-api.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md) · [Owning module, declaration or section: Unittest API](doctest-docfilesuite-to-doctest-doctestsuite.md)
