# doctest: `doctest.DebugRunner`

*class *doctest.DebugRunner(*checker=None*, *verbose=None*, *optionflags=0*)

A `DocTestRunner` subclass that throws an exception the instant a failure turns up. Where an unexpected exception arises, it raises an `UnexpectedException` carrying the test, the example, and the original exception. Where the output fails to agree, it raises a `DocTestFailure` carrying the test, the example, and the actual output.

Details on the constructor parameters and the methods live in the `DocTestRunner` documentation within the Advanced API section.

Instances of `DebugRunner` may throw either of two exceptions:

[Subject index](INDEX.md) · [Previous](doctest-script-from-examples-to-doctest-debug-src.md) · [Continue](doctest-doctestfailure-to-unexpectedexception-exc-info.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md) · [Owning module, declaration or section: Debugging](debugging.md)
