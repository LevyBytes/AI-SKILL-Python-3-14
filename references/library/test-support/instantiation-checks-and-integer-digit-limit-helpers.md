# test.support`test.support` - Utilities for the Python test suite

test.support.check_disallow_instantiation(*test_case*, *tp*, **args*, ***kwds*)

Confirms that the type *tp* cannot be created via *args* and *kwds*.

Added in version 3.10.

 test.support.adjust_int_max_str_digits(*max_digits*)

Hands back a context manager that adjusts the global [`sys.set_int_max_str_digits()`](https://docs.python.org/3.14/library/sys.html#sys.set_int_max_str_digits) setting for the span of the context, so that test code needing a different cap on the digit count while converting between an integer and a string can run.

Added in version 3.11.

The `test.support` module defines the following classes:

[Subject index](INDEX.md) · [Previous](package-test-loading-and-process-skip-helpers.md) · [Continue](test-support-suppresscrashreport-class.md) · [Owning module, declaration or section: test.support](test-support-testfailed-to-test-support-internet-timeout.md)
