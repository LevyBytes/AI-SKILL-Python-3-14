# doctest: Example source, expected output and exception fields

source

A string that holds the example's source code. This source code is made up of a single Python statement and always finishes with a newline; the constructor supplies a newline where one is needed.

 want

The output expected from running the example's source code (whether from stdout or, in the case of an exception, a traceback). `want` finishes with a newline unless no output is expected, in which case it is an empty string. The constructor supplies a newline where one is needed.

 exc_msg

The exception message the example produces, when the example is expected to raise an exception; or `None` when it is not expected to raise one. That exception message is checked against the return value of [`traceback.format_exception_only()`](https://docs.python.org/3.14/library/traceback.html#traceback.format_exception_only). `exc_msg` finishes with a newline unless it is `None`. The constructor supplies a newline where one is needed.

 lineno

The line number inside the string that holds this example at which the example starts. This line number is zero-based relative to the start of the holding string.

 indent

The example's indentation within the holding string, that is, how many space characters come before the example's first prompt.

 options

A dictionary that maps option flags onto `True` or `False`, used to override the default options for this example. Any option flags absent from that dictionary keep their default value (as set by the `DocTestRunner`'s optionflags). By default, no options are set.

[Subject index](INDEX.md) · [Previous](doctest-example-class.md) · [Continue](doctest-doctestfinder-class.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md) · [Owning module, declaration or section: doctest.Example](doctest-example-class.md) · [Owning module, declaration or section: Example Objects](doctest-example-class.md)
