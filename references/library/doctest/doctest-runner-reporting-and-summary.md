# doctest.DocTestRunner: `report_start()`, `report_success()`, `report_failure()`, `report_unexpected_exception()`, `run()`, `summarize()`

report_start(*out*, *test*, *example*)

Signal that the test runner is on the verge of handling the named example. The method exists so that `DocTestRunner` subclasses can shape their own output; do not invoke it yourself.

Here *example* is the one about to be handled, *test* is the test holding *example*, and *out* is the output function that was given to `DocTestRunner.run()`.

 report_success(*out*, *test*, *example*, *got*)

Signal that the named example completed without error. This method is there to let `DocTestRunner` subclasses shape their own output; refrain from calling it directly.

In this case *example* is the one about to be handled, *got* holds the example's actual output, *test* is the test holding *example*, and *out* is the output function handed to `DocTestRunner.run()`.

 report_failure(*out*, *test*, *example*, *got*)

Signal that the named example came up failing. The method is supplied so `DocTestRunner` subclasses can shape their output; you should not call it yourself.

For this one, *example* is the one about to be handled, *got* carries the actual output of the example, *test* is the test holding *example*, and *out* is the output function passed along to `DocTestRunner.run()`.

 report_unexpected_exception(*out*, *test*, *example*, *exc_info*)

Signal that the named example threw an exception nobody expected. This method is offered so `DocTestRunner` subclasses can shape their own output; do not invoke it directly.

Here *example* is the one about to be handled, *exc_info* is a tuple of details about that unexpected exception (just as [`sys.exc_info()`](https://docs.python.org/3.14/library/sys.html#sys.exc_info) returns), *test* is the test holding *example*, and *out* is the output function that was passed to `DocTestRunner.run()`.

 run(*test*, *compileflags=None*, *out=None*, *clear_globs=True*)

Execute the examples held in *test* (a `DocTest` object) and present the outcomes through the writer function *out*. A `TestResults` instance is handed back.

Those examples execute inside the `test.globs` namespace. When *clear_globs* is true — the default — that namespace gets wiped once the test finishes, which aids garbage collection. To inspect the namespace after the test wraps up, pass *clear_globs=False* instead.

The *compileflags* value supplies the flags the Python compiler is to apply while running the examples. Left unspecified, it falls back to the collection of future-import flags relevant to *globs*.

Every example's output is vetted by the `DocTestRunner`'s output checker, and the `DocTestRunner.report_*()` methods then format the results.

 summarize(*verbose=None*)

Write out a recap of every test case this DocTestRunner has executed, and give back a `TestResults` instance.

How thorough that recap is depends on the optional *verbose* argument. With no verbosity given, the `DocTestRunner`'s own verbosity setting applies.

`DocTestParser` has the following attributes:

 tries

How many examples were attempted.

 failures

How many examples failed.

 skips

How many examples were skipped.

Added in version 3.13.

[Subject index](INDEX.md) · [Previous](doctest-doctestrunner-class.md) · [Continue](doctest-outputchecker-class.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md) · [Owning module, declaration or section: doctest.DocTestRunner](doctest-doctestrunner-class.md) · [Owning module, declaration or section: DocTestRunner objects](doctest-doctestrunner-class.md)
