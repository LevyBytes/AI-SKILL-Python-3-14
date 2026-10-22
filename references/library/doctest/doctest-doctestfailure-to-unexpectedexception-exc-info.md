# doctest: `doctest.DocTestFailure`, `DocTestFailure.test`, `DocTestFailure.example`, `DocTestFailure.got`, `doctest.UnexpectedException`, `UnexpectedException.test`, `UnexpectedException.example`, `UnexpectedException.exc_info`

*exception *doctest.DocTestFailure(*test*, *example*, *got*)

Thrown by `DocTestRunner` to indicate that a doctest example's actual output failed to line up with what was expected. Its constructor arguments seed the attributes bearing the same names.

`DocTestFailure` defines the following attributes:

 DocTestFailure.test

The `DocTest` object in progress at the moment the example failed.

 DocTestFailure.example

Whichever `Example` came up failing.

 DocTestFailure.got

What the example actually output.

 *exception *doctest.UnexpectedException(*test*, *example*, *exc_info*)

Thrown by `DocTestRunner` to flag that a doctest example itself threw an exception nobody expected. The constructor arguments seed the attributes that share their names.

`UnexpectedException` defines the following attributes:

 UnexpectedException.test

The `DocTest` object that was executing at the time the example failed.

 UnexpectedException.example

The particular `Example` that failed.

 UnexpectedException.exc_info

A tuple holding details of the unexpected exception, exactly as [`sys.exc_info()`](https://docs.python.org/3.14/library/sys.html#sys.exc_info) returns it.

[Subject index](INDEX.md) · [Previous](doctest-debugrunner-class.md) · [Continue](soapbox.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md) · [Owning module, declaration or section: Debugging](debugging.md)
