# test — Running tests using the command-line interface

### Running tests using the command-line interface

Because of the [`-m`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-m) option, the `test` package can be launched as a script that drives Python's regression test suite: **python -m test**. Internally this relies on `test.regrtest`; the older invocation **python -m test.regrtest** from earlier Python releases continues to function. Launching the script with no arguments kicks off every regression test in the `test` package automatically. It accomplishes this by locating each module in the package whose name begins with `test_`, importing those modules, and then running the `test_main()` function when one is present, or otherwise loading the tests through unittest.TestLoader.loadTestsFromModule when `test_main` is absent. You can also hand the names of specific tests to the script. Naming just one regression test (**python -m test test_spam**) trims the output, reporting only whether that test passed or failed.

When you run `test` directly you can configure which resources the tests are permitted to use. That is controlled through the `-u` command-line option. Passing `all` as the `-u` value turns on every available resource: **python -m test -uall**. When you want everything except a single resource (the more frequent situation), append a comma-separated list of the unwanted resources after `all`. So **python -m test -uall,-audio,-largefile** runs `test` enabling all resources apart from the `audio` and `largefile` ones. To see every resource plus additional command-line options, run **python -m test -h**.

Additional means of running the regression tests vary with the platform you run them on. On Unix, run **make test** from the top-level directory in which Python was compiled. On Windows, running **rt.bat** out of your `PCbuild` directory executes the full regression suite.

Added in version 3.14: By default the output carries color; you govern this by [controlling it with environment variables](https://docs.python.org/3.14/using/cmdline.html#using-on-controlling-color).

[Subject index](INDEX.md) · [Previous](sequence-acceptance-test-mixin-example.md) · [Continue](../test-support/test-support-testfailed-to-test-support-internet-timeout.md) · [Owning module, declaration or section: test](test-regression-tests-package-for-python.md)
