# doctest: DocTest examples, globals and source metadata

examples

A list of `Example` objects that encode the separate interactive Python examples this test is meant to run.

 globs

The namespace (also called globals) within which the examples run. This is a dictionary that maps names onto values. Whatever the examples do to the namespace (such as binding fresh variables) shows up in `globs` once the test has run.

 name

A string name that identifies the `DocTest`. This is generally the name of the object or file the test was pulled from.

 filename

The name of the file that this `DocTest` came out of; or `None` when the filename is unknown, or when the `DocTest` did not come from a file.

 lineno

The line number inside `filename` at which this `DocTest` starts, or `None` when the line number cannot be had. This line number is zero-based relative to the start of the file.

 docstring

The string the test was pulled from, or `None` when that string is unavailable, or when the test did not come from a string.

[Subject index](INDEX.md) · [Previous](doctest-doctest-class.md) · [Continue](doctest-example-class.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md) · [Owning module, declaration or section: doctest.DocTest](doctest-doctest-class.md) · [Owning module, declaration or section: DocTest Objects](doctest-doctest-class.md)
