# doctest: `doctest.DocTestRunner`

### DocTestRunner objects

 *class *doctest.DocTestRunner(*checker=None*, *verbose=None*, *optionflags=0*)

A worker class that runs and checks the interactive examples held in a `DocTest`.

Matching expected outputs against actual ones is the job of an `OutputChecker`. You can tailor that matching with a range of option flags, detailed under the Option Flags section. Where the flags do not go far enough, you can further tailor it by handing a subclass of `OutputChecker` to the constructor.

There are two avenues for governing what the test runner displays. The first is to give `run()` an output function, which then receives the strings meant to appear; by default that function is `sys.stdout.write`. When merely capturing the output falls short, you can instead subclass DocTestRunner and override its `report_start()`, `report_success()`, `report_unexpected_exception()`, and `report_failure()` methods.

By way of the optional keyword argument *checker* you name the `OutputChecker` object — or a drop-in stand-in — tasked with weighing the expected outputs against the actual outputs of doctest examples.

The optional keyword argument *verbose* dictates how chatty the `DocTestRunner` is. Set it to `True` and details about every example are printed as that example runs; set it to `False` and only the failures show up. Leave *verbose* out, or pass `None`, and verbose output kicks in precisely when the `-v` command-line switch is supplied.

With the optional keyword argument *optionflags* you steer both how the test runner weighs expected output against actual output and how it presents failures. The Option Flags section has the fuller story.

Statistics pile up as the test runner works. Running totals of attempted, failed, and skipped examples can be read off the `tries`, `failures`, and `skips` attributes. Both `run()` and `summarize()` give back a `TestResults` instance.

`DocTestRunner` defines the following methods:

[Subject index](INDEX.md) · [Previous](testresults-objects.md) · [Continue](doctest-runner-reporting-and-summary.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md)
